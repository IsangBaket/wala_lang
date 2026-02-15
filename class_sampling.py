class Dog:
    def __init__(self, name,):
        self.name = name

    def walk(self, action):   
        if action == 'w':
            print(f'{self.name} is walking forward')
        elif action == 'a':
            print(f'{self.name} is walking letfward')
        elif action == 's':
            print(f'{self.name} is walking rightward')
        elif action == 'd':
            print(f'{self.name} is walking backward')
        elif action == "e":
            print(f"{self.name} stopped")
    
    def sleep(self, action):
        if action == 'f':
            print(f"{self.name} is sleeping")
        elif action == 'g':
            print(f"{self.name} is awake")

    def eat(self, action):
        if action == 'r':
            print(f"{self.name} is Eating")






        
    
