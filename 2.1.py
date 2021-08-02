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
    
        
        


















            

