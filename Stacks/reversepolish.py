class Solution(object):
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        eval_str = u""
        for item in tokens:
            if item.isalpha():
                continue            
            else:
                if item.strip(u"-").isdigit(): #need to use strip cuz python thinks -ve ain't digits loma
                    stack.append(item)
                    #print(stack)
                elif item in u"+-*/":
                    eval_str = u""
                    eval_str += stack.pop()
                    eval_str = stack.pop() + item + eval_str
                    #print(eval_str)
                    stack.append(unicode(eval(eval_str)))
        if eval_str:
            return(int(round(eval(eval_str))))
        else:
            return int(u" ".join(stack))