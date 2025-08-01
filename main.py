import random 
computer = random.choice([-1, 0, 1])
youstr = input("Enter Your Choise: ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
if youstr not in youDict:
    print ("Invalid input!")
else:
    you = youDict[youstr]
    print (f" You Chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")
    if (you == computer):
        print("Draw")
    else:
        if (you == 1 and computer == 0):
            print("You Lose!")
        elif (you == 1 and computer == -1):
            print("You win!")
        elif (you == 0 and computer == -1):
            print("You Lose!")
        elif (you == 0 and computer == 1):
            print("You Win!")
        elif (you == -1 and computer == 0):
            print("You Win!")
        elif (you == -1 and computer == 1):
            print("You Lose!")
        else:
            print("Somthing Went Wrong!")

    print ("Thank You For Playing  :)")
