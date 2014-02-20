from flask import Flask, render_template, url_for, request, redirect, flash
from reddit import get_hot
app = Flask(__name__)

subs = ['jailbreak', 'askreddit']
LIMIT = 5

@app.route('/change_amount', methods=['POST'])
def change_amount():
	global LIMIT
	if int(request.form['amount']) > 0:
		LIMIT = int(request.form['amount'])
	return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add_sub():
	if str(request.form['subreddit']) != '':
		subs.append(str(request.form['subreddit']))
	return redirect(url_for('index'))

@app.route('/')
def index():
	sub_list, sub_msg = get_hot(subs, LIMIT)
	return render_template('index.html', subreddits = sub_list, lst = sub_msg)

if __name__ == '__main__':
    app.run(port=5000, debug=True)


