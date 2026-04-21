# Stack and Queue implementation in Python
# Stack follows Last In First Out (LIFO) principle
#Stack implementation using list
# Stack operations: push, pop, peek, isEmpty

Stack = []
Stack.append(1)
Stack.append(2)
Stack.append("Sathish")
print(Stack)
print(Stack.pop())
print(Stack)
print(Stack[-1]) #peek
print(len(Stack) == 0) #isEmpty

#stack implementation using class
class Stack:
    def __init__(self):
        self.stack =[]
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if(len(self.stack)==0):
            return "Stack is empty"
        else:
            return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def isEmpty(self):
        return(len(self.stack)==0)
    
s = Stack()
s.push(1)
s.push("Sathish")
print(s.stack)

#Queue follows First In First Out (FIFO) principle
#Queue implementation using list
# Queue operations: enqueue, dequeue, peek, isEmpty

Queue =[]
Queue.append(1)
Queue.append(2)
Queue.append("Sathish")
print(Queue)
print(Queue.pop(0)) #dequeue
print(Queue)
print(Queue[0]) #peek
print(len(Queue) == 0) #isEmpty

#Queue implementation using class
class Queue:
    def __init__(self):
        self.queue =[]
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if(len(self.queue)==0):
            return "Queue is empty"
        else:
            return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def isEmpty(self):
        return(len(self.queue)==0)
    
q = Queue()
q.enqueue(1)
q.enqueue("Sathish")
print(q.queue)

print(q.dequeue())
print(q.queue)
print(q.peek())
print(q.isEmpty())

