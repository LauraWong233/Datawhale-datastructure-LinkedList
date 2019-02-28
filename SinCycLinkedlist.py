#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 23:55:18 2019

@author: laura
"""

class Node(object):
	def __init__(self, item):
		super(Node, self).__init__()
		self.data = item
		self.next = None
class SinCycLinkedlist(object):
	def __init__(self):
		super(SinCycLinkedlist, self).__init__()
		self.head = None
	def initlist(self,item):
		self.head = Node(item[0])
		cur = self.head
		for i in item[1:]:
			cur.next = Node(i)
			cur = cur.next
		cur.next = self.head
	def is_empty(self):
		if self.head == None:
			print('list is empty')
			return True
		else:
			print('list is not empty')
			return False
	def length(self):
		len = 0
		cur = self.head
		while cur.next!=self.head:
			len += 1
			cur = cur.next
		print('链表长度为 %d' %len)
		return len
	def travel(self):
		cur = self.head
		while cur.next!=self.head:
			print(cur.data,end=' ')
			cur = cur.next
		print()
	def add(self,item):########################遇到了一个什么奇怪的鬼问题
		node = Node(item)
		cur = self.head
		if self.head == None:
			self.head = node
			node.next = self.head
		else:
			node.next = self.head
			while cur.next!= self.head:
				cur = cur.next
			cur.next = node
			self.head = node

	def append(self,item):
		node = Node(item)
		cur = self.head
		if self.head == None:
			self.head = node
			node.next = self.head
		else:
			while cur.next != self.head:
				cur = cur.next
			node.next = self.head
			cur.next = node
	def insert(self,pos,item):
		node = Node(item)
		cur = self.head
		i=0
		if pos<=0:
			self.add(node)
		elif pos>=self.length():
			self.append(node)
		else:
			while i<pos-1:
				i+=1
				cur = cur.next
			node.next = cur.next
			cur.next = node
	def delete(self,item):
		if self.is_empty():
			return
		else:
			cur = self.head
			while cur.next != self.head:
				if cur.data != item:
					pre = cur
					cur = cur.next

				else:
					if cur != self.head:
						pre.next = cur.next
						break
					else:
						temp = self.head
						while temp.next != self.head:
							temp = temp.next
						self.head = cur.next
						temp.next = self.head
						break
	def search(self,item):
		i = 0;
		cur = self.head
		if self.is_empty():
			print('链表为空')
			return False
		else:
			while cur.next != self.head:
				if cur.data == item:
					print('位置为 %d' %(i+1))
					return(i+1)
				else:
					i+=1
					cur = cur.next
			print('不在')
			return False



if __name__ == '__main__':
    test = SinCycLinkedlist()
    test.is_empty()
    test.initlist([1,2,3])
    test.append(4)
    test.add(0)
    test.travel()
    test.insert(3,100)
    test.travel()
    test.length()
    test.delete(3)
    test.travel()
    test.search(4)



		
		