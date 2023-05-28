import configparser

# creates the config file
def create():
    config_file = configparser.ConfigParser()

    # Add Section
    config_file.add_section("API-Keys")
    config_file.add_section("Tweet-Settings")
    
    # Get Api Keys
    consumerKey = input("Consumer Key: ")
    consumerSecret = input("Consumer Secret: ")
    accessToken = input("Access Token: ")
    accessTokenSecret = input("Access Token Secret: ")
    bearerToken = input("Bearer Token: ")
    openaiApiKey = input("OpenAI Api Key: ")

    # Add API Keys to API-Keys
    config_file.set("API-Keys", "consumerKey", consumerKey)
    config_file.set("API-Keys", "consumerSecret", consumerSecret)
    config_file.set("API-Keys", "accessToken", accessToken)
    config_file.set("API-Keys", "accessTokenSecret", accessTokenSecret)
    config_file.set("API-Keys", "bearerToken", bearerToken)
    config_file.set("API-Keys", "openaiApiKey", openaiApiKey)

    # Tweet Settings
    config_file.set("Tweet-Settings", "tweetCount", "600")
    config_file.set("Tweet-Settings", "tweetFrequency", "3600")

    # Save File
    with open(r"configurations.ini", "w") as configfileObj:
        config_file.write(configfileObj)
        configfileObj.flush()
        configfileObj.close()

# Opens the config file and returns its contents
def read():
    config = configparser.ConfigParser()
    config.read('configurations.ini')
    return config