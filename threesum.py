#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:22:50 2019

@author: laura
https://leetcode-cn.com/problems/3sum/
"""

class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        left = 1
        right = len(nums)-1#首先设置左右指针
        cur = 0
        for i in range(0,len(nums)):
            if i==0 or nums[i]>nums[i-1]:
                if nums[i]<=0:#如果扫描到大于0的就停下
                    cur = i 
                    left =i+1#从当前位置下一个开始
                    right = len(nums)-1
                    while right>left:
                        sum = nums[cur]+nums[left]+nums[right]
                        if sum==0:#只有=0时才会出现重复情况
                            ans.append([nums[cur],nums[left],nums[right]])
                            left+=1
                            right-=1
                            while left<right and nums[left]==nums[left-1]:
                                left+=1
                            while left<right and nums[right]==nums[right+1]:
                                right-=1
                        elif sum>0:
                            right-=1
                        else:
                            left+=1
        return ans

if __name__ == '__main__':
    a = Solution()
    a.threeSum([0,0,0,0])
