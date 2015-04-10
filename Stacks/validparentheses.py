"""
Can't pop empty stack
What happens when you get "}" straight away?
Reject if the length is not even
"""

class Solution:
    # @return a boolean
    def isValid(self, s):
    	bracket_dict = {"(":")", "{":"}","[": "]"}
    	if len(s)%2 != 0:
    		return False
    	stack = []
        for char in s:
        	if char in bracket_dict.keys():
        		stack.append(char)
        	elif char in bracket_dict.values():
        		"""You can't pop an empty stack"""
        		try:
        			if bracket_dict[stack[-1]] == char: #Checks if character on top of stack is closing of bracket
        				stack.pop() 
        		except IndexError: #If the stack is empty before adding in all the brackets then it's false
        			return False
        	#print(stack)
        return stack == []
q = Solution
print(Solution().isValid("(()()())*()*))*)(*)*()"))