# Pgm to display n terms of natural nos and their sum
N =int(input("Enter data: "))
print("Enter the natural numbers")

for i in range(1,N +1):
    print(i)
    
sum = 0
for i in range(1, N+1):
    sum += i
print("sum of natural numbers from 1 to ", N, "is ",sum)    

