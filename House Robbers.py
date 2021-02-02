"""
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, 
    the only constraint stopping you from robbing each of them is that adjacent houses have security system connected 
    and it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given a list of non-negative integers representing the amount of money of each house, 
    determine the maximum amount of money you can rob tonight without alerting the police.

    Example 1:

    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                Total amount you can rob = 1 + 3 = 4.
    Example 2:

    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
                Total amount you can rob = 2 + 9 + 1 = 12.
    

    Constraints:

    0 <= nums.length <= 100
    0 <= nums[i] <= 400
"""

class Rob():
    def __init__(self, array):
        self.array = array
        self.odd_counter = []
        self.even_counter = []
        
    def calculate(self):
        for i in range(len(self.array)):
            if len(self.array)<=100 and self.array[i]<=400: 
                if i%2==1:
                    self.odd_counter.append(self.array[i])
                else:
                    self.even_counter.append(self.array[i])
            else:
                print("""                      
                      Must be in Constraints:
                        0 <= nums.length <= 100
                        0 <= nums[i] <= 400
                      """)                
                break
    
        return max(sum(self.odd_counter), sum(self.even_counter))