# write a prog. to display a person name ,age,address in three different lines
"""name = "john"
age = 56
address = "98 lake view"
print(name)
print(age)
print(address)"""

# write a prog. to swap two variables
# method1
"""x = 12
y = 13
temp = x
print(temp)
x = y
print(y)
print("value of x is", x)
print("value of y is", y)"""

# method2
"""a = 45
b = 34
# left,right = right,left is a method
a, b = b, a
print(a)
print(b)"""

# write a program to convert a float into integer
"""a = 78.9
b = int(a)
print(type(b))"""

# write a program to take details from a student for id card and then print it in different lines.
"""name = input("enter name")
Grade = input("enter grade")
age = int(input("enter age"))
email = input("Enter valid email")
ph_no = input("enter No.")
print(name)
print(Grade)
print(age)
print(email)
print(ph_no)"""

# write a prog to take an user input as integer then convert it to float
"""a = int(input("enterA NO."))
print(float(a))"""

# write a program to check if a no. is positive
"""num = int(input("Enter your No. here"))
if num > 0:
    print("num is positive")
else:
    print("num is negative")"""

# write a no. to check whether a no. is odd or even.
"""num = int(input("enter your no."))
if num % 2 == 0:
    print("your no. is even")
else:
    print("your no. is odd")"""

# write a prog. to create area calculator
"""print(press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get the area of triangle)"""

"""choice = int(input("Enter a no. between 1-4:"))

if choice == 1:
    side = float(input("Enter the side of square"))
    area = side ** 2
    print("the area of sq. is : ", area)

elif choice == 2:
    length = float(input("Enter the Length of rectangle"))
    width = float(input("Enter the width of rectangle"))
    area = length * width
    print("the area of rectangle is :", area)

elif choice == 3:
    radius = float(input("Enter radius of the circle"))
    area = ((22 / 7) * (radius ** 2))
    print("the area of circle is:", area)
elif choice == 4:
    base = float(input("Enter the base if triangle"))
    height = float(input("Enter the height of traingle"))
    area = 0.5 * base * height
    print("Enter the area of triangle is:", area)
else:
    print("invalid input")"""

# write a prog.to check the passed letter is a vowel or not
"""letter = input("Enter your letter here")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("it is a vowel")
else:
    print("it is not a vowel")"""

# write a prog. to check if a no. is a single digit no.,2-digit no. and so on ... up to 5 digit
"""num = int(input("Enter a no. upto 5 digit"))
if num >= 0 and num <= 9:
    print("it is a single digit no.")
elif num >= 10 and num <= 99:
    print("it is a double digit no.")
elif num >= 100 and num <= 999:
    print("it is a triple digit no.")
elif num >= 1000 and num <= 9999:
    print("it is a four digit no.")
else:
    print("it is a five digit no.")"""

# write a table  with for loop
"""n = int(input("Enter your no."))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)"""

# with while loop
"""n = 1
a = int(input("Enter your no."))
while n <= 10:
    print(a, "x", n, "=", n * a)
    n += 1"""
# 7/2/25
# write a prog. to find the sum of all the even no. upto 50
"""sum = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum += i
print("The sum of first 50 no. is", sum)"""

# write a prog. to write first 20 no. and their sq no.
"""for i in range(1, 21):
    print(i, i ** 2)"""

# write a prog. to find sum of first 10 odd no. using while loop.
"""sum = 0
n = 0
while n <= 20:
    if n % 2 != 0:
        sum += n
    n += 1
print("The sum of first 10 odd no. is ", sum)"""

# write a prog. to check if a no. is divisible by  8 and 12 upto 100 no.
"""for i in range(1, 101):
    if i % 8 == 0 and i % 12 == 0:
        print(i)"""

# write a prog. to create a billing system at supermarket
# using while True
"""while True:
    name = input("Enter Customer's name:")
    total = 0

    while True:
        print("Enter the amount and quantity")
        amount = float(input("Enter amount:"))
        quantity = float(input("Enter the quantity:"))
        total += amount * quantity
        repeat = input("do you want to add more items? (yes/no):")
        if repeat == "no" or repeat == "No":
            break
    print("-" * 40)
    print("Name:", name)
    print("Amount to be paid:", total)
    print("-" * 40)
    print("**********Happy shopping**********")

    repeat1 = input("do want to go to next customer? (yes/no):")
    if repeat1 == "no" or repeat == "No":
        break"""

# a= "why fit in , when you are born to stand out!"
# write a program to find out length og a string
"""a = "why fit in, when you are born to stand out!"
 print(len(a))"""

# write a program to check how many times alphabet o is occurring.
"""a = "why fit in, when you are born to stand out!"
print(a.count("o"))"""

# write a prog to convert the whole string into lower and upper cases.
"""a = "why fit in, when you are born to stand out!"
print(a.upper())
print(a.lower())"""

# write a prog to convert the following string into a title.
"""a = "why fit in, when you are born to stand out!"
print(a.title())"""

# write a prog to find the index no. of "fit in" .
"""a = "why fit in, when you are born to stand out!"
print(a.find("fit in"))"""

# write a prog to display the pattern (1,22,333,4444,55555) / (*,**,***,****,*****) / 1,12,123,1234,12345)
"""for i in range(1, 6):  # rows
    for j in range(1, i + 1):  # columns
        print(i, end=" ")
    print()"""
# -------------------------------------(*,**,***,****,*****)------------------------------------------------
"""for i in range(1, 6):  # rows
    for j in range(1, i + 1):  # columns
        print("*", end=" ")
    print()"""
# -----------------------------(1,12,123,1234,12345)------------------------------------------------------------
"""for i in range(1, 6):  # rows
    for j in range(1, i + 1):  # columns
        print(j, end=" ")
    print()"""

# ---------------------------(11111,2222.333,44,5)--------------------------------------------------------------
"""for i in range(1, 6):  # rows
    for j in range(6, i, -1):  # columns
        print(i, end=" ")
    print()"""

# -------------------------------------------------------------------------------------------------------------
"""for i in range(1, 6):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()"""

# -------------------------(1,21,321,4321,54321)----------------------------------------------------------
"""for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()"""

# ----------------------------(*,**,***,****,*****,****,***,**,*)-----------------------------------------
"""for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for i in range(5, 0, -1):
    for k in range(0, i - 1):
        print("*", end=" ")
    print() """

# --------(1,2/4,3/6/9,4/8/12/16,5/10/15/20/25,6/12/18/24/30/36, 7/14/21/28/35/42/49)--------------------------
"""for i in range(1, 11):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()"""

# Write a prog. to get Fibonacci series up to 10 no.
"""a = 0
b = 1
n = int(input("Enter your number:"))
if n == 1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)"""

# write a prog to check the no. is prime or not
"""num = int(input("Enter your no. :"))

if num <= 1:
    print("it is not a prime no.")
else:
    for i in range(2, num):
        if num % i == 0:
            print("number is not prime")
            break
    else:
        print("it is prime no.")"""

# write a prog to check no. is palindrome
num = int(input("Enter a no. here"))
temp = num
rev = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if rev == temp:
    print("it is palindrome")

else:
    print("it is not a palindrome")
