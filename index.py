from flask import Flask, render_template, url_for, request, redirect, flash
from reddit import get_hot, Reddit

app = Flask(__name__)

subs = ['learnpython', 'programming']
LIMIT = 1

reddit = Reddit(subs, LIMIT)

@app.route('/remove', methods=['POST'])
def remove_sub():
	'''Gets called when the "Remove" button underneth each sub'''
	if (str(request.form['subreddit']) != '') and (str(request.form['subreddit']) in reddit.subs):
		reddit.remove(request.form['subreddit'])
	return redirect(url_for('index'))

@app.route('/change_amount', methods=['POST'])
def change_amount():
	'''Gets called when the user invoke the "Change Amount" button'''
	if int(request.form['amount']) > 0:
		reddit.change_amount(request.form['amount'])
	return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add_sub():
	'''Gets called when the user press the "Add!" button'''
	if (str(request.form['subreddit']) != '') and (str(request.form['subreddit']) not in reddit.subs):
		reddit.add(request.form['subreddit'])
	return redirect(url_for('index'))

@app.route('/')
def index():
	sub_list, sub_msg = get_hot(reddit)
	if reddit.limit == 1:
		return render_template('list_em.html', subreddits = sub_list, lst = sub_msg)
	return render_template('index.html', subreddits = sub_list, lst = sub_msg)

if __name__ == '__main__':
    app.run(port=5200,debug=True)


