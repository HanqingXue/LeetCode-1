"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
    Did you consider the case where path = "/../"?
    In this case, you should return "/".
    Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".
    "///"
    "/..."
"""

"""Create a stack, pass all the non ".." paths. Append all words, if .. you go back"""
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
    	#print(path.split("/")) #Split somehow creates random empty strings
        path =  filter(None, path.split("/")) #removes empty strings in list
        stack = []
        for char in path:
        	# "." mean current dir, so DO NOTHING
        	if char == ".":
        		continue
        	#Pop because like "cd .."
        	elif char == "..":
        		if stack != []:
        			stack.pop()
        	#Append FOLDER NAME
        	else:
        		stack.append(char)
        path_str = ""
        #print(stack)
        if stack == [] or ("" in stack):
        	return "/"
      	for i in range(len(stack)):
        	path_str += "/" + stack[i]
       	return path_str

print(Solution().simplifyPath("///"))

"""
    def simplifyPath(self, path):
    	if list(path).count("/") % 2 != 0:
    		return path
    	#print(path.split("/")) #Split somehow creates random empty strings
        path =  filter(None, path.split("/")) #removes empty strings in list
        #print(path)
        stack = []
        for char in path:
        	if char.isalpha():
        		stack.append(char)
        path_str = ""
        if stack == []:
        	return "/"
      	for i in range(len(stack)):
        	path_str += "/" + stack[i]
       	return path_str
"""


