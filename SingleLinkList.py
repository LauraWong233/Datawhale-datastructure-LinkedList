#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:18:21 2019

@author: laura
"""

##位置从0开始
class Node(object):
	#首先定义节点
	def __init__(self,value):
		super(Node, self).__init__()
		self.data = value
		self.next = None
class SingleLinkList(object):
	#头节点，默认为空
	def __init__(self):
		super(SingleLinkList, self).__init__()
		self.head = None
    #创建初始链表
	def initlist(self,data):
		self.head=Node(data[0])
		cur = self.head
		for i in data[1:]:
			cur.next = Node(i)
			cur = cur.next
	#判断链表是否为空
	def isempty(self):
		if self.head == None:
			print('LinkList is empty')
			return True;
		else:
			return False;
	#计算链表长度
	def length(self):
		len = 0
		cur = self.head
		while cur != None:
			len+=1
			cur=cur.next
		return len
	#遍历链表并输出
	def travel(self):
		cur = self.head
		while cur!=None:
			print(cur.data,end=' ')
			cur=cur.next
		print()
	#在头部添加元素
	def add(self,item):
		#首先创建一个存储了item的节点
		node = Node(item)
		if self.head == None:
			self.head = node;
		else:
			#插入
			node.next = self.head
			self.head = node
	#在尾部添加元素
	def append(self,item):
		node = Node(item)
		if self.head==None:
			self.head=node
		else:
			cur = self.head
			while cur.next!= None:
				cur = cur.next
			cur.next = node
	#在指定位置添加元素
	def insert(self,pos,item):
		node = Node(item)
		cur=self.head
		if pos>=self.length():
			self.append(item)
		elif pos<=0:
			self.add(item)
		else:
			index=0
			while index<pos-1:
				index+=1
				cur=cur.next
			node.next = cur.next
			cur.next = node
	#删除某个节点
	#注意要保存pre节点
	def delete(self,item):
		if self.isempty():
			return 
		cur = self.head
		pre = None
		while cur!=None:
			if cur.data!=item:
				pre = cur
				cur = cur.next
			else:
				if cur==self.head:
					self.head == cur.next
					break
				else:
					pre.next = cur.next
					break
	#查找某个元素是否存在及其位置
	def search(self,item):
		if self.isempty():
			print('LinkList is empty!')
		else:
			count = 0
			cur = self.head
			while cur!=None:
				if cur.data == item:
					print('该元素存在于链表中，在第%d个位置'%(count))
					return True
				else:
					count+=1
					cur = cur.next
			print('该元素不存在于链表中')
			return False
	##查找链表的中间节点
	#搞两个指针，一个每次前进一步，一个每次前进两步，前进两步的到链表尾时前进一步的到了链表中间
	def findmid(self):
		cur1 = self.head
		cur2 = self.head
		while (cur1.next!=None) & (cur2.next.next!=None):
			cur1 = cur1.next
			cur2 = cur2.next.next
		print('中间节点为 %f' % cur1.data)
	#单链表反转#在这里用的就地反转的方法
	def reverse(self):
		cur = self.head
		if self.head == None:
			return self.head
		else:
			while cur.next!=None :
				p = cur.next
				cur.next = p.next
				p.next = self.head
				self.head = p

		



##Test

if __name__ == '__main__':
    #直接运行.py则运行，若是import则不运行
    test = SingleLinkList()
    test.isempty()
    test.initlist([2,5,6])
    test.isempty()
    test.append(3)
    test.add(0)
    test.insert(2,10)
    test.travel()
    test.search(3)
    test.search(4)
    test.findmid()
    test.travel()
    test.reverse()
    test.travel()

    