######## Lecture 4 Tasks ########

# Q1 : Multiply 10 with 5, and print the result.
# Ans:
print(10*5)

# Q2 : Write output of print(11//2)
# Ans:
print(11//2)

# Q3 : Write output of print(2 ** 5)
# Ans:
print(2 ** 5)

# Q4 : Write a program to swap two numbers in python.
# Ans:
x = 2
y = 6
y, x = x, y
print(x, y)

# Q5 : Write the output on following program and have your comment on it.
# Ans:
a = 7
b = 4
x = a % b
# print(x)

# Q6 : Convert the following code using arithmetic assignment operator.
# Ans:
X=5
Y=9
X+=Y
print(X) 

# Q7 : Write the output of print(6 & 3)
# Ans:
print(6 & 3)

# Q8 : write the output of print(6 | 3)
# Ans:
print(6 | 3)

# Q9 : Write the output of print(6 ^ 3)
# Ans:
print(6 ^ 3)

# Q10 : Write a program to ask the speed of a car in miles per hour and convert that in kilometers per hour and display.
# Ans:
mph = float(input("Enter the speed of the car in miles per hour: "))
kmph = mph * 1.60934
print("The speed in kilometers per hour is:", kmph)

# Q11 : Write a program that asks the user to enter two integers. Have the program output the two integers and the result when the first number entered is raised to the power of the second number entered.
# Ans:
num1 = int(input("Enter a first number : ")) 
num2 = int(input("Enter a second number : "))
result = num1 ** num2
print("First number:", num1)
print("Second number:", num2)
print("Result (first number raised to the power of second):", result)

# Q12 : Write a program that asks the user to enter two integers. Have the program output how many times the second number can be divided into the first number. For example if the first number entered was 23 and the second number entered was 4 the program should report 5 times (i.e. the fractional bit is ignored). You are required to implement this program using the floor operator.
# Ans:
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
result = num1 // num2
print("The second number can be divided into the first number", result, "times.")
