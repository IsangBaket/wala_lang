import os

def get_filename():
    file_name = input("input your file name(don't for get to include '.txt'): ")
    if not os.path.isfile(file_name):
        raise FileNotFoundError(f"File ''{file_name}' not found")
    return file_name

def text_writer(file_name):
    while True:
        user_input = input("input any thing: (type e to stop program) ")
        if user_input == 'e':
            break
        with open(file_name, 'a') as file:
            file.write(f"{user_input}\n")
            print(f"'{user_input}' has been written")

def main():
    file = get_filename()
    text_writer(file)

main()