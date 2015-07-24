"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the". 
"""

def reverseWords(s):
    s = s.strip()
    #s = list(s)
    s = s.split(" ")
    print(s)
    
    
    #reverse whole word
    i = 0
    j = len(s) - 1
    while i != j and i < j:
        #print(i, j)
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    print(s)
    
    for word in s:
        word = word[::-1]
        print(word)
    print(s)
    
    #for i in range(len(s)):
        
    
    return "".join(s)

print(reverseWords("the sky  is blue"))
