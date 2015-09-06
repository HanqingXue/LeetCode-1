def isPalindrome(s):
    return s == s[::-1]
    
def isRotatedPalindrome(s):
    # split each char string into left + right and check the combination
    # of right + left to see if it's a palindrome
    for i in range(len(s)):
        left = s[0:i]
        right = s[i:]
        #now use our palindrome checker to check for right + left
        if isPalindrome(right + left):
            return True
    return False
    
    
value = "1234321"
print(isRotatedPalindrome(value))

value2 = "112"
print(isRotatedPalindrome(value2))


