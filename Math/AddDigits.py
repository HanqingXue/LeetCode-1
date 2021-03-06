"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime? 
"""

class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        while num > 9:
            x = 0
            for i in range(len(str(num))):
                x += int(str(num)[i])
            num = x
        return num
        
        
# Solution 2
"""
Digital root
https://en.wikipedia.org/wiki/Digital_root
"""
import math
class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        if num == 0:
            return 0
        return int(num-9*math.floor((num-1)/9))
