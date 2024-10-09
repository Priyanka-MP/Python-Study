#n = 45

def func(n):
    if n>90 and n<=100:
        print("A")
    elif n>80 and n<=90:
        print("B")
    elif n>70 and n<=80:
        print("C")
    elif n>=0 and n<=70:
        print("D")
    else:
        print("invalid")
n = int(input())
func(n)                        