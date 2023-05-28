import configparser

# Create Object
config_file = configparser.ConfigParser()

# Add Section
config_file.add_section("API-Keys")

# Add Settings to Section
config_file.set("API-Keys", "consumerKey", "TestKey")
config_file.set("API-Keys", "consumerSecret", "TestKey")
config_file.set("API-Keys", "accessToken", "TestKey")
config_file.set("API-Keys", "accessTokenSecret", "TestKey")
config_file.set("API-Keys", "bearerToken", "TestKey")
config_file.set("API-Keys", "openaiApiKey", "TestKey")

# Save File
with open(r"configurations.ini", "w") as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()