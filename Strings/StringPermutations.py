def permute(nums):
    result = []
    
    permutation(nums, 0, result)
    return result
 
def permutation(nums, begin, result):
    if begin == len(nums):
        print(nums)
        return
    else:
        for i in range(begin, len(nums)):
            nums[begin], nums[i] = nums[i], nums[begin]
            permutation(nums, begin + 1, result)
            nums[begin], nums[i] = nums[i], nums[begin]
            #print(nums)
#output = []
print(permute([1,2,3]))
#print(output)
