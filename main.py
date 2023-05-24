import collect
import os
import bot
import time
import sys

if __name__ == '__main__':
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
            