"""
#1 Does casing matter?
#2 Do digits count?
#3 Is an empty string a valid palindrome?
"""
class Solution(object):
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower() #1 remember to change cases
        alpha_s = u"".join([letter for letter in s if letter.isalpha() or letter.isdigit()]) #2
        if alpha_s == alpha_s[::-1]:
        	return True
        else:
        	return False
