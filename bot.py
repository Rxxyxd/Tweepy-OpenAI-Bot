import tweepy
import csv
import random
import ast
import config

config = config.read()

def open_csv(filename): #Opens CSV file and returns a list of tweets
    tweets = []
    with open(filename, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                for i in range(0, len(row)):
                    content = row[i]
                    content_list = ast.literal_eval(content)
                    tweets.append(content_list)
            rand = random.randint(0, int(config["Tweet-Settings"]["tweetCount"])-1)
            used_index = []
            exists = True
            while exists:
                if rand in used_index:
                    rand = random.randint(0, int(config["Tweet-Settings"]["tweetCount"])-1)
                    continue
                else:
                    exists = False
            tweet = ''.join(tweets[rand])
            return tweet    
def tweet(): #Connects to Twitter API V2 and creates a tweet with the content of the CSV file
    consumer_key = config["API-Keys"]["consumerKey"]
    consumer_secret = config["API-Keys"]["consumerSecret"]
    access_token = config["API-Keys"]["accessToken"]
    access_token_secret = config["API-Keys"]["accessTokenSecret"]
    bearer_token = config["API-Keys"]["bearerToken"]
    client = tweepy.Client(bearer_token=bearer_token , consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
    tweet=open_csv("tweets.csv")
    client.create_tweet(text=tweet)
    print(tweet)
            