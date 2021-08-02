# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 10:30:14 2021

@author: mjwor
"""

class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
    
    def __iter__(self):
        node = self.top
        while node:
            yield node
            node.next 
    
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
    
    def treverseStack(self):
        if self.top  == None:
            print('There is nothing')
        else:
            node = self.top
            while node is not None:
                print(node.value)
                node = node.next
            

class Queue():
    def __init__(self):
        self.s = Stack()
        self.q = Stack()
    
    def add(self, newValue):
        newNode = Node(newValue)
        newNode.next = self.s.top
        self.s.top = newNode
        
    
    def s_to_q(self):
        node_s = self.s.top
        
        while node_s is not None:
            self.q.push(node_s)
            node_s = node_s.next
        
    def treverseQueue(self):
        
        node = self.s.top
        while node is not None:
            self.q.push(node.value)
            node = node.next
        
        node_2 = self.q.top

        while node_2 is not None:
            print(node_2.value)
            node_2 = node_2.next
        
        
    


print("S")
s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.treverseStack()

print("")

print('Q')

q1 = Queue()
q1.add(1)
q1.add(2)
q1.add(3)
print(q1.treverseQueue())

