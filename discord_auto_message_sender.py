import requests
import os

def file_name():
    user_input = input("Input a file name: ")
    return user_input

def message_reader(file):
    try:
        with open(file, 'r') as f:
            for line in f:
                content = line.strip()
                if content:
                    message_sender(content)
                    print(f"Sent: {content}")
                        
    except FileNotFoundError:
        print("bruh di ko mahanap")
        print(f"Current working directory: {os.getcwd()}")
        file_name()

def message_sender(message): 
    key = 'secret'
    url = 'https://discord.com/api/v9/channels/1446467532725686334/messages'
    payload = {
        "content" : f"{message}"
    }
    headers = {
        "Authorization" : key
    }
    res = requests.post(url, json=payload, headers=headers)

def main():
    txt = file_name()
    message_reader(txt)

if __name__ == '__main__':
    main()





