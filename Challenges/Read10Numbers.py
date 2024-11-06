# Task : Pgm to read 10 numbers from the keyboard and find their sum and average
# logic : append method , sum, length 
myList = []

print("Enter 10 numbers")

for i in range(10):
    userInput = int(input("Num " + str(i+1) + ":"))
    myList.append(userInput)
print("List: ", myList)

sum = 0
for i in myList:
    sum = sum + i
print("sum of the list is ",sum)

average = sum/len(myList)
print("Average is " ,average)