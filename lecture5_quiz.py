######## Lecture 5 Tasks ########
# Suppose:
# a is 50 and b is 10
a = 50
b = 10

# 1. : Print "Hello World" if a is greater than b.
# Ans:
if a > b:
    print("Hello World")

# 2. : Print "Hello World" if a is not equal to b.
# Ans:
if a != b:
    print("Hello World")

# 3. : Print "Yes" if a is equal to b, otherwise print "No".
# Ans:
if a == b:
    print("Yes")
else:
    print("No")

# Q1 : Print "1" if a is equal to b, print "2" if a is greater than b, print “3” if b is greater than a
# Ans:
if a == b:
    print("1")
elif a > b:
    print("2")
elif b > a:
    print("3")

# Q2 : Print appropriate message if x is greater, lessor or equal to y. Take y as 100 and x as a user input.
# Ans:
x = int(input("Enter a number : "))
y = 100
if x > y:
    print(x, "is greater than", y)
elif x < y:
    print(x, "is less than", y)
else:
    print(x, "is equal to", y)

# Q3 : Write a Python program to find those numbers which are divisible by 7. prompt user to input and display suitable answers.
# Ans:
num = int(input("Enter a number : "))
for i in range(1, num + 1):
    if i % 7 == 0:
        print(i, "is divisible by", 7)

# Q4 : Write a program to prompt user to input a number and checks weather its even or odd.
# Ans:
num = int(input("Enter a number : "))
if num % 2 == 0:
    print(num, "is even number")
else:
    print(num, "is odd number")

# Q5 : Write a program that checks the temperature and prints. "Cold" if temperature < 15. "Moderate" if temperature is between 15 and 30. "Hot" if temperature > 30
# Ans:
temp = int(input("Enter a temperature : "))
if temp <= 15:
    print("Cold")
elif temp >= 15 and temp <= 30:
    print("Moderate") 
else:
    print("Hot")       
  
# Q6 : Ask the user to enter a year. Check if it’s a leap year. (A leap year is divisible by 4, but if divisible by 100, it must also be divisible by 400.)    
# Ans:
year = int(input("Please enter a year: "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a Leap Year!")
        else:
            print(f"{year} is NOT a Leap Year.")
    else:
        print(f"{year} is a Leap Year!")
else:
    print(f"{year} is NOT a Leap Year.")
    
# Q7 : Ask the user to enter a password. If the password is "admin123", print "Access granted", otherwise print "Access denied".
p_word = input("Enter a Password : ")
if p_word == "admin123":
    print("Access granted")
else:
    print("Access denied")
    
# Q8 : Take a number from the user and check if it is divisible by 3 and 5.
num = int(input("Enter a number : "))    
if num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by", 3, "and", 5)
else:    
    print(num, "is not divisible by", 3, "and", 5)