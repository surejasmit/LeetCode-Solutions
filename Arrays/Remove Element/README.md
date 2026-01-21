
# Remove Element

📌 Problem Statement
Given an integer array nums and an integer val, remove all occurrences of val in-place.
The relative order of the remaining elements may change.

You must return the number of elements k that are not equal to val.
The first k elements of nums should contain the valid values, and the remaining
elements can be ignored.


## 🔍 Example

```bash
Input:  nums = [3,2,2,3], val = 3
Output: 2
Updated nums = [2,2,_,_]
```

```bash
Input:  nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5
Updated nums = [0,1,3,0,4,_,_,_]
```

🧠 Key Observations
- The array must be modified in-place
- No extra array should be created
- Order of remaining elements is not important
- Only the first k elements matter
- This problem tests in-place array manipulation

📂 Repository Structure & File Navigation
The repository is structured so that each approach and language has its own file.
The README focuses only on explanation, while implementations are kept separate.


    

```text
Remove-Element/
├── README.md
├── Python/
│   ├── count_remove_solution.py        # Simple count & remove method
│   ├── two_pointer_solution.py         # Optimal two-pointer solution
│   └── swap_with_last_solution.py      # Swap-with-last approach
└── Cpp/
    ├── count_remove_solution.cpp
    ├── two_pointer_solution.cpp
    └── swap_with_last_solution.cpp
```
## 📊 Approach Comparison

| Approach    | Time       | Space | Interview Friendly |
| ----------- | ---------- | ----- | ------------------ |
| Two-Pointer   | O(n)       | O(1)  | ✅ Yes               |
| Swap with End | O(n)       | O(1)  | ✅ Yes(rare val)          |
| Extra Space    | O(n) | O(n)  | ❌ No               |


## 🏁 Final Notes

*Two-Pointer method is optimal and most commonly used in interviews
* Swap with End is a good trick for rare val elements
* Extra space method is simplest but not space-efficient

  ⭐ *If this repository helped you, consider giving it a star!*
