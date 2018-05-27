# The needs I have for my program are as follows:
# Get the most recent posts of a sub
# Run hourly (I was using schedule and time, but that didn't seem to work on pythonanywhere)
# If an author from a list of authors posted it, save the post.

import time
import praw

authors = [] # Add authors here e.g: authors = ["Carlos_Menezes", "False1512"]

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('all') # Change this to be the subreddit you'd like to get submissions from.
submissions = subreddit.stream.submissions() # Submissions stream

start_time = time.time() # Getting the time the script is executed at.

while True:
    for submission in submissions: # Checks for new submissions.
            if submission.author.name in authors: # Check if the author is in authors.
                if submission.created_utc > start_time: # Check if the submission was created after the script executed.
                    submission.save()
                    print(f"Saved #{submission.id} | www.reddit.com{submission.url}")
