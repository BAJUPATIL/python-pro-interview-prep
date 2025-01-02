# Program to check if a number or string is a palindrome.
# A palindrome reads the same backward as forward.
# Example: 'madam' is a palindrome, but 'hello' is not.

name= input("enter name to check palindrome ")

print(name)
Lname=list(name)

if Lname==Lname[::-1]:
    print("String is Palindrome")
else:
    print("string is not palindrome")