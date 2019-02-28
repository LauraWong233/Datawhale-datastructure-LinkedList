#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:42:21 2019

@author: laura

https://leetcode-cn.com/problems/linked-list-cycle/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return False
        p1 = head
        p2 = head
        while (p1!=None)&(p2!=None):
            if (p1.next==None):
                return False
            if (p2.next == None):
                return False        
            p1 = p1.next
            p2 = p2.next.next
            if p1==p2:
                return True
        return False
    
        