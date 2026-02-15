class Dog:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def walk(self, name, action):   
        if action == 'w':
            print(f'{name} is walking forward')
        if action == "e":
            print(f"{name} stopped")
    
    def sleep(self, name, action):
        if action == 'f':
            print(f"{name} is sleeping")
        if action == 'g':
            print(f"{name} is awake")

    def eat(self, name, action):
        if action == 'r':
            print(f"{name} is Eating")

dog_name = input("Give the dog a name: ")
while True:
    user_input=input("press the keys to command the dog: ")
    if user_input == 'x':
        break

Dog(dog_name, user_input)
    
