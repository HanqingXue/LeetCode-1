def binarySearch(A, target):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = int(low + (high - low) /2)
        if A[mid] == target:
            if mid != 0 and A[mid - 1] == target:
                high = mid -1
            else:
                return mid
        elif A[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    
print(binarySearch([1,1,2,3,3,3,3,4], 3))
