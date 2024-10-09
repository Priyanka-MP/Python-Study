# Challenge - print the following pattern
""" 
  * 1 row 1 star
  ** 2 row 2 star
  *** 3 row 3 star
  **** 4 row 4 star
  ***** 5 row 5 star
"""

for row in range(1,6):
    for star in range(0,row):
        print("*", end =" ")
    print()   