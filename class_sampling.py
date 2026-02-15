class Dog:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def walk(self):   
        if self.action == 'w':
            print(f'{self.name} is walking forward')
        elif self.action == "e":
            print(f"{self.name} stopped")
    
    def sleep(self):
        if self.action == 'f':
            print(f"{self.name} is sleeping")
        elif self.action == 'g':
            print(f"{self.name} is awake")

    def eat(self):
        if self.action == 'r':
            print(f"{self.name} is Eating")

dog_name = input("Give the dog a name: ")
while True:
    user_input = input("Press the keys [w,a,s,d,e,f,g,r] to command the dog. e to exit: ")
    Dog(dog_name, user_input)


        
    
