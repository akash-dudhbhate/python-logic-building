''' 

Problem 1 — Linear Search (Easy)

Question:
Write a Python function that checks if a number exists in a list.

👉 Example:

arr = [5, 10, 15, 20, 25]
target = 15


✅ Expected Output:

15 found at index 2


❌ If not found:

30 not found


Rules:

Use a for loop (no built-in functions like index()).

Use linear search logic only.

Handle both “found” and “not found” cases.

'''

arr = [5, 10, 15, 20, 25, 30]
target = 30

for i,val in enumerate(arr):
    if val == target:
        print(f"{target} found at index {i}")
        break
    elif i == len(arr) - 1:
        print(f"{target} not found")

    