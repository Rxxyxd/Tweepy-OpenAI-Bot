# 3rd Party Packages
import os
from os.path import exists
import time
import sys

# Scripts 
import collect
import bot

if __name__ == '__main__':
    config_exists = exists("configurations.ini")
    if config_exists:
        print("Found Config File")
    else:
        print("Generate config")
    while True:
        file_exist = os.path.isfile('tweets.csv')
        if not file_exist:
            collect.run_get_tweets()
        else:
            bot.tweet()
            print("Waiting 1 hour")
            for i in range(0, 3600):
                sys.stdout.write(str(i)+'\r')
                sys.stdout.flush()
                time.sleep(1)
            