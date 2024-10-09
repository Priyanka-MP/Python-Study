#join() -> operates on a string and a list together
l = ["I", "am", "from", "Kerala"]
print("|".join(l)) #separator.join(list)-any delimiter |

# isupper() | islower >>check string is upper,lower case
print("PRIYANKA&".isupper())  #can have any symbols and checks for upper case and returns true or false
print("priyanka%123".islower())

#isalpha() >> check only for english alphabets
print("Priyanka Murugan".isalpha())
#isdigit() check if string contains only digit
print("12345".isdigit())
#isalnum()checks if string is alphanumeric
print("Priyanka Murugan 2703".isalnum())
#startwith(<substring>) >>checks if string is starting with substring
print("Priyanka K".startswith("Priyanka"))
print("Priyanka K".endswith("K"))
