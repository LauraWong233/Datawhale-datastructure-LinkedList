#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 23:06:04 2019

@author: laura
"""
##位置从0开始
class Node(object):
	#创建节点
	def __init__(self, item):
		super(Node, self).__init__()
		self.data = item
		self.next = None
		self.pre = None
class DoubleDirectionList(object):
	#头结点
	def __init__(self):
		super(DoubleDirectionList, self).__init__()
		self.head = None
	#初始化链表
	def initlist(self,item):
		self.head = Node(item[0])
		cur = self.head
		for i in item[1:]:
			node = Node(i)
			cur.next = node
			node.pre = cur
			cur = cur.next
	#是否是空
	def isempty(self):
		if self.head == None:
			print('list is empty')
			return True
		else:
			return False
	#长度
	def length(self):
		cur = self.head
		count = 0
		while cur != None:
			count+=1
			cur = cur.next
		print('链表的长度为%d'%count)
		return count
	#遍历并输出
	def travel(self):
		cur = self.head
		while cur!= None:
			print(cur.data,end=' ')
			cur = cur.next
		print()
	#在头部添加元素
	def add(self,item):
		node = Node(item)
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head.pre = node
			self.head = node 
	#在尾部添加元素
	def append(self,item):
		node = Node(item)
		cur = self.head
		if self.head == None:
			self.head = node
		else:
			while cur.next!=None:
				cur = cur.next
			cur.next = node
			node.pre = cur
	#在指定位置添加元素
	def insert(self,pos,item):
		node = Node(item)
		cur = self.head
		count = 0
		if pos<=0:
			self.add(item)
		elif pos>=self.length():
			self.append(item)
		else:
			while count<pos-1:
				count+=1
				cur = cur.next
			node.pre = cur
			node.next = cur.next
			cur.next.pre = node
			cur.next = node
	#删除某个节点
	def delete(self,item):
		cur = self.head
		pre = None
		while cur!=None:
			if cur.data != item:
				pre = cur
				cur = cur.next
			else:
				if cur == self.head:
					cur.next.pre = self.head
					self.head = cur.next
					break
				else:
					pre.next = cur.next
					cur.next.pre = pre
					break
	#查找某个元素
	def search(self,item):
		count = 0
		cur = self.head
		if self.isempty():
			print('链表为空')
			return False
		else:
			while cur != None:
				if cur.data == item:
					print('该元素存在于链表中，在第%d个位置'%(count))
					return True
				else:
					count += 1
					cur = cur.next
			print('该元素不在链表中')
			return False


if __name__=='__main__':
    test = DoubleDirectionList()
    test.isempty()
    test.initlist([1,2,3])
    test.travel()
    test.append(4)
    test.add(0)
    test.travel()
    test.length()
    test.delete(6)
    test.travel()
    test.delete(3)
    test.travel()
    test.insert(2,100)
    test.travel()
    test.search(100)
    




		