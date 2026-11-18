#stack using linked list
class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node  
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp=self.top
            popped_data= temp.data
            self.top=self.top.next
            temp=None
            return popped_data
    def reverse(self):
        temp=self.top
        while temp:
            st1.push(Node(temp.data))
            temp=temp.next

    def print(self):
        temp=self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp=temp.next

#Linear Queue

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        
    
    def dequeue(self):
        if self.rear==None:
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data
    
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    def reverse_stack(s1):
        q1 = myQueue()
        while not s1.isempty(): # pop from stack and enqueue to queue
          q1.enqueue(Node(s1.pop()))
        q1.print()
# Create a queue
myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end="")
myQueue.printQueue()
print("Dequeue: ", myQueue.dequeue())
print("Dequeue: ", myQueue.dequeue())
print("Dequeue: ", myQueue.dequeue())
print("Dequeue: ", myQueue.dequeue())
st=stack()
st1=stack()
st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(78))
st.push(Node(90))
st.print()
st.pop()
st.print()
st.reverse()
st1.print()