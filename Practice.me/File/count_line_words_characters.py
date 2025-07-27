# WAP to read a python file abc.txt and count number of line, word, character in file
Lines = 0
Char = 0
word = 0

with open("abc.txt","r") as f1:
    for line in f1:
        Lines++;