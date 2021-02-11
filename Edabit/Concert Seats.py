"""
Create a function that determines whether each seat can "see" the front-stage. 
A number can "see" the front-stage if it is strictly greater than the number before it.
Everyone can see the front-stage in the example below:

# FRONT STAGE
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]]

# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.
Not everyone can see the front-stage in the example below:

# FRONT STAGE
[[1, 2, 3, 2, 1, 1], 
[2, 4, 4, 3, 2, 2], 
[5, 5, 5, 10, 4, 4], 
[6, 6, 7, 6, 5, 5]]

# The 10 is directly in front of the 6 and blocking its view.
The function should return True if every number can see the front-stage, 
and False if even a single number cannot.

Examples
can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ True

can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) ➞ True

can_see_stage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
]) ➞ False

can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) ➞ False

# Number must be strictly smaller than 
# the number directly behind it.

Notes:
Numbers must be strictly greater than the number in front of it.
All numbers within the lists will be whole numbers greater than or equal to zero.
"""

def can_see_stage(listt):
    column_length = len(listt[0])
    import numpy as np
    aa = np.array(listt)
    for i in range(column_length):
      if (aa[:,i] == sorted(aa[:,i])).all():
        continue
      else:
        temp = aa[:,i]==sorted(aa[:,i])  
        #temp is to maintain a boolean array of mismatched items/columns blocking other way
        # print(temp)
        # print(aa[:,i], sorted(aa[:,i]),"\n")
        where_block = np.where(temp==0)[0][0]
        # print(where_block)
        print("{} is blocking the way of {}".format(aa[:,i][where_block], aa[:,i][where_block+1]))
        return False
    return True
    
print(can_see_stage([[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]]))