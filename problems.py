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
n = 1
a = int(input("Enter your no."))
while n <= 10:
    print(a, "x", n, "=", n * a)
    n += 1
