"""
pgm for count the number of alphabets and digits in the string
"""
s = input()
 
count_alpha = 0
count_digit = 0

for char in s:
    if char.isalpha(): count_alpha+=1
    if char.isdigit() : count_digit +=1

print(count_alpha)
print(count_digit)