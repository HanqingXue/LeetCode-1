class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
    	s_list = s.split()
    	if s_list != []:
    		return len(s_list[len(s_list) - 1])
    	else:
    		return 0
        