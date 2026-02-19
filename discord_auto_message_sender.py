import requests
import os

def file_name():
    user_input = input("Input a file name: ")
    return user_input

def message_reader(file):
    try:
        with open(file) as f:
            return f.read()
                
    except FileNotFoundError:
        print("bruh di ko mahanap")
        print(f"Current working directory: {os.getcwd()}")
        file_name()

def message_sender(message):
    url = 'https://discord.com/api/v9/channels/1446467532725686334/messages'
    payload = {
        "content" : f"{message}"
    }
    headers = {
        "Authorization" : "classified"
    }
    res = requests.post(url, json=payload, headers=headers)

txt = file_name()
content = message_reader(txt)
message_sender(content)





