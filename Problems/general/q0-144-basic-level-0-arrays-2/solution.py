"""
Problem: Q0.144 - Basic_Level_0_Arrays_2
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-28
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range(len(arr)):
    sum+=arr[i]
print(sum)
