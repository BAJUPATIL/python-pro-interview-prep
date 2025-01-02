# Program to check if a number is prime.
# A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
# Example: 7 is prime, but 8 is not.

input = int(input("Enter a number: "))
count=0
for i in range(2,input):
    if input%i== 0:
        count+=1
        
if count==0:
    print("Number is prime")
    
else:
    print("number is not prime")