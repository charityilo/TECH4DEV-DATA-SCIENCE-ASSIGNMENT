#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a program to produce the following output using for loop
#+----+
#\ /
#/ \
#\ /
#/ \
#\ /
#/ \
#+----+


# In[2]:


#As a function Method 1
def diagram():
    print("+----+")
    for i in range(4):
        print("\\ /")
        print("/ \\")
     
    print("+----+")
    return
    
#testing the program

diagram()


# In[3]:


# method 2 

# Top portion
print("+----+")

# Middle area 
for i in range(4):
    print("\\ /")
    print("/ \\")

# Bottom portion
print("+----+")

                


# In[ ]:


#Write a program to produce the following output using for loop
#**********
#**********
#**********
#**********
#**********


# In[4]:


# method
for i in range(5):
    for j in range(10):
        print("*", end="")
    
    print() 


# In[ ]:


#Complete the code for the following for loop:
#for in range(1,7):
#//your code here
#so that it prints the following numbers, one per line:


# In[5]:


for a in range(1,7):
    print(a)
 
print()
for b in range (1,7):
    print(b * 2)
    
print()
for c in range(1, 7):
    print(4 + 15 * (c - 1))
    
print()
for d in range(1, 7):
    print(40 - 10 * d)
    
print()
for e in range(1, 7):
    print(-7 + (e-1) * 4)

print()
for f in range(1, 7):
    print(97 - 3 * (f-1))
    
print()
for g in range(1, 7):
    print(-4 + (g -1) * 18)

    


# In[ ]:


#Write a program to produce the following output using for loops. Then use a class constant to make it possible to change the 
#number of lines in the figure.
#1
#22
#333
#4444
#55555
#666666
#7777777


# In[6]:


class numberlines:
    lines =7    # constant
    
    def number_pyramid(pyramid):
        for i in range(1,pyramid.lines + 1):
            print(str(i) * i)
        return
    
#trying out the program

PYRAMID = numberlines()
PYRAMID.number_pyramid()


# In[ ]:


#Write a method named pay that accepts two parameters: a real number for a TA's salary, and an integer for the number of hours 
#the TA worked this week. The method should return how much money to pay the TA. For example, the call pay(5.50, 6)
#should return 33.0. The TA should receive "overtime" pay of 1 ½ normal salary for any hours above 8. For example, the call 
#pay(4.00, 11) should return (4.00 * 8) + (6.00 * 3) or 50.0. 


# In[7]:


#name of method

def pay(salary_rate, hours_worked):
    
#body of method

    normal_hours = 8
    overtime_rate = 1.5

    if hours_worked <= normal_hours:
        total_pay = salary_rate * hours_worked
    else:
        normal_pay = salary_rate * normal_hours
        overtime_pay = salary_rate * overtime_rate * (hours_worked - normal_hours)
        total_pay = normal_pay + overtime_pay

    return total_pay

# trying the program

pay(5.50, 6)

pay(4.00, 11)


# In[ ]:


# Write a similar method named area that takes as a parameter the radius of a circle and that returns the area of the circle.
# Recall that area can be computed as π times the radius squared and that Python has a constant called math.pi


# In[8]:


import math  #This brings in the maths module to enable the mth.pi (a constant for pi) to be activated

# this is the function proper
def area_of_circle(radius):
    return math.pi * radius**2

# trying the program
area_of_circle(2.0)


# In[ ]:


# Modify the code to use a input to prompt the user for the values of low and high. Below is a sample execution in which the 
#user asks for the same values as in the original program (1 through 1000):
#low? 1
#high? 1001
#sum = 500500


# In[9]:


low = int(input("low? "))
high = int(input("high? "))
sum  = 0

for j in range(low, high):
    sum += j

print("sum =", sum)


# In[ ]:


# Write a program using while loop that prompts the user for numbers until the user types 0, then outputs their sum.


# In[10]:


sum_of_num = 0
user_num = float(input("Enter a number (note that typing 0 ends the sequence)"))

while user_num != 0:
    sum_of_num += user_num
    user_num = float(input("Enter another number (note that typing 0 ends the sequence)"))
    
    print("sum of entered values is", sum_of_num)


# In[ ]:


# Write a program using while loop that prompts the user for numbers until the user types -1, then outputs their sum.


# In[11]:


sum_of_num = 0
user_num = float(input("Enter a number (note that typing -1 ends the sequence)"))

while user_num != -1:
    sum_of_num += user_num
    user_num = float(input("Enter another number (note that typing -1 ends the sequence)"))
    
    print("sum of entered values is", sum_of_num)


# In[ ]:


#Write a method named repl that accepts a String and a number of repetitions as parameters and returns the String concatenated 
#that many times. For example, the call repl("hello", 3) returns "hellohellohello". If the number of repetitions is 0 or less, 
#an empty string is returned.


# In[13]:


def repl(string, num_repl):
    if num_repl <= 0:
        return " "
    else:
        return string * num_repl
    
#trying out the program

repl("he",2)
        


# In[ ]:


#Write a method called printRange that accepts two integers as arguments and prints the sequence of numbers between the two 
#arguments, separated by spaces. Print an increasing sequence if the first argument is smaller than the second; otherwise, print
#a decreasing sequence. If the two numbers are the same, that number should be printed by itself. Here are some sample calls to 
#printRange: 
#printRange(2, 7)
#printRange(19, 11)
#printRange(5, 5)


# In[14]:


def printRange(num1,num2):
  
# for increasing sequence when num1 is less than num2
    if num1 < num2:
        for a in range(num1,num2+1):
            print(a, end="")
            
# for decreasing sequence when num1 is larger than num2

    elif num1 > num2:
        for a in range(num1, num2 -1,-1):
            print(a, sep= " ", end="")
            
# for single number output when num1 = num 2
    
    else: num1 = num2
    print (num1)
    
    
 # trying out the program

printRange(2,7)
printRange(19,11)
printRange(5,5)  


# In[ ]:


#Write a method named smallestLargest that asks the user to enter numbers, then prints the smallest and largest of all the numbers typed in by the 
#user. You may assume the user enters a valid number greater than 0 for the number of numbers to read. Here is an example dialogue: 
#How many numbers do you want to enter? 4
#Number 1: 5
#Number 2: 11
#Number 3: -2
#Number 4: 3
#Smallest = -2
#Largest = 11


# In[15]:


def smallestLargest():
    count = int(input("How many numbers do you want to enter? "))

    if count > 0:
        num_list = []
        for i in range(1, count + 1):
            num = float(input(f"Number {i}: "))
            num_list.append(num)

        smallest = min(num_list)
        largest = max(num_list)

        print(f"Smallest = {smallest}")
        print(f"Largest = {largest}")
    else:
        print("Please enter a valid number greater than 0 for the count.")

# trying the code
smallestLargest()


# In[ ]:


#Write a method called printAverage that uses a sentinel loop to repeatedly prompt the user for numbers. Once the user types any number 
#less than zero, the method should display the average of all nonnegative numbers typed. Display the average as a double. 
#Here is a sample dialogue with the user:
#Type a number: 7
#Type a number: 4
#Type a number: 16
#Type a number: –4
#Average was 9.0
#If the first number that the user types is negative, do not print an average:Type a number: –2


# In[16]:


def printAverage():
    sum = 0
    count = 0

    while True:
        num = float(input("Type a number: note that a negative number breakes the sequence"))
        
        if num < 0:
            break  # Break the loop if a negative number is entered
        
        sum += num
        count += 1

    if count > 0:
        average = sum / count
        print("Average was", average)
    else:
        print("No nonnegative numbers were entered.")

# trying the code
printAverage()


# In[ ]:


#Write a method named numUnique that takes three integers as parameters and returns the number of unique integers among the 
#three. For example, the call numUnique(18, 3, 4) should return 3 because the parameters have three different values.By 
#the call numUnique(6, 7, 6)should return 2 because there are only two unique numbers among the three parameters: 6 and 7.


# In[18]:


def numUnique(num1, num2, num3):
    unique_numbers = len(set([num1, num2, num3]))
    return unique_numbers

#trying out the code

result1 = numUnique(18, 3, 4)
print(result1)  

result2 = numUnique(6, 7, 6)
print(result2)  


# In[ ]:


#A Random object generates pseudo-random numbers. Find out how to use the Random class and write a program that simulates 
#rolling of two 6-sided dice until their combined result comes up as 7. One possible output can be seen as below:
#2 + 4 = 6
#3 + 5 = 8
#5 + 6 = 11
#1 + 1 = 2
#4 + 3 = 7
#You won after 5 tries!


# In[19]:


import random

def rolls_stimulator():
    random_generator = random.Random()
    total_rolls = 0

    while True:
        die1 = random_generator.randint(1, 6)
        die2 = random_generator.randint(1, 6)
        total = die1 + die2

        print(die1, "+", die2, "=", total)

        total_rolls += 1

        if total == 7:
            break

    print("You won after" ,total_rolls, "tries!")

# trying out the code
rolls_stimulator()


# In[ ]:




