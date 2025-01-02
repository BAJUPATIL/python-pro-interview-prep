# Program to count the number of vowels in a string.
# The program counts how many vowels (a, e, i, o, u) are present in the string.
# Example: 'hello' has 2 vowels.
sentense=input("Enter the sentense: ")

vowels=['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']

count=0

for i in sentense:
    if i in vowels:
        count+=1
print("Number of vowels are: ", count)