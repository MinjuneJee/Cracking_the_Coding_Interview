# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:17:06 2021

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
    def size(self):
        node = self.top
        count = 0
        
        while node is not None:
            node = node.next
            count += 1
        return count
    
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
    
    def removeNth(self, n):
        if n > self.size():
            print("Sorry n is greater than the size of this stack")
        elif n == 1:
            self.top = self.top.next
        else:
            node = self.top
            n = n-1
            for i in range(n-1):
                node = node.next
            
            try:
                node.next = node.next.next
            except:
                pass

    def insertNth(self, value, location):
        
        
        if location == 1:            
            self.push(value)
        else:
            node = self.top    
            newNode = Node(value)  
            
            count = 1
            while count != location-1:
                node = node.next
                count += 1
            nextNode = node.next
            node.next = newNode
            newNode.next = nextNode
    
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
        
    def peek(self):
        return self.top
    
                    
                        
    def treverseStack(self):
        if self.top  == None:
            print('There is nothing')
        else:
            node = self.top
            while node is not None:
                print(node.value)
                node = node.next
    

def sort(target_stack):
    temp_stack = Stack()

    top_value = target_stack.peek().value
    temp_stack.push(top_value)
    target_stack.removeNth(1)
    
    for i in range(8):
        count = 1
        top_value = target_stack.peek().value
        
        node_temp = temp_stack.top 
        while node_temp is not None:
            if top_value > node_temp.value:
                node_temp = node_temp.next
                count += 1
            else:
                break
        print("count",count)
        temp_stack.insertNth(top_value, count)
        target_stack.removeNth(1)
            
    print('temp_stack')

    temp_stack.treverseStack()
    print('target_stack')
    target_stack.treverseStack()
            
        


    


print("S")
s1 = Stack()
s1.push(2)
s1.push(3)
s1.push(1)
s1.push(8)
s1.push(7)
s1.push(6)
s1.push(5)
s1.push(4)
print("_____________")
s1.insertNth(200,2)

s1.treverseStack()

print("_____________")
s1.size()
#s1.removeNth(7)

s1.treverseStack()
print(sort(s1))








