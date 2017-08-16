print("Number Multiply and Divsion")
print("This program asks for three numbers, adds the first two together")
print("then divides the total by the third number before displaying the answer")
print()
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
num3 = int(input("Please enter a third number: "))
print()
ans = (num1 + num2) / num3
print("The total of ({0}+{1})/{2} is {3}." .format(num1,num2,num3,ans)) #new style
print("The total of (%2d+%2d)/%2d is %.2f." %(num1,num2,num3,ans) ) #old style
print("The total of ({a:d}+{num2:d})/{num3:d} is {ans:.3f}." .format(a=num1, num2=num2,num3=num3,ans=ans) ) #old style
firstName = "aizul"
lastName = "faideen"
age = 36
print(firstName + " " + lastName + " .Age is " + str(age))
print(firstName + " " + lastName + " .Age is %.2f" %age)
print(firstName + " " + lastName + " .Age is {0:.3f}" .format(age))