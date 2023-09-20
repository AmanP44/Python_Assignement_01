#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1)"'Write a Python program to print the following string in a specific format (see the output). Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output '"
a = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
print(a)


# In[2]:


# 2)Write a Python program to get the Python version you are using

import sys
print(sys.version)


# In[3]:


# 3) Write a Python program to display the current date and time.

import datetime

print(datetime.datetime.today())


# In[4]:


# 4) Write a Python program which accepts the radius of a circle from the user and compute the area

r = int(input("Enter radius of circle"))

area = 3.14*r*r
print(area)


# In[5]:


# 5)Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first_name = str(input("Enter the first name "))
last_name = str(input("enter the last name "))

print(last_name[::-1], first_name[::-1])


# In[6]:


# 6)Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list with those numbers

num = input('Enter the number')
list = num.split(',')
print(list)


# In[7]:


# 7)Write a Python program to accept a filename from the user and print the extension of that

file_name = input('Enter the file name ')
a = file_name.split('.')
print(a)


# In[8]:


# 8)Write a Python program to display the first and last colors from the following list
color_list = ["yellow","Green","grey" ,"orange"]
print(color_list[0])
print(color_list[3])


# In[9]:


# 10)Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

X = int(input("Enter the number"))

n1 = int('%s' % X)
n2 = int('%s%s' %(X,X))
n3 = int('%s%s%s' %(X,X,X))
print(n1+n2+n3)


# In[10]:


# 10).Write a program to demonstrate different number data types in Python.

a = True
b = 34.5
c = 5
d = 'Data Science'

print('The data type of a is: ', type(a))
print('The data type of b is: ', type(b))
print('The data type of c is: ', type(c))
print('The data type of d is: ', type(d))


# In[11]:


# 11)Python Program to find sum of array
import numpy as np

def sumofarray(b):
    sum = 0
    for i in b:
        sum = sum + i
    return sum


# In[12]:


sumofarray(np.array([1,2,3]))


# In[13]:


# 12) Write a program to create, concatenate and print a string and accessing sub-string from a given string

s1 = input("Enter the first string ")
s2 = input("Enter the second string ")
print("Print the string s1 ", s1)
print('Print the string s2 ', s2)
print('Print the concatenate the string ', s1 + s2)
print('Print sub_string s1 is ', s1[1:3])
print('print sub_string s2 is ', s2[1:3])


# In[14]:


# 13) Create and explain the working of tuple.
tup = (1,2,35,6)
print(tup)
type(tup)


# In[15]:


# Tuple is immutable,in tuple we will not change the value.


# In[16]:


# 14) Write a python program to find largest of three numbers.

num1 = int(input('Enter the number 1 '))
num2 = int(input('Enter the number 2 '))
num3 = int(input('Enter the number 3 '))

if num1>=num2 and num1>=num3:
    print('The larget number is: ', num1)
elif num2>=num1 and num2>=num3:
    print('The larget number is: ', num2)
else:
    print('The largest number is: ', num3)


# In[17]:


# 15)Write a Python program to convert temperatures to and from Celsius, Fahrenheit. [ Formula: c = (f-32)(5/9)]

temp = float(input('Enter the temperature '))
unit = input('Enter the unit ')

if unit=='C' or unit =='c':
    newtemp= 9/5*(temp+32)
    print('Temperature in farenhite ', newtemp)
elif unit== 'F' or unit=='f':
    newtemp= 5/9*(temp-32)
    print('Temperature in celcius ', newtemp)
else:
    print('Unknown')


# In[18]:


# 16) Write a Python program to construct the following pattern, using a nested for loop

max = 6

for i in range(0, max+1):
    print('* ' *i)
for i in range(max+1, 0, -1):
    print('* '*i)


# In[19]:


# 17) Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides).

hypo = float(input('Enter the length of one side: '))
base = float(input('Enter the other first side: '))
height = float(input('Enter the the other second side: '))

if hypo**2==(base**2)+(height**2):
    print('The triangle is a right angle triangle')
else:
    print('The triangle is not a right angle triangle ')


# In[20]:


# 18) Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration print the sum of the current number and previous number

def sumofpreviousnum(num):
    previousnum=0
    
    if i in range(num):
        sum=previousnum+i
        print('The current number is: ', i, 'Previous number is ', previousnum, 'sum is ', sum)
        previousnum=i


# In[23]:


sumofpreviousnum(20)


# In[29]:


# 19) Print multiplication table of 12 using recursion

def table(n,i):
    print(n*i)
    i=i+1
    if i<=10:
        table(n,i)


# In[30]:


table(12,1)


# In[31]:


# 20) Write a function to calculate area and perimeter of a rectangle.

def area_of_rectangle(a,b):
    area= (a*b)
    print(area)
    perimeter=2*(a*b)
    print(perimeter)


# In[32]:


area_of_rectangle(5,4)


# In[34]:


# 20) Write a function to calculate power of a number raised to other

def power(a,b):
    power=a**b
    print(power)


# In[35]:


power(2,3)


# In[36]:


# 21) Write a function to tell user if he/she is able to vote or not.

def voterage(age):
    if age>=18:
        print("He/She is able to vote: ")
    else:
        print("He/She is not able to vote")


# In[37]:


voterage(20)


# In[38]:


voterage(17)


# In[41]:


# 22) Write a function to check if a number is even or not.

def evenodd():
    num=int(input('Enter the number'))
    if num%2==0:
        print('The number is even')
    else:
        print('The number is odd')


# In[42]:


evenodd()


# In[51]:


# 23) Write a function to check if a number is prime or not

def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
        return True


# In[55]:


it_prime(6)


# In[1]:


# 24)Given a list of numbers, return True if first and last number of a list is same

num = [10,20,30,40,50,60,10]

first_number = num[0]
last_number = num[-1]

if first_number==last_number:
    print('Number is same')
else:
    print('The number is not same')


# In[2]:


# 25) Write a program to check if each word in a string begins with a capital letter?

print("The america".istitle())
print("the america".istitle())


# In[4]:


# 26) Write a program to Check if a string contains a specific substring

a = 'The world fastest plane'

'plane' in a


# In[6]:


# 27) Capitalize the first character of a string

str = 'aman priyambad'
str.capitalize()


# In[8]:


# 28) Reverse the string “hello world”

str = 'Aman Priyambad'
print(str[::-1])


# In[10]:


# 29) Remove vowels from a strings

str1 = 'Hello World'
vowels = ('a','e','i','o','u')
'.join([c for c in string if c not in vowels])'


# In[12]:


# 30) Iterate through a string Using for Loop.

str2 = "priyambad"
h_letters = []

for i in str2:
    h_letters.append(i)
    
print(h_letters)


# In[17]:


# 31)Write a program to check whether a number is divisible by 7 or not.

num = int(input('Enter the number '))

if num%7==0:
    print('Number is divisible by 7 ')
else:
    print('Number is not divisible by 7 ')


# In[20]:


# 32) Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria
# First 100 units no charge Next 100 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs2000)

amt = 0

unit = int(input('Enter the number of unit '))

if unit<=100:
    amt=0
elif unit>=100 and unit<=200:
    amt=(unit-100)*5
elif unit>=200:
    amt=500+(unit-200)*10
print('The amount of electricity bill is: ', amt)


# In[22]:


# 33) Write a program to display the last digit of a number. (hint : any number % 10 will return the last digit)

num1 = float(input('Enter the number: '))
print('The last digit number is: ',num1%10)


# In[25]:


# 34) Write a program to check whether an years is leap year or not.

yr = int(input('Enter the number: '))
if yr%100==0:
    if yr%400==0:
        print('Leap year')
    else:
        print('Not leap year')
else:
    if yr%4==0:
        print('Leap year ')
    else:
        print('Not leap year ')


# In[27]:


# 35) Write a Python program to calculate a dog's age in dog's years. Go to the editor Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years. Expected Output:

h_age = int(input("Input a dog's age in human years: "))

if h_age < 0:
    print("Age must be positive number.")
    exit()
elif h_age <= 2:
    d_age = h_age * 10.5
else:
    d_age = 21 + (h_age - 2)*4
    


# In[ ]:




