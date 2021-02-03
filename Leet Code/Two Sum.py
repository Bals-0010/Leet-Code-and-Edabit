"""[summary]
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Example 1:
        ---------
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1].
        
        Example 2:
        ---------
        Input: nums = [3,2,4], target = 6
        Output: [1,2]
        
        Example 3:
        ---------
        Input: nums = [3,3], target = 6
        Output: [0,1]
        

        Constraints:

        2 <= nums.length <= 105
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        Only one valid answer exists.
"""

def Two_Sum(arr, target):
    # Accepts list/array and target as arguments
    target = 0
    target_list = []
        
    if len(arr)==0 or type(arr)!=list:
        print("List is empty or not a list")
    else:
        for i in range(len(arr)):
            for j in range(1,len(arr)):
                if (arr[i]+arr[j]==target):
                    target_list.extend([i,j])
    return target_list

# print(Two_Sum([2,7,11,15],9))