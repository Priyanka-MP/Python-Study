#Write a pgm to display the cube of the number upto an integer
N = int(input("Enter the number: "))
print("Cube of the number")
for i in range(1, N+1):  
    print("The number is: ", i , "and the cube of ", i , "is" , i *i *i)
