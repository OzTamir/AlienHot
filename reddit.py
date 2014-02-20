import praw

class Subreddit(object):
	'''This class represents a single subreddit and it's hot submissions'''
	def __init__(self, sub):
		self.name = str(sub)
		self.reddit_name = '/r/%s' % self.name.title()
		self.submissions = []
	def add_submission(self, submission):
		self.submissions.append(submission)

class Submission(object):
	'''This class represents a Submission as an Title-URL object'''
	def __init__(self, submission):
		self.url = str(submission.short_link)
		self.title = str(submission).split(':: ')[1]

def get_hot(subreddits, lim):
	'''
	This function gets the lim(By default 5) hot post from each subreddit and return a list of subreddits
	objects - each with it's own hot submissions - as well as a string with all the subreddits's names
	'''
	subs = []
	reddit = praw.Reddit(user_agent='Reddit Summery 1.0 by /u/xXaoSs')
	for sub in subreddits:
		sub = Subreddit(sub)
		submits_gen = reddit.get_subreddit(sub.name).get_hot(limit=lim)
		[sub.add_submission(post) for post in submits_gen]
		subs.append(sub)
	msg = 'Subreddits: '
	for sub in subs:
		msg += sub.reddit_name + ' | '
	msg = msg[:-2]
	return subs, str(msg)