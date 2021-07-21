#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
            
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(head, data):
    NewNode=DoublyLinkedListNode(data)
    # Write your code here
    #for empty list
    if head==None:
        return NewNode
    #for head insertion
    elif head.data>data:
        NewNode.next=head
        head.prev=NewNode
        head=NewNode
    #for insertion in between and end
    Curr=head
    while Curr.data<=data and Curr.next:
        Curr=Curr.next
    if Curr.next==None and Curr.data<data:
        Curr.next=NewNode
        NewNode.prev=Curr
        NewNode.next=None
    else:
        Curr=Curr.prev
        NEXT=Curr.next
        Curr.next=NewNode
        NewNode.prev=Curr
        NewNode.next=NEXT
        NEXT.prev=NewNode
    return head
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
