"""
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct. 
Time O(n) Space O(n)
"""

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        num_counter = {} # create counter hashtable
        for n in nums: # build dictionary
            try:
                num_counter[n] += 1
                return True # will create a duplicate if you need to += 1 so return True!
            except KeyError:
                num_counter[n] = 1
        return False # else (outside for loop and didn't hit the repeat) return False as in no repeats
