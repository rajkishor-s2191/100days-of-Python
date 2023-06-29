#Challenge-1 Sum of digits of 2-digit number
# a=int(input("Enter a number: "))
# temp=a
# num=temp%10
# temp=temp/10

# res=int(temp+num)

# print(res)

#Challenge-2 BMI Calculator
# h=float(input("Enter height(m): "))
# w=float(input("Enter weight(kg): "))
# bmi = w/(h*h)
# print(bmi)

#Rounding of Numbers
#floor operator - //
# print(round(8/3,2))

#Tip Calculator
print("Welcome")
amt=float(input("What was the total bill"))
percentage=int(input("What percentage tip would you like to give?"))
people=int(input("How many people to split the bill"))
tip= (amt/people)*(percentage*0.01)

print(f"Total Bill : $ {amt+round(tip,2)}")