'''
Problem 2 — Binary Search (Easy–Medium)

Question:
Given a sorted list, write a function that finds the index of a target element using binary search (iterative).

👉 Example:

arr = [2, 4, 6, 8, 10, 12, 14]
target = 8


✅ Expected Output:

8 found at index 3


❌ If target not in list:

9 not found


Rules:

Use while loop.

No built-in search functions.

Follow the binary search steps:
find mid, compare, move low or high.
'''
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10
half=len(arr)//2
while len(arr)>0:
    if arr[half]==target:
        print(f"{target} found at index {half}")
        break
    elif arr[half]>target:
        print("target is going to find left")
        half=half-1
    elif arr[half]<target:
        print("target is going to find right")
        half=half+1   