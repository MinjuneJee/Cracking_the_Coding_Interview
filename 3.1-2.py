# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 13:19:19 2021

@author: mjwor
"""

"""3.1 Three in One"""

"""Put the three stacks as element of array just like hash Tables"""

"""
pop(): Remove the top item from the stack.
push( item) : Add an item to the top of the stack.
peek ( ): Return the top of the stack.
is£mpty() : Return true if and only if the stack is empty

"""

"""3.2 Stack Min"""


class Node():
    
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack():
    
    def __init__(self):
        self.top = None
    
    def __iter__(self):
        node = self.top
        while node:
            yield node
            node = node.next
    
    def length(self, count = 0):
        node = self.top
        count = 0
        while node != None:
            yield node
            node = node.next
            count += 1
        print(count)
        return count
    
    def pop(self):
        node = self.top
        node.next = self.top
    
    def push(self, nodeValue):
        newNode = Node(nodeValue)
        newNode.next = self.top
        self.top = newNode
        
        
    def peek(self):
        return self.top
    
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    
    def traverseStack(self):
        if self.top is None:
            print("The Stack is empty")
        else:
            node = self.top
            while node is not None:
                print(node.value)
                node = node.next

testStack = Stack()
testStack.push(1)
testStack.push(1)
testStack.push(1)
print("pringint Length",testStack.length())

print('tranverseStack')
print(testStack.traverseStack())


        
        
    
        
        
        
    