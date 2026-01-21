Remove Element (LeetCode 27)

📌 Problem Statement
Given an integer array nums and an integer val, remove all occurrences of val in-place.
The relative order of the remaining elements may change.

You must return the number of elements k that are not equal to val.
The first k elements of nums should contain the valid values, and the remaining
elements can be ignored.

🔍 Example
Input:  nums = [3,2,2,3], val = 3
Output: 2
Updated nums = [2,2,_,_]

Input:  nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5
Updated nums = [0,1,3,0,4,_,_,_]

🧠 Key Observations
- The array must be modified in-place
- No extra array should be created
- Order of remaining elements is not important
- Only the first k elements matter
- This problem tests in-place array manipulation

📂 Repository Structure & File Navigation
The repository is structured so that each approach and language has its own file.
The README focuses only on explanation, while implementations are kept separate.

Remove-Element/
│
├── README.md
│
├── Python/
│   ├── count_remove_solution.py        # Simple count & remove method
│   ├── two_pointer_solution.py         # Optimal two-pointer solution
│   └── swap_with_last_solution.py      # Swap-with-last approach
│
├── Cpp/
│   ├── count_remove_solution.cpp
│   ├── two_pointer_solution.cpp
│   └── swap_with_last_solution.cpp

🔍 Approach 1: Count & Remove Method (Simple but Inefficient)
Files:
- Python: Python/count_remove_solution.py
- C++: Cpp/count_remove_solution.cpp

Explanation
This approach first counts how many times val appears in the array.
It then removes val repeatedly using built-in removal functions.
Finally, the updated length of the array is returned.

Key Points
- Very easy to understand
- Uses built-in language features
- Multiple shifts occur during removal
- Not suitable for large inputs

Complexity
- Time: O(n²)
- Space: O(1)

🔍 Approach 2: Two Pointer Technique (Optimal & Recommended)
Files:
- Python: Python/two_pointer_solution.py
- C++: Cpp/two_pointer_solution.cpp

Explanation
This method uses two pointers:
- One pointer tracks where the next valid element should be placed
- The second pointer scans through the array

Whenever an element is not equal to val, it is placed at the valid position.
The count of valid elements becomes the final answer.

Key Points
- Fully in-place
- No extra memory required
- Preserves relative order
- Most preferred in interviews

Complexity
- Time: O(n)
- Space: O(1)

🔍 Approach 3: Swap with Last Element (Order Not Preserved)
Files:
- Python: Python/swap_with_last_solution.py
- C++: Cpp/swap_with_last_solution.cpp

Explanation
If the current element is equal to val, it is replaced with the last element
of the array. The array size is then reduced.
The index is not moved forward after a swap.

This minimizes operations when order does not matter.

Key Points
- Very efficient
- Order of elements is not preserved
- Useful when minimizing writes

Complexity
- Time: O(n)
- Space: O(1)

📊 Approach Comparison
Approach               Time     Space     Interview Friendly
Count & Remove         O(n²)    O(1)      ❌ No
Two Pointer            O(n)     O(1)      ✅ Yes
Swap with Last         O(n)     O(1)      ✅ Yes

🏁 Final Notes
- The Two Pointer approach is the most optimal and recommended solution
- Swap-with-last is useful when order does not matter
- Count & remove is simple but inefficient
- Code is separated by language and approach for clarity
- Click any file in the repository to directly view the implementation

⭐ If this repository helped you, consider giving it a star!
