from flask import Flask, render_template, url_for, request, redirect, flash
from reddit import get_hot, Reddit

app = Flask(__name__)

# Initial list of subreddits to work with
subs = ['learnpython', 'programming', 'python', 'learnprogramming']

# Initial number of posts to fetch from each sub
LIMIT = 1

# Our reddit object!
reddit = Reddit(subs, LIMIT)

@app.route('/defaults')
def set_defaults():
	global reddit
	'''Gets called when the "Set Defaults" button is pressed'''
	reddit.set_defaults()
	return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove_sub():
	global reddit
	'''Gets called when the "Remove" button underneth a sub gets pressed'''
	if (str(request.form['subreddit']) != '') and (str(request.form['subreddit']) in reddit.subs):
		reddit.remove(request.form['subreddit'])
	return redirect(url_for('index'))

@app.route('/change_amount', methods=['POST'])
def change_amount():
	global reddit
	'''Gets called when the user invoke the "Change Amount" button'''
	if int(request.form['amount']) > 0:
		reddit.change_amount(request.form['amount'])
	return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
	global reddit
	'''Gets called when the user press the "Add!" button'''
	if (str(request.form['username']) != '') and (str(request.form['password']) != ''):
		reddit.login(str(request.form['username']), str(request.form['password']))
	return redirect(url_for('index'))

@app.route('/logout', methods=['POST'])
def logout():
	global reddit
	'''Gets called when the user press the "Add!" button'''
	reddit.logout()
	return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add_sub():
	global reddit
	'''Gets called when the user press the "Add!" button'''
	if (str(request.form['subreddit']) != '') and (str(request.form['subreddit']) not in reddit.subs):
		reddit.add(request.form['subreddit'])
	return redirect(url_for('index'))

@app.route('/')
def index():
	global reddit
	sub_list, sub_msg = get_hot(reddit)
	return render_template('index.html', subreddits = sub_list, lst = sub_msg, reddit = reddit)

if __name__ == '__main__':
    app.run(port=5200,debug=True)


