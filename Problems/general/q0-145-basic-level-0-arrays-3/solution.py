"""
Problem: Q0.145 - Basic_Level_0_Arrays_3
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-28
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

n=int(input())
arr=list(map(int,input().split()))
left=0
right=n-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(*arr)
