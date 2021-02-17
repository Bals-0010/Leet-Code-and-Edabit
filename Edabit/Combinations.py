"""
Create a function that takes a variable number of arguments, 
each argument representing the number of items in a group, 
and returns the number of permutations (combinations) of items that you could get by taking one item from each group.

Examples:
combinations(2, 3) ➞ 6
combinations(3, 7, 4) ➞ 84
combinations(2, 3, 4, 5) ➞ 120

Notes:
Don't overthink this one.
Input may include the number zero.
"""

def combinations(*items):
    if items == ():
        print("No Arguments Inserted")
    elif 0 in items:
        print(0)
    else:
        temp = 1
        for i in items:
            temp = temp * i
        print(temp)

combinations(0,1,2)