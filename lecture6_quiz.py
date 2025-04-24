######## Lecture 6 Tasks ########

# Q1 : Write a program to display the first 10 natural numbers
# Ans:
for i in range(1, 11):
    print(i)

# Q2 : Print the sequence 3,4,5,6,7,8,9,10,11,12,13
# Ans:
for i in range(3, 14):
    print(i)

# Q3 : Print the sum of first 5 natural numbers
# Ans:
total = 0
for i in range(1, 6):
    total += i
print(total)

# Q4 : Write a program that prints the table of 2 from 1 to 10.
# Ans:
for i in range(1, 11):
    print(f"{2} * {i} = {2 * i}")

# Q5 : Write a program that takes a number and the range (limit) of its table from the user using a comma, and then prints the table of that number up to the given range.
# Ans:
no, rang = input("Enter a table name and table range : ").split(",")
no = int(no)
rang = int(rang)
for i in range(1, rang+1):
    print(f"{no} * {i} = {i * no}")

# Q6 : Write a program that prints odd numbers from 1 to 60, but if the number is 59, print only the number; for all other numbers, print the message: 'loop is less than 60' along with the number.
# Ans:
for i in range(1,61, 2):
    if i == 59:
        print(i)
    else:
        print(f"loop is lass than 60 {i}")

# Q7 : Write a program that uses a while loop to print odd numbers from 1 to 60. If the number is 59, print only the number; for all other numbers, print the message: 'loop is less than 60' along with the number.
# Ans:
i = 1
while i < 60:
    if i == 59:
        print(i)
    else:
        print(f"loop is lass than 60 {i}")
    i += 2

# Q8 : Write a program that uses a while loop to print numbers from 1 to 5, but stops the loop using the break statement as soon as the number 4 is encountered.
# Ans:
i = 1
while i < 6:
    if i == 4:
        break
    else:
        print(i)
        i += 1

# Q9 :Write a program that prints a diamond shape. This shape should have an upper half (from 1 to 5) and a lower half (from 5 to 1) with stars (*). The arrangement of spaces and stars on each line should be such that the shape looks like a diamond. The program should first print the upper half, then print the lower half. In the upper half, the number of stars increases, while in the lower half, they decrease. The example shape will look something like this:
#         * 
#        * * 
#       * * * 
#      * * * * 
#     * * * * * 
#    * * * * * * 
#     * * * * * 
#      * * * * 
#       * * * 
#        * * 
#         *
# Ans:
for i in range(1, 6):
        print(" " * (6 - i) + "* " * i)
for i in range(6, 0, -1):
        print(" " * (6 - i) + "* " * i)