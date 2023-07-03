#loops
# fruits=['apple','peach','orange','mango']
# for item in fruits:
#     print(item)

#Average height 
# student_heights = [180, 124, 165, 173, 189, 169, 146]
# student_heights = input("Input a list of student heights").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
    
# sum = 0

# for height in student_heights:
#     sum += height

# avg = sum/len(student_heights)
# print(round(avg))

# for a in range(0,9):   #print form 0 to 8 excluding 9
#     print(a)

#Fizzbuzz Exercise
# num = int(input("Enter a number: "))
# for n in range(1, num):
#     if n%3==0 and n%5==0:
#         print("FizzBuzz")
#     elif n%3==0:
#         print("Fizz")
#     elif n%5==0:
#         print("Buzz")
#     else:
#         print(n)

#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))

#print(password_list)
random.shuffle(password_list)
#print(password_list)

password=""
for char in password_list:
    password += char

print(password)