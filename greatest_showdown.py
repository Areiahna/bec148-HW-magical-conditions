# The Greatest Showdown

#Task 1: Identify the Greatest Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.

# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The largest number is 4.".

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Last one, I promise!: "))


if (num1 > num2 and num3):
    print("The largest number is", num1)
elif (num2 > num1 and num3):
    print("The largest number is", num2)
elif (num3 > num1 and num2):
    print("The largest number is", num3)
else:
    print("Duplicate numbers??")



        
