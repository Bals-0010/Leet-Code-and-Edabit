"""
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
    

    Example 1:

    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
    
"""

class Min_Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        return self.stack
        
    def pop(self):
        if len(self.stack)!=0:
            self.stack.remove(self.stack[-1])
            return self.stack
        else:
            return "Stack is Empty"
        
    def top(self):
        return self.stack[0]
        
    def getMin(self):
        return min(self.stack)

    
ms = Min_Stack()
ms.push(-2)
ms.push(2)
ms.push(-4)
ms.push(5)
ms.push(0)
ms.pop()
ms.getMin()
ms.top()