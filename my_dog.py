from class_sampling import Dog

dog_name = input("Give the dog a name: ")
dog = Dog(dog_name)
while True:
    user_input = input("Press the keys [w,a,s,d,e,f,g,r] to command the dog. k to exit: ")
    dog.walk(user_input)
    dog.sleep(user_input)
    dog.eat(user_input)
    if user_input == 'k':
        break
