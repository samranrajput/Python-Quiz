######## Lecture 5 Tasks ########
# Suppose:
# a is 50 and b is 10
a = 50
b = 10

# Q1 : Print "Hello World" if a is greater than b.
# Ans:
if a > b:
    print("Hello World")

# Q2 : Print "Hello World" if a is not equal to b.
# Ans:
if a != b:
    print("Hello World")

# Q3 : Print "Yes" if a is equal to b, otherwise print "No".
# Ans:
if a == b:
    print("Yes")
else:
    print("No")

# Q4 : Print "1" if a is equal to b, print "2" if a is greater than b, print “3” if b is greater than a
# Ans:
if a == b:
    print("1")
elif a > b:
    print("2")
elif b > a:
    print("3")


# Q5 : Print appropriate message if x is greater, lessor or equal to y. Take y as 100 and x as a user input.
# Ans:
x = int(input("Enter a number : "))
y = 100
if x > y:
    print(x, "is greater than", y)
elif x < y:
    print(x, "is less than", y)
else:
    print(x, "is equal to", y)

# Q6 : Write a Python program to find those numbers which are divisible by 7. prompt user to input and display suitable answers.
# Ans:
num = int(input("Enter a number : "))
for i in range(1, num + 1):
    if i % 7 == 0:
        print(i, "is divisible by", 7)

# Q7 :
# Ans:
num = int(input("Enter a number : "))
if num % 2 == 0:
    print(num, "is even number")
else:
    print(num, "is odd number")