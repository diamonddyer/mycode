#!/usr/bin/env python3

import random 



wordbank= ["indentation", "spaces"] 
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

##Append integer to wordbank
wordbank.append(4)

##Input asking for num 

num = int(input("Enter a number between 0 and 20: "))

student_name = tlgstudents[num]

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

random_name= random.choice(tlgstudents)
print(f"{random_name}")

