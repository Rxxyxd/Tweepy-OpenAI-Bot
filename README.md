# Tweepy-OpenAI-Bot
A Twitter bot that uses OpenAI's API to generate a specified number of "Motivational Tweets" and tweets the once per hour.

NOTE: This is a hobby project, there will probably be bugs or bad code.

# Set-up
Be to create a .env file for your keys. The file should look like this:
```
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
bearer_token = ""
openai_api_key = ""
```
**Remember to put your API Keys in the quotes!**
NOTE: This will likely change in the future for a .cfg file or JSON.

To build the docker image simply run:
`$ docker build -t tweepyopenai:v0.01 .`

# Issues
If you come up on any issues or suggestions feel free to drop them on the issues page!
