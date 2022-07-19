#
# Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.

input_string=input("Enter the hyphen separated sequence of words: ")

list_of_words=input_string.split("-")

list_of_words.sort()

print('-'.join(list_of_words))


    

