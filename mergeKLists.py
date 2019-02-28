#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:22:50 2019

@author: laura

https://leetcode-cn.com/problems/merge-k-sorted-lists/
"""

"""
首先先合并两个有序链表，
之后将相邻的链表依次进行合并
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergetwolists(self,l1,l2):#首先合并两个链表的
        l3 = ListNode(0)#空链表
        cur = l3
        while (l1 != None) & (l2!=None):
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2
        l3 = l3.next
        return l3
    def mergeKLists(self, lists):
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        if len(lists)==2:
            return self.mergetwolists(lists[0],lists[1])
        temp = [self.mergetwolists(lists[0],lists[1])]
        if len(lists)>=3:
            for i in range(0,len(lists)-2):
                temp.append(self.mergetwolists(temp[i],lists[i+2]))
            return temp[len(lists)-2]


        