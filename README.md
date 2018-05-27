# postSaverReddit
Requested by False1512 in /r/RequestABot — [submission](https://www.reddit.com/r/RequestABot/comments/8mhnrg/a_bot_that_saves_posts_in_a_sub_based_on_author/).

```
1. Get the most recent posts of a sub

2. Run hourly (I was using schedule and time, but that didn't seem to work on pythonanywhere)

3. If an author from a list of authors posted it, save the post.
```
---

## How to run postSaverReddit.py

**0.** Install [Python](https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe).

**1.** Go to [Reddit Apps](https://www.reddit.com/prefs/apps/) and register a new application. Give it a `name`, select `script`, give it a `description` and finally, set the `redirect uri` to **https://127.0.0.1**.

**2.** Clone this repository.

  `$ git clone https://github.com/c-mnzs/postSaveReddit.git` or download as a ZIP.

**43** Open `main.py` and edit the value of the list `author` with the name of the authors you want; change `all` in `subreddit = reddit.subreddit('all')` to be the name of the subreddit you want to monitor submissions in. You may close this file afterwards.

**5.** Open `praw.ini` and edit the values at the bottom. Refer to step 1 for the values.

**6.** Install PRAW using `$ pip install praw`.

**7.** Execute the program by typing `$ py main.py` in a terminal window.

***