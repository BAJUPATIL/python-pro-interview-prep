# Program to calculate the sum of the squares of the digits of a number.
# The sum is calculated by squaring each digit and adding them up.
# Example: The sum of squares of digits of 12 is 1² + 2² = 5.

num=  25
sum=0
for i in str(num):
    if i.isdigit():
        i=int(i)
        sum=sum+(i*i)
        
    else:
        print("please enter digit")
        
print("sum of squares: ", sum)