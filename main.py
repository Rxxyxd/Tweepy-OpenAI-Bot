# 3rd Party Packages
import os
from os.path import exists
import time
import sys

# Scripts 
import collect
import bot
import config

if __name__ == '__main__':
    config_exists = exists("configurations.ini")
    if config_exists:
        print("Found Config File")
    else:
        config.create()
    config = config.read()
    while True:
        file_exist = os.path.isfile('tweets.csv')
        if not file_exist:
            collect.run_get_tweets(target_tweets=int(config['Tweet-Settings']['tweetCount']))
        else:
            bot.tweet()
            print("Waiting 1 hour")
            for i in range(0, int(config["Tweet-Settings"]["tweetFrequency"])):
                sys.stdout.write(str(i)+'\r')
                sys.stdout.flush()
                time.sleep(1)
            