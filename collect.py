import openai
import time
import multiprocessing
import csv
from dotenv import load_dotenv
load_dotenv()
import os
openai.api_key = os.environ.get('openai_api_key')

tweets = []
process_count = 60
target_tweets = 600
filename = "tweets.csv"

def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
        timeout=10
    )
    return response.choices[0].text.strip()

def get_tweets():
    try:
        tweet = ask_gpt("Give me a motivational tweet")
        tweets.append(tweet)
    except Exception as e:
        print(e)
    return tweets

results_queue = multiprocessing.Queue()

def run_get_tweets_with_queue(func, queue):
    result = func()
    queue.put(result)

def run_get_tweets():
    start = time.time()
    tweets = []
    processes = []
    while len(tweets) != target_tweets:
        batch_num = target_tweets / 60
        current_batch = 0
        if current_batch != batch_num: 
            current_batch +=1
        print("Batch ",current_batch)
        for _ in range(process_count):
            process = multiprocessing.Process(target=run_get_tweets_with_queue, args=(get_tweets, results_queue))
            processes.append(process)
            process.start()
            print("process ",_," Started")
    
        for process in processes:
            process.join()
            print(process)
        
        while not results_queue.empty():
            tweets.append(results_queue.get())
    
        time.sleep(60)
    
    with open(filename, 'w', newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(tweets)
    
    listlen = len(tweets)
    print(listlen, "tweets collected")
    end = time.time()
    print(end - start, "seconds")