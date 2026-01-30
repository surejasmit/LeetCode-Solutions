
📌 Problem Statement
Given an integer numRows, return the first numRows rows of Pascal’s Triangle.

In Pascal’s Triangle:
- The first and last element of each row is always 1
- Each interior element is the sum of the two elements directly above it

The result should be returned as a list of lists representing each row.


🔍 Example
```text
Input:  numRows = 5

Output:
[
     [1],
    [1, 1],
   [1, 2, 1],
  [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
```

```text
Input:  numRows = 1  
Output: [[1]]
```

🧠 Key Observations
- The first row is always [1]
- Each row contains (row index + 1) elements
- First and last elements of every row are always 1
- Middle elements are calculated as the sum of two elements directly above
- This problem tests pattern recognition and basic dynamic programming concepts


📂 Repository Structure & File Navigation
The repository is structured so that explanation and implementations are separated.
This file contains only conceptual understanding, while language-specific solutions
are stored in their respective folders.

```text
Pascal-Triangle/
├── README.md
├── Python/
│   └── generate_pascal_triangle.py
└── Cpp/
    └── generate_pascal_triangle.cpp
```

```text
📊 Approach Comparison

Approach              | Time     | Space   | Interview Friendly
--------------------- | -------- | ------- | ------------------
Dynamic Programming   | O(n²)    | O(n²)   | Yes
Mathematical Formula  | O(n²)    | O(n²)   | Rare
Recursive Generation  | O(n²)    | O(n²)   | No
```

🏁 Final Notes
- Dynamic Programming is the most common and preferred approach in interviews
- This problem is frequently asked to test logical pattern building
- It forms the foundation for problems like Pascal’s Triangle II

⭐ If this file helped you, consider giving the repository a star!
