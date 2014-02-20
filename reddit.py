import praw

class Subreddit(object):
	def __init__(self, sub):
		self.name = str(sub)
		self.reddit_name = '/r/%s' % self.name.title()
		self.submissions = []
	def add_submission(self, submission):
		self.submissions.append(submission)

class Submission(object):
	def __init__(self, submission):
		self.url = str(submission.short_link)
		self.title = str(submission).split(':: ')[1]

def get_hot(subreddits):
	subs = []
	reddit = praw.Reddit(user_agent='Reddit Summery 1.0 by /u/xXaoSs')
	for sub in subreddits:
		sub = Subreddit(sub)
		submits_gen = reddit.get_subreddit(sub.name).get_hot(limit=1)
		[sub.add_submission(post) for post in submits_gen]
		subs.append(sub)
	return subs