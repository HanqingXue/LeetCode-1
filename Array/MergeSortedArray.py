# longUsed = represents how many items are used in the longArray
 
#nums1 is the longer one, m = length of nums1, n = legnth of nums2
def merge(nums1, m, nums2, n):
    if n == 0:
        return
    
    i = m + n - 1
    a = m - 1
    b = n - 1
    
    while i > 0 and a > 0 and b > 0:
        if nums1[a] > nums2[b]:
            nums1[i] = nums1[a]
            a -= 1
        else:
            nums1[i] = nums2[b]
            b -= 1
        i -= 1

    if b >= 0:
        nums1[:b + 1] = nums2[:b + 1]
        
        
A = [0, "BLAH"]
B = [1]
print(A)
merge(A, 0, B, 1)

print(A)
