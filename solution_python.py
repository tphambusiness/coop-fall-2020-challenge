class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.currentPoint = 0 # keep track of current point in history relative to undos/redos
        self.history = [] # keep track of operations

    def add(self, num: int):
        self.value += num

        if (self.currentPoint != len(self.history)):
            # there has been an undo and/or redo command
            # so this operation overrides the index of the current point
            # assumed the entire history onwards before and from current point is preserved
            self.history[self.currentPoint] = num
        else:
            self.history.append(num)

        self.currentPoint = len(self.history)

    def subtract(self, num: int):
        self.value -= num

        if (self.currentPoint != len(self.history)):
            # there has been an undo and/or redo command
            # so this operation overrides the index of the current point
            # assumed the entire history onwards before and from current point is preserved
            self.history[self.currentPoint] = num * -1
        else:
            self.history.append(num * -1) # negated value is added to a list 

        self.currentPoint = len(self.history)

    def undo(self):
        if (self.currentPoint > 0): 
            self.value -= self.history[self.currentPoint-1] # take away the last operation done 
            self.currentPoint -= 1
        

    def redo(self):
        if (self.currentPoint < len(self.history)): 
            self.value += self.history[self.currentPoint-1]
            self.currentPoint += 1
        

    def bulk_undo(self, steps: int):
        for i in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        for i in range(steps):
            self.redo()

e = EventSourcer()
e.add(5)
e.add(5)
e.add(5)
e.undo()
e.undo()
e.add(1)
for i in e.history:
    print(i)
e.redo()
print(str(e.value) + " end value")