import praw
from random import shuffle

class Reddit(object):
	def __init__(self, subs, limit=1):
		self.r = praw.Reddit(user_agent='AlienHot 1.0 by /u/xXaoSs')
		self.subs = subs
		self._subs = []
		self.limit = limit
		self.is_logged = 0
		self.username = ''
		self.is_defaults = 0
	def login(self, user, password):
		self.is_logged = 1
		self.username = str(user)
		self.r.login(str(user), str(password))
		self._subs = list(self.subs)
		self.subs = self.r.get_my_subreddits()
	def logout(self):
		self.is_logged = 0
		self.subs = list(self._subs)
	def add(self, sub):
		self.subs.append(str(sub))
	def remove(self, sub):
		self.subs.remove(str(sub))
	def change_amount(self, new_amount):
		self.limit = int(new_amount)
	def set_defaults(self):
		if self.is_defaults:
			self.subs = list(self._subs)
			self.is_defaults = 0
		else:
			self._subs = list(self.subs)
			self.subs = ['AdviceAnimals', 'AskReddit', 'AskScience', 'Aww', 'BestOf', 'Books', 'EarthPorn', 'ExplainLikeImFive', 'Funny', 'Gaming', \
						'Gifs', 'IAmA', 'Movies', 'Music', 'News', 'Pics', 'Science', 'Sports', 'Technology', 'Television', 'TodayILearned', 'Videos', \
						'WorldNews']
			self.is_defaults = 1

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

def get_hot(r_object):
	'''
	This function gets the lim(By default 5) hot post from each subreddit and return a list of subreddits
	objects - each with it's own hot submissions - as well as a string with all the subreddits's names
	'''
	subreddits, lim = r_object.subs, r_object.limit
	# Let's mix it up a bit, shell we?
	shuffle(subreddits)
	subs = []
	reddit = praw.Reddit(user_agent='AlienHot 1.0 by /u/xXaoSs')
	for sub in subreddits:
		sub = Subreddit(sub)
		submits_gen = reddit.get_subreddit(sub.name).get_hot(limit=lim)
		[sub.add_submission(post) for post in submits_gen]
		subs.append(sub)
	if len(subs) == 0:
		msg = 'No subreddits selected :('
	else:
		msg = 'Subreddits: '
		for sub in subs:
			msg += sub.reddit_name + ' | '
		msg = msg[:-2]
	return subs, str(msg)