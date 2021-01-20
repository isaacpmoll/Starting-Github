# in this file, print your name and ask the user for two numbers,
# then print the larger between the two:  
# pi to the power of the first number 
# or the square root of the second number.
# then commit and push it back up to github.
import math

print("Isaac Moll")

num1 = float(input("Gimme number one: "))
num2 = float(input("Gimme number two: "))

num1 = (math.pi)**num1
num2 = math.sqrt(num2)

if num1 > num2:
	print(num1)
else:
	print(num2)
