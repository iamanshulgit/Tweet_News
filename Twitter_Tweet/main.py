from time import sleep
from news import News
from github import Github
from tweet import Tweet
from database import Database
from newsapi import NewsAPI
from datetime import datetime

current_time = int(datetime.now().strftime("%H%M"))
idx = 0

def reset_db(db):
    db.create_table()
    db.delete_all_tables()
    # change the post_num your wish if its different from 1 and is_github to 0
    db.insert_table()

def db_connect():
    # Get DB connect and setup, fetch data :)
    db = Database()
    # reset_db(db)
    is_github = db.get_is_github()[0]
    post_num = db.get_post_num()[0]
    return (db, is_github, post_num)

def get_content(db, is_github, post_num, newsapi_ele):
    global idx, current_time
    if current_time == 13 and is_github == 0:
        ## To get github post
        print("Get github Post")
        if post_num < 10:
            post = f"0{post_num}"
        else:
            post = f"{post_num}"
        print(f"post number: {post}")
        github_post = Github(post=post)
        content = github_post.get_latest_post(post=post)
        print(f"{github_post} - {content}")

        db.update_is_github()
        db.update_post_num()

    else:
        # To get top rated news
        print("Get News")
        # setup_news = News()
        # setup_news.get_latest_article()
        # content = f"Amazing TechNews:\n{setup_news.get_high_upvotes_article()}\n#technews"

        content = newsapi_ele.get_article(idx=idx)

        # db.update_is_github()
        idx += 1

    # print(content)
    return content

def post_tweet(content):
    # To send the content to tweet
    tweets = Tweet()
    tweets.get_message(content)
    tweets.post_tweet()

def process(db, is_github, post_num, newsapi_ele):
    global current_time
    current_time = int(datetime.now().strftime("%H%M"))
    # content = get_content(db, is_github, post_num, newsapi_ele)
    print(f'content- {datetime.now().strftime("%H%M")}')
    # post_tweet(content)

if __name__ == "__main__":
    # connect to DB
    db, is_github, post_num = db_connect()
    # Connect to NewsAPi
    newsapi_ele = NewsAPI()
    # print(post_num)
    while current_time/100 <= 23:     
        try:
            print(f"Current time(hours): {current_time}")
            process(db, is_github, post_num, newsapi_ele)
        except Exception as e:
            print(f"Exception Raised: {e}")
            sleep(0.01*60*60) # Hold for 4 mins
        else:
            sleep(0.01*60*60) # Hold for 15 mins



    # Reset flag to 0 for next day.
    db.update_is_github()

