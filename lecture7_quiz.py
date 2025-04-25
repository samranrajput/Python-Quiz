######## Lecture 7 Tasks ########

# Q1 : Using both a nested for loop and a simple for loop, print this output.
"""
* * * * * 
* * * * * 
* * * * *
* * * * *
* * * * *
"""
# simple for loop Ans:
for row in range(1, 6):
    print("* " * 5)

# nested for loop Ans:
for row in range(1, 6):
    for col in range(1, 6):
        print("*", end = " ")
    print()

""" Q2:
* * * * * 
* * * * 
* * *
* *
*
"""
# simple for loop Ans:
for row in range(5, 0, -1):
    print("* " * row)

# nested for loop Ans:
for row in range(5, 0, -1):
    for col in range(row):
        print("*", end = " ")
    print()

""" Q3:
* 
* * 
* * *
* * * *
* * * * *
"""
# simple for loop Ans:
for row in range(1, 6):
    print("* " * row)

# nested for loop Ans:
for row in range(1, 6):
    for col in range(row):
        print("*", end = " ")
    print()

""" Q4:
* * * * * 
  * * * * 
    * * *
      * *
        *
"""
# simple for loop Ans:
for row in range(5, 0, -1):
    spaces = "  " * (5 - row)
    stars = "* " * row
    print(spaces + stars)


# nested for loop Ans:
for row in range(5, 0, -1):
    for space in range(5 - row):
        print(" ", end = " ")
    for stars in range(row):
        print("*", end=" ")
    print()

""" Q5:
        * 
      * * 
    * * *
  * * * *
* * * * *
"""
# simple for loop Ans:
for row in range(1, 6):
    spaces = "  " * (5 - row)
    stars = "* " * row
    print(spaces + stars)


# nested for loop Ans:
for row in range(1,6):
    for space in range(5 - row):
        print(" ", end = " ")
    for stars in range(row):
        print("*", end=" ")
    print()

""" Q6:
     * 
    * * 
   * * *
  * * * *
 * * * * *
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
"""
# simple for loop Ans:
for row in range(1,6):
    print(" " * (6 - row) + "* " * row)
for row in range(6, 0, -1):
    print(" " * (6 - row) + "* " * row)

# nested for loop Ans:
for row in range(1,6):
    for space in range(6 - row):
        print(" ", end = "")
    for stars in range(row):
        print("* ", end = "")
    print()
for row in range(6, 0, -1):
    for space in range(6 - row):
        print(" ", end = "")
    for stars in range(row):
        print("* ", end = "")
    print()

""" Q:7
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
"""
# simple for loop Ans:
for i in range(10):
    if i <= 4:
        stars = "* " * (5 - i)
        spaces = "  " * (2 * i)
        print(stars + spaces + stars)
    else:
        stars = "* " * (i - 4)
        spaces = "  " * (2 * (10 - i - 1))
        print(stars + spaces + stars)

# nested for loop Ans:
for i in range(10):
    for j in range(10):
        if i <= 4:
            if j <= 4 - i or j >= 5 + i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            if j <= i - 5 or j >= 14 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()


""" Q8:
1 
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
"""
# nested for loop Ans:
for row in range(1,6):
    for col in range(1, row+1):
        print(col, end=" ")
    print()

""" Q9:
1     1
1     2
1     3

2     1
2     2
2     3

3     1
3     2
3     3

4     1
4     2
4     3

5     1
5     2
5     3
"""
# nested for loop Ans:
for row in range(1,6):
    for col in range(1,4):
        print(row, "   ", col)
    print()