# Program to count the number of digits in a number.
# The program counts how many digits the number has.
# Example: 12345 has 5 digits.
str= input("enter the string to calculate digit:  ")
count=0
for i in str:
    if i.isdigit():
        count+=1
print(count)