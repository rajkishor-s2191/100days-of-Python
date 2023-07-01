#Odd or Even
# num=int(input("Enter a number: "))

# if num%2==0:
#     print("Even")
# else:
#     print("Odd")

#Nested if-else
#Challenge-1 BMI
# height=float(input("Enter Height(m): "))
# weight=float(input("Enter weight(kg): "))

# bmi = weight/(height**2)

# if bmi<18.5:
#     print("Underweight")
# elif bmi<25:
#     print("Normal weight")
# elif bmi<30:
#     print("Overweight")
# elif bmi<35:
#     print("Obese")
# else:
#     print("Critically Obese")

#Challenge-2 Leap year

# year=int(input("Enter year: "))

# if year%4==0:
#     if year%100==0:  
#         if year%400==0:
#             print("Leap year")
#         else:
#             print("Not a Leap year")
#     else:
#         print("Leap Year")
# else:
#     print("Not a Leap Year")

#Challenge-3 Pizza Order Challenge
# print("Welcome to Python Pizza Deliveries!")
# size=input("What size of pizza do you want? S,M,L ")
# pepperoni = input("Do you wat to add pepperoni? Y or N ")
# extra_cheese= input("Do you want extra cheese? Y or N ")

# bill = 0

# if size=="S":
#     bill+=15
# elif size=="M":
#     bill+=20
# else:
#     bill+=25

# if pepperoni=="Y":
#     if size=="S":
#         bill+=2
#     else:
#         bill+=3

# if extra_cheese=="Y":
#     bill+=1

# print(f"Your final bill is ${bill}")

#Final Challenge Treasure Island

print("Welcome to Treasure Island. Your mission is to find treasure.")

dir = input("Left of Right? L or R: ")

if dir=="L":
    boat= input("Swim or wait? S or W: ")
    if boat=="W":
        door = input("Choose which door? R,Y,B?")
        if door=="R":
            print("Fire!!! Game Over!!!")
        elif door=="B":
            print("Drowned!!! Game Over!!!")
        else:
            print("You Win!!!!!!")
    else:
        print("Game Over")
else: 
    print("Game Over")