# Program to calculate the sum of digits of a number.
# The sum is calculated by adding all the individual digits of a number.
# Example: For 123, the sum is 1 + 2 + 3 = 6.

number= 4542
sum=0
for i in str(number):
    if i.isdigit():
        sum+=int(i)
        
print("sum of number:", sum)