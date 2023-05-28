# Tweepy-OpenAI-Bot
A Twitter bot that uses OpenAI's API to generate a specified number of "Motivational Tweets" and tweets the once per hour.

NOTE: This is a hobby project, there will probably be bugs or inefficient code.

## Set-up
Ensure that you have run:
`pip install -r requirements.txt`
To ensure you have all dependencies.

Run main.py, to generate configurations file, you will recieve a prompt in the terminal to insert your API Keys.

if you havent already generated tweets.csv then it will generate 600 tweets by default.

After the tweets are generated it will tweet one per hour by default


To build the docker image run:
`$ docker build -t tweepyopenai:v0.01 .`
NOTE: **You may want to run the script once before building the docker image so that your config file and API Keys are saved - This may change in the future.**

## Configurations.ini
After running main.py for the first time a file called configurations.ini will be generated.
This holds your API Keys and has 2 settings:

 - tweetCount - The amount of tweets to be generated
 - tweetFrequency - How often to tweet

The tweet count can be as large as you like but has to be a multiple of 60. **NOTE: The larger the Tweet Count, the more you may be charged by OpenAI since they charge per word.**

**tweetFrequency is in seconds, REMEMBER that twitter has a limit on how many times you can tweet per day.**


## Issues
If you come up on any issues or suggestions feel free to drop them on the issues page!
