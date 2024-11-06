def print_diamond(n):
    for i in range(1, n+1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" *(2 * i - 1))
n = 5
print_diamond(n)    
"""
Explanation:
The top part of the diamond:

The outer loop runs from 1 to n, where n is the number of rows for the top part.
" " * (n - i) adds spaces to center the stars.
"*" * (2 * i - 1) prints the odd number of stars in each row (1, 3, 5, etc.).
The bottom part of the diamond:

The outer loop runs in reverse from n-1 to 1 to print the bottom half.
The same logic applies for centering the stars and printing them in a decreasing order.
"""