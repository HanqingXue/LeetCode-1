"""
Important that the list is sorted
given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

def summaryRanges(nums):
    length = len(nums)
    summary_list = []
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] == nums[j] - 1:
                print(nums[i], nums[j])
            print(nums[j])

print(summaryRanges([0, 1, 2, 4, 5 ]))
