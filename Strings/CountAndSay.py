"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string. 
"""

def countAndSay(n):
    """
    count = 1
    say_str = ""
    for idx in range(len(n)):
        try:
            if n[idx] == n[idx + 1]:
                count += 1
            else: 
                say_str = str(count) + n[idx]
        except IndexError:
            pass
        #print(say_str)
    return say_str
    """
    set_str = set(n)
    print(set_str)
    output = ""
    for element in set_str:
        output = str(n.count(element)) + str(element) + output

    return output
print(countAndSay("11111112"))
        
