import random

# random_int= random.randint(0,20) # returns a random number
# print(random_int) 

# random_float=random.random() #0.00000 - 0.9999....
# print(random_float)


#lists
# fruits = ["apple","banana","orange","mango"]
# print(fruits[1])
# print(len(fruits))

#Rock Paper Scissors
choice=["Rock","Paper","Scissors"]
user = int(input("What do you choose? Rock(0), Paper(1) and Scissors(2)\n"))
if user>=3 or user<0:
    print("Invalid")
else:
    print("You choose: \n",choice[user])
    computer = random.randint(0,2)
    print("Computer chooses: \n",choice[computer])
    if user==0 and computer==2:
        print("You win!")
    elif computer==0 and user==2:
        print("You lose!")
    elif computer>user:
        print("You lose!")
    elif user>computer:
        print("You Win!")
    elif computer==user:
        print("Draw!")

