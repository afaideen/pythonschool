def main():
    message1= input("Enter your first message ")
    message2= input("Enter your second message ")
    print("Your first message was {0} ".format(message1))
    print("Your second message was {0} ".format(message2))

# Exercise 2 Basics
# Write a program to input two whole numbers,
# add them together and print the result to the screen.

def ex2():
    number1= int(input("Enter your first number "))
    number2= int(input("Enter your second number "))
    sumOfNumbers = number1 + number2
    print("{0} + {1} = {2}".format(number1,number2,sumOfNumbers))



main()
ex2()