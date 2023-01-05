import praw
from psaw import PushshiftAPI
import pandas as pd
import datetime as dt
import os

api = PushshiftAPI()

reddit = praw.Reddit(client_id ='zhNcXpKUgU9ZJFmQocuABw', 
		client_secret ='CvSeH0YMj4JnD4KB0tDWoHHGajSvvg', 
		user_agent ='redScrapeProj1', 
)


}

def main():
	subreddits = ['MensRights']
	start_month = 9
	end_month = 11
	# directory on which to store the data
	basecorpus = './my-dataset/'

	for month in range(start_month, end_month+1):
		dirpath = basecorpus + str(month)
		if not os.path.exists(dirpath):
			os.makedirs(dirpath)

	ts_after = int(dt.datetime(2022, month, 1).timestamp())
	ts_before = int(dt.datetime(2022, month+1, 1).timestamp())

	for subreddit in subreddits:
		subredditdirpath = dirpath + '/' + subreddit
		if os.path.exists(subredditdirpath):
			continue
		else:
			os.makedirs(subredditdirpath)
		submissions_csv_path = str(month) + '-' + subreddit + '-submissions.csv'

		submissions_dict = {
			"id" : [],
			"url" : [],
			"title" : [],
			"score" : [],
			"num_comments": [],
			"created_utc" : [],
			"selftext" : [],
		}

		gen = api.search_submissions(
			after = ts_after,
			before = ts_before,
			filter = ['id'],
			subreddit = subreddit,
			limit = 10000
		)

		for submission_psaw in gen:
			submission_id = submission_psaw.d_['id']
			submission_praw = reddit.submission(id=submission_id)
	
			submissions_dict["id"].append(submission_praw.id)
			submissions_dict["url"].append(submission_praw.url)
			submissions_dict["title"].append(submission_praw.title)
			submissions_dict["score"].append(submission_praw.score)
			submissions_dict["num_comments"].append(submission_praw.num_comments)
			submissions_dict["created_utc"].append(submission_praw.created_utc)
			submissions_dict["selftext"].append(submission_praw.selftext)

			submission_comments_csv_path = str(month) + '-' + subreddit + '-submission_' + submission_id + '-comments.csv'
			submission_comments_dict = {
				"comment_id" : [],
				"comment_parent_id" : [],
				"comment_body" : [],
				"comment_link_id" : [],
			}

			submission_praw.comments.replace_more(limit=None)

			for comment in submission_praw.comments.list():
				submission_comments_dict["comment_id"].append(comment.id)
				submission_comments_dict["comment_parent_id"].append(comment.parent_id)
				submission_comments_dict["comment_body"].append(comment.body)
				submission_comments_dict["comment_link_id"].append(comment.link_id)

			pd.DataFrame(submission_comments_dict).to_csv(subredditdirpath + '/' + submission_comments_csv_path, index=False)

	# single csv file with all submissions
		pd.DataFrame(submissions_dict).to_csv(subredditdirpath + '/' + submissions_csv_path, index=False)

main()
