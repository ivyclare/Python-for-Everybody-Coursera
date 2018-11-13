# Program to extract the numbers from a bunch of text
#and calculate their sum
import re
name = input("Enter file name:")
if len(name) < 1 : name = "test.txt"
handle = open(name)

total = 0
for line in handle:
    num_extract = re.findall('[0-9]+',line)
    #Checking if list is not empty
    if num_extract:
        for num in num_extract:
            total += int(num)
print(total)
