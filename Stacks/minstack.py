"""
 Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack. O(1)
    Space O(n)
"""
class MinStack:
    def __init__(self):
        self.data = []
        self.min = []
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.data.append(x)
        if self.min == []: #if there is nothing in min_stack
            self.min.append(x)
        else: #if there is something in min_stack
            if x <= self.min[-1]: #if there is something in self.data
                self.min.append(x) #push x if x <= top of min_stack (takes care of duplicates too)

    # @return nothing
    def pop(self):
        if self.min: #if there is something in min stack
            if self.data[-1] == self.min[-1]: #pop min if top of min stack == top of stack
                self.min.pop() 
        self.data.pop()

    # @return an integer
    def top(self):
        if self.data:
            return self.data[-1]
        else:
            return None

    # @return an integer
    def getMin(self):
        if self.min:
            return self.min[-1]
        else:
            return None

s = MinStack()
s.push(-3)
s.getMin()
"""
print(s.push(2))
print(s.push(0))
print(s.push(3))
print(s.push(0))
s.getMin()
print(s.pop())
s.getMin()
print(s.pop())
s.getMin()
print(s.pop())
s.getMin()
"""