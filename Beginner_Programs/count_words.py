# Program to count the number of words in a string.
# The program splits the string by spaces and counts how many words are present.
# Example: 'Hello world' has 2 words.
sen="Program to count the number of words in a string"

count=0
for i in sen:
    if i.isspace():
        count+=1
print("number of words: ", count)


#write programm for multiple spaces in sentense