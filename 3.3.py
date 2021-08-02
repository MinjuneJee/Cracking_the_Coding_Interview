# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 13:19:19 2021

@author: mjwor
"""


"""3.3 Stack Min"""


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
    
    def count(self):
        current_top = self.top
        count = 0
        while(current_top is not None):
            if current_top.value:
                count += 1
            current_top = current_top.next
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

"""
class MyQueue():
    def __init__(self):
        que = Stack()
        que.first = None
        que.last = None
        S2 = Stack()
        

    def add(self,item):
        newNode = Node(item)
        if que.last = None:
            que.first = newNode
        else:        
            while que.first:
                que.first.next
            newNode.next = que.last
            que.last = newNode
    
    def remove(self):

"""        
        
    
    
        


"""3.3 Stack of Plates"""


class SetOfStacks():
    
    def __init__(self):
        self.listStack = []
        self.listStack.append(Stack())
        self.i = 0
        
#        for i in range(len(self.listStack)):
#            self.listStack[i] = Stack()
    
        self.current = self.listStack[0]
        
    def rotation(self):
        if self.current.count() >= 9:
            self.i += 1
            self.listStack.append(Stack())
            self.current = self.listStack[self.i]
    
    def push_Set(self, value):
        self.rotation()
        self.current.push(value)
    
    def pop_Set(self):
        self.current.top = self.current.top.next
    
    def popAt_Set(self, loc):
        currentNode = self.current.top
        j = 0
        for i in range(loc):
            nextNode = currentNode.next
            tempNode = currentNode.next.next
            currentNode = nextNode
            j +=1
            
        if j > 0:
            currentNode.next = tempNode.next
        
      
    def testing(self):    
        self.rotation()
        for i in range(25):
            self.push_Set(i)
            self.rotation()
#        self.pop_Set()

        for i in range(len(self.listStack)):
            if i == 0:
                print(str(i+1)+'st in list')
                print(self.listStack[i].traverseStack())
            elif i == 1:
                print(str(i+1)+'nd in list')
                print(self.listStack[i].traverseStack())
            
            elif i == 2:
                print(str(i+1)+'rd in list')
                print(self.listStack[i].traverseStack())
            else:
                print(str(i+1)+'th in list')
                print(self.listStack[i].traverseStack())
    

print("Testing SetOfStacks")
print(SetOfStacks().testing())



    
    

    
    


        
        
    
        
        
        
    