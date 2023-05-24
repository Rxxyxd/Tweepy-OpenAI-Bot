import tweepy
import csv
import random
import ast
from dotenv import load_dotenv
load_dotenv()
import os

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
bearer_token = os.environ.get("bearer_token")

tweets = []

def open_csv(filename):
    with open(filename, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                for i in range(0, len(row)):
                    content = row[i]
                    content_list = ast.literal_eval(content)
                    tweets.append(content_list)
            rand = random.randint(0, 599)
            used_index = []
            exists = True
            while exists:
                if rand in used_index:
                    rand = random.randint(0, 599)
                    continue
                else:
                    exists = False
            tweet = ''.join(tweets[rand])
            return tweet
def tweet():
    client = tweepy.Client(bearer_token=bearer_token , consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
    tweet=open_csv("tweets.csv")
    client.create_tweet(text=tweet)
    print(tweet)
            