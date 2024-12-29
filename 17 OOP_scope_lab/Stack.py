from logging import exception


class Stack:
    #defines scope as a list with a dictionary
    def __init__(self):
        self.scope=[{}]

    #adds value to scope
    def push(self,value):
        self.scope.append(value)

    #returns last item placed in stack unless empty
    def top(self):
        if not self.scope:
            raise Exception("Stack is empty")
        return self.scope[-1]

    #returns the item in respect to the index
    def __getitem__(self,index):
        if index>len(self.scope) or index<0:
            raise exception("index out of range")
        return self.scope[index]

    #returns the length of the scope
    def __len__(self):
        return len(self.scope)

    #used for loops returns the list reversed
    def __iter__(self):
        return reversed(self.scope)

    #removes last item in scope unless there is only one scope left
    def pop(self):
        if len(self.scope)>1:
            self.scope.remove(self.scope[-1])
        else:
            print("Cannot leave global scope")





