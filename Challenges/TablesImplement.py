A = int(input("Enter the number:"))
#string concatenation or f format can be used for printing
print("Multiplication Table = " + str(A))

for i in range(1,11):
     print(str(i) + " * " + str(A) + " = " + str(i * A))
      
"""
f factor method:
# Get user input
A = int(input("Enter a number to generate its multiplication table: "))

# Generate the multiplication table
print(f"Multiplication Table for {A}")
for i in range(1, 11):
    print(f"{i} * {A} = {i * A}")
"""

 
      
     