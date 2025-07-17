# write a program to count words ,lines, and characters in a user provided sentence
# Author: Edwin K Johnson
# Rollno: 16
sentence = input("Enter a sentence: ")
words = sentence.split(     )
num_words = len(words)
num_lines = sentence.count('\n') + 1 
num_characters = len(sentence)
print("Number of words: ",num_words)
print("Number of lines: ",num_lines)
print("Number of characters: ",num_characters)
