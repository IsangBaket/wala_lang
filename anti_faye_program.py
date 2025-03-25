#This program rejects people like Faye

#Asks user if he likes to take the test again
def again():
    cont = input("do you wish to continue? yes or no: ")
    if cont == "yes":
        test()
    else:
        print("Thank you for testing!")

#The actual test
def test():
    qualifications = ["yes", "yes", "yes"]
    test = [] #stores user input

    print("This program verifies if you are like Faye")

    name = input("please input your name: ") 

    ques1 = input("do you like love and deep space? yes or no: ")
    test.append(ques1)

    ques2 = input("do you like hyunjin? yes or no: ")
    test.append(ques2)

    ques3 = input("do you like san? yes or no: ")
    test.append(ques3)

    if qualifications == test:
        print(f"you are rejected {name}")
        again()
    else:
        print(f"you may pass {name}")
        again()

test()