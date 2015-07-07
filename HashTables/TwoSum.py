"""
Given an array of ints, find two numbers that add up to target number.

The function should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 
"""
import collections

# @param {integer[]} nums
# @param {integer} target
# @return {integer[]}
def twoSum(nums, target):
    """
    num_dict = collections.OrderedDict()
    output = []
    for n in nums:
        try:
            print(num_dict[n])
        except KeyError:
            num_dict[n] = target-n
    #print(sorted(num_dict.items()))
    for key, value in num_dict.items():
        if key in nums and value in nums and value != key: #[3,2,4], 6
            output.append(nums.index(key)+1) 
            nums[output[0]-1] = "a"
            #print(nums)
            output.append(nums.index(value)+1)
            return output
     """
    processed = {}
    for i in range(0, len(nums)):
        if target-nums[i] in processed:
            print(processed)
            return [processed[target-nums[i]]+1,i+1]
        processed[nums[i]]=i
print(twoSum([3,2,4], 6))
        
