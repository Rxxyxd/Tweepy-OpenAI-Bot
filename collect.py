import openai
import time
import multiprocessing
import csv
import config

config = config.read()

tweets = []
process_count = 60
filename = "tweets.csv"
results_queue = multiprocessing.Queue()

def get_response(topic): #Connects to OpenAI API and returns the response
    try:
        openai.api_key = config['API-Keys']['openaiApiKey']
        q = "Give me a "+topic+" tweet"
        response = openai.Completion.create(
            engine="text-davinci-003", #OpenAI Model
            prompt=q,
            temperature=0.7,
            max_tokens=100,
            n=1,
            stop=None,
            timeout=10
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(e)

def get_tweets(): #uses what get_response() returned, adds to list and returns the list
    try:
        tweet = get_response("motivational")
        tweets.append(tweet)
        return tweets
    except Exception as e:
        print(e)

def run_get_tweets_with_queue(func, queue): # starts a queue for the information returned from each process
    result = func()
    queue.put(result)

def run_get_tweets(target_tweets):
    tweets = []
    processes = []
    current_batch = 0
    while len(tweets) != target_tweets:
        batch_num = target_tweets / 60 #defines number of times to run loop
        if current_batch <= batch_num: 
            current_batch +=1
        else: break # breaks out of while loop if batch_num is equal to target_tweets
        print("Batch ",current_batch)
        for _ in range(process_count): #runs defined number of processes for the specified function
            process = multiprocessing.Process(target=run_get_tweets_with_queue, args=(get_tweets, results_queue))
            processes.append(process)
            process.start()
            print("process ",_," Started")
    
        for process in processes:
            process.join()
            print(process) #not required but helps with debugging
        
        while not results_queue.empty(): #apends each returned tweet to the list of tweets
            tweets.append(results_queue.get())
    
        time.sleep(60)
    
    with open(filename, 'w', newline="", encoding="utf-8") as csvfile: #adds liost of tweets to csv file
        writer = csv.writer(csvfile)
        writer.writerow(tweets)
    
    tweets_len = len(tweets)
    print(tweets_len, "tweets collected") # Outputs the number of tweets collected (Not Required but helps with debugging)