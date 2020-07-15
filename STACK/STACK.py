class stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        if (len(self.stack))==0:
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]



