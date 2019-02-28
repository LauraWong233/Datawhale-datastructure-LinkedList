#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:58:56 2019

@author: laura
"""

"""
https://leetcode-cn.com/problems/majority-element/comments/
leetcode求数组内出现次数大于n/2的元素
"""

##方法一，最常规的方法，但是占用内存较多
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        order = list(set(nums))
        count = []
        length = len(nums)
        for i in order:
            a = 0
            for j in range(0,length):
                if nums[j] == i:
                    a+=1
            count.append(a)
        index = count.index(max(count))          
        return order[index]

##方法二，摩尔投票法，相同+1，不同-1，为0换数
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """     
        count= 0
        for num in nums:
            if count == 0:
                temp = num
            if num == temp:
                count += 1
            else:
                count -= 1
        return temp
            


            
        