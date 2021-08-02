# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:08:55 2021

@author: mjwor
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else: 
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"
    
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None

    
                    
singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(3, 1)

singlyLinkedList.insertSLL(0, 0)

singlyLinkedList.insertSLL(4, 1)

    

singlyLinkedList.traverseSLL()
print(singlyLinkedList.searchSLL(3))

print([node.value for node in singlyLinkedList])

"""2.1 Remove Dups"""


def removeDupl(cla):
    current = cla.head
    previous = None
    record = set()
    
    while current:
        if current.value in record:
            previous.next = current.next
        else:
            record.add(current.value)
            previous = current
        current = current.next
    cla.tail = previous
    
    return [node.value for node in cla]

print(removeDupl(singlyLinkedList))


"""2.2 Return kth to Last"""

def kthLast(cla, k):
    current = cla.head
    tempNode = current
    
    while k != 0:
        current = current.next
        tempNode.next = current.next
        
        tempNode.value = current.value
        print("Testing")
        print(current.value)
        k -=1
    
    


    return [node.value for node in cla]

singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(6, 1)
singlyLinkedList.insertSLL(5, 1)

singlyLinkedList.insertSLL(0, 0)

singlyLinkedList.insertSLL(4, 1)

print([node.value for node in singlyLinkedList])
print(kthLast(singlyLinkedList, 5))


"""Delete Middle Node"""

def deleteMiddle(cla):
    count = 0
    middle = 0
    for node in cla:
        count += 1
    
    middle = count//2
    
    current = cla.head
    previous = current
    
    count = 0
    
    while count != middle + 1:
        if count == middle:
            
            previous.next = current.next
        elif count == middle-1:
            previous = current
            current = current.next
        else:
            current = current.next
            
        count += 1
    
    return [node.value for node in cla]

print(deleteMiddle(singlyLinkedList))

"""2.4 Partition"""

def partition(cla, x):
    current = cla.tail = cla.head
    
    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            current.next = cla.head
            cla.head = current
        else:
            cla.tail.next = current
            cla.tail = current
        
        current = nextNode
    
    if cla.tail.next is not None:
        cla.tail.next = None

        
    return [node.value for node in cla]
    

print(partition(singlyLinkedList, 4))

print(singlyLinkedList)
    
"""2.5 Sum Lists"""



singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])

def makeNumber(cla,x,y,z):
    cla.insertSLL(z, 0)
    cla.insertSLL(y, 0)
    cla.insertSLL(x, 0)
    
    num = 0
    
    i = 100
    for node in cla:
        num += node.value*i
        i = 10
    
        
    return num

def sumLists(cla,x,y,z,x1,y1,z1):
    left = makeNumber(cla, x, y, z)
    right = makeNumber(cla, x1, y1, z1)
        
    return left + right

print("SumeList")

print(sumLists(singlyLinkedList, 2, 3, 8, 8,6,2))


"""2.6 Palindrome"""

def palindrome(cla):
    
    
    current = cla.head
    last = cla.tail
    l = 0
    while current:
        
        nextNode = current.next
        current = nextNode
        l += 1
    print("length",l)
    i = 0
    j = 0
    k = 0
    w = 0

    
    last = cla.tail

    while cla.head != cla.tail:
        
        i = j
        k = 0
        current = cla.head
        while i > 0:
            current = current.next
            i -= 1
        A = current.value
        A_add = current
        current = current.next       
        Z = current.value

        while k < l-2:            
            print(k)
            current = current.next              
            k += 1
        Z = current.value
        Z_add = current
        l -= 2
        if A == Z:
            print("A=",A,"Z=",Z)
            j += 1
        elif A_add == Z_add:
            break
        elif A_add.next == Z_add:
            break
        else:
            return False
        
    return True
    

singlyLinkedList.deleteEntireSLL()

print(sumLists(singlyLinkedList, 2, 3, 8, 8,3,2))
print([node.value for node in singlyLinkedList])

singlyLinkedList.deleteEntireSLL()

print(sumLists(singlyLinkedList, 2, 3, 8, 8,3,2))
print(singlyLinkedList.insertSLL(5,3))

print([node.value for node in singlyLinkedList])
print(palindrome(singlyLinkedList))

        

"""2.7 Intersection """
import random

def Intersection(n):
    
    cla = SLinkedList()
    cla_2 = SLinkedList()
    
    
    for i in range(n):
        cla.insertSLL(random.randrange(1,10), 0)
        cla_2.insertSLL(random.randrange(1,10), 0)
    
    print("print cla",[node.value for node in cla])
    
    for node in cla:
        for node_2 in cla_2:
            if node == node_2:
                print(node_2)
                print("Yes there is a intersection")
                return True
    return False

print(Intersection(1000))


"""Loop Detection """

def loopDetection(n):

    cla = SLinkedList()
    
    for node in range(n):
        cla.insertSLL(random.randrange(1,10), 0)
    
    print([node.value for node in cla])

    i = 0
    z = 0
    val_col = []

    for node in cla:
        i += 1
        j = 0
        for node_2 in cla:
            j += 1
            if j <= i:
                pass
            elif node.value == node_2.value:
                if node.value in val_col:
                    break
                else:
                    val_col.append(node.value)
                    
                    print(node.value)
             
                
print(loopDetection(10))
                
    
    
    
















            

