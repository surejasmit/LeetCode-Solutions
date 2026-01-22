## Search Insert Position
=====================

## Problem Statement
-----------------
Given a sorted array of distinct integers nums and a target value,
return the index if the target is found.

If the target is not found, return the index where it would be inserted
in order.

You must write an algorithm with O(log n) time complexity.


Example
-------

```text

Input:  nums = [1,3,5,6], target = 5
Output: 2

Input:  nums = [1,3,5,6], target = 2
Output: 1

Input:  nums = [1,3,5,6], target = 7
Output: 4

```

# Key Observations
----------------
- The array is already sorted
- All elements are distinct
- If the target is missing, we still return a valid index
- Sorted data strongly suggests Binary Search
- The returned index must maintain sorted order


## Repository Structure & File Navigation
-------------------------------------

This repository is organized so that each approach is implemented
in a separate file. The README explains the logic only.

```text
Search-Insert-Position/
|
|-- README.txt
|
|-- Python/
|   |-- linear_search_solution.py      # Brute-force approach
|   |-- binary_search_solution.py      # Optimal approach
|   |-- builtin_bisect_solution.py     # Python built-in method
|
|-- Cpp/
|   |-- linear_search_solution.cpp     # Brute-force approach
|   |-- binary_search_solution.cpp     # Optimal C++ solution
|   |-- builtin_solution.cpp           # STL-based approach

```
## Approach 1: Linear Search (Brute Force)
--------------------------------------

File: Python/linear_search_solution.py
C++ File: Cpp/linear_search_solution.cpp

## Explanation
-----------
- Traverse the array from left to right
- If the current element is greater than or equal to the target,
  return the current index
- If the loop finishes, the target is greater than all elements,
  so return the array length

 ## Key Points
----------
- Very easy to understand
- Works for any array
- Does not satisfy the required O(log n) constraint

```twxt
Time Complexity
---------------
O(n)

Space Complexity
----------------
O(1)
```

## Approach 2: Binary Search (Optimal)
----------------------------------

File: Python/binary_search_solution.py
C++ File: Cpp/binary_search_solution.cpp

## Explanation
-----------
- Uses two pointers: left and right
- Calculate the middle index
- If nums[mid] equals target, return mid
- If nums[mid] is smaller than target, search the right half
- If nums[mid] is greater than target, search the left half
- When the loop ends, the left pointer gives the correct insert position

## Why Returning Left Works
------------------------
- When the target is not found, left always points to the index
  where the target should be inserted to keep the array sorted

## Key Points
----------
- Uses sorted array property
- In-place and efficient
- Most recommended approach for interviews
```text
Time Complexity
---------------
O(log n)

Space Complexity
----------------
O(1)
```

##Approach 3: Built-in Method
--------------------------

File: Python/builtin_bisect_solution.py
C++ File: Cpp/builtin_solution.cpp

## Explanation
-----------
- Python uses the bisect module
- bisect_left returns the insertion index automatically
- C++ can use lower_bound from STL

## Key Points
----------
- Very concise
- Internally uses binary search
- Not always allowed in interviews

```text
Time Complexity
---------------
O(log n)

Space Complexity
----------------
O(1)
```

## Approach Comparison
------------------

Approach        | Time     | Space | Interview Friendly
--------------- | -------- | ----- | ------------------
Linear Search   | O(n)     | O(1)  | No
Binary Search   | O(log n) | O(1)  | Yes
Built-in Method | O(log n) | O(1)  | Depends


Final Notes
-----------
- Binary Search is the optimal and expected solution
- Code is separated by language and approach for clarity
- Best problem to understand Binary Search fundamentals

Problem Link
------------
https://leetcode.com/problems/search-insert-position/
