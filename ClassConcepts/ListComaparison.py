l1 = [4,5]
l2 = [4,5,6]
#returns true or false
print(l1<l2) 
print(l1>l2)
print(l1==l2)
"""
why list comparison?
String is a list of characters
ASCII comparison A =65 , a=97
str1 < str2 

String Comparison:
When you compare strings using < or >, Python compares them lexicographically (i.e., alphabetically).
Character by Character:
Python compares the strings character by character, starting from the left.
First Difference:
In this case, the first character of "1000" is '1', and the first character of "20" is '2'.
ASCII Values:
Since the ASCII value of '1' is less than the ASCII value of '2', Python considers "1000" to be less than "20".
"""
print("1000" < "2000")
str1 = "Priyanka"#P=80
str2 = "priya" #p=112

print(str1 < str2)

"""
List comprehension
l = [1,2,3,....100]

"""
l = [i for i in range(1,101)]
print(l)

l = [i**2 for i in range(1,101)]
print(l)
