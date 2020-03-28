import praw
import pandas as pd
import json
import pprint
import datetime
from textblob import TextBlob

"""
Usueful stuff:

https://textblob.readthedocs.io/en/dev/
https://towardsdatascience.com/ultimate-beginners-guide-to-collecting-text-for-natural-language-processing-nlp-with-python-256d113e6184


"""

class Reddit(object):

    def __init__(self):
        self.load_config()
    
    def load_config(self):
        with open("config.json", "r") as jsonfile:
            self.config = json.load(jsonfile)["reddit"]

    def create_connection(self):
        self.reddit = praw.Reddit(client_id= self.config["client-id"],
                                client_secret= self.config["secret"],
                                user_agent= self.config["user-agent"])

    def get_subreddit(self):
        subreddit = self.reddit.subreddit('news').new()
        for post in subreddit:
            created_utc = datetime.datetime.fromtimestamp(post.created_utc)
            title = post.title
            print(f"{created_utc.isoformat()} :: {self.sentiment(title)} :: {title}")

    def sentiment(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity



if __name__ == "__main__":
    
    reddit = Reddit()
    reddit.create_connection()
    reddit.get_subreddit()
    print("Finshed!")