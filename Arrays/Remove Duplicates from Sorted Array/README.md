# Remove Duplicates from Sorted Array

## 📌 Problem Statement

Given a **sorted array** `nums`, remove the duplicates **in-place** such that each unique element appears only once. The **relative order** of the elements should be kept the same.

You must return the number of unique elements `k`. The first `k` elements of the array should contain the unique values, and the rest of the array can be ignored.

---

## 🔍 Example

```text
Input:  nums = [1,1,2]
Output: 2
Updated nums = [1,2,_]
```

```text
Input:  nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5
Updated nums = [0,1,2,3,4,_ ,_ ,_ ,_ ,_]
```

---

## 🧠 Key Observations

* The array is **already sorted**
* Duplicate elements appear **next to each other**
* The problem requires **in-place modification**

---

## ✅ Approach 1: Using Set (Your Approach)

### 💡 Idea

* Use a `set` to keep track of elements we have already seen
* Traverse the array
* If an element is not in the set, place it at index `i`
* Increment `i` for the next unique element

### 📂 Repository Structure & File Navigation

This repository is organized so that **each approach has its own code file**. The README only explains the logic — the actual implementations are kept separate for clean structure and easy access.

```text
Remove-Duplicates-from-Sorted-Array/
│
├── README.md
│
├── Python/
│   ├── set_based_solution.py        # Set-based approach
│   ├── two_pointer_solution.py      # Optimal two-pointer approach
│   └── builtin_solution.py          # Built-in Python approach
│
├── Cpp/
│   ├── two_pointer_solution.cpp     # Optimal C++ solution (recommended)
│   ├── set_based_solution.cpp       # Set-based C++ approach
│   └── builtin_solution.cpp         # STL-based approach
```

---

## 🔍 Approach 1: Set-Based Method

**File:** `Python/set_based_solution.py`
**C++ File:** `Cpp/set_based_solution.cpp`

### Explanation

* A set is used to track elements that have already appeared
* While iterating through the array:

  * If the element is new, it is placed at the next valid index
* The index counter represents the number of unique elements

### Key Points

* Easy to understand
* Works for both sorted and unsorted arrays
* Uses extra memory

### Complexity

* Time: O(n)
* Space: O(n)

---

## 🔍 Approach 2: Two Pointer Technique (Optimal)

**File:** `Python/two_pointer_solution.py`
**C++ File:** `Cpp/two_pointer_solution.cpp`

### Explanation

* Takes advantage of the **sorted array** property
* One pointer tracks the last unique element
* Second pointer scans the array
* When a new value is found, it is placed after the last unique element

### Key Points

* In-place solution
* No extra memory used
* Most preferred in interviews

### Complexity

* Time: O(n)
* Space: O(1)

---

## 🔍 Approach 3: Built-in / STL Method

**File:** `Python/builtin_solution.py`
**C++ File:** `Cpp/builtin_solution.cpp`

### Explanation

* Uses language-provided utilities to remove duplicates
* Python uses set + sort
* C++ uses `unique()` from STL

### Key Points

* Very concise
* Less control over in-place behavior
* Not ideal for interviews

### Complexity

* Time: O(n log n)
* Space: O(n)

---

## 📊 Approach Comparison

| Approach    | Time       | Space | Interview Friendly |
| ----------- | ---------- | ----- | ------------------ |
| Set-Based   | O(n)       | O(n)  | ❌ No               |
| Two Pointer | O(n)       | O(1)  | ✅ Yes              |
| Built-in    | O(n log n) | O(n)  | ❌ No               |

---

## 🏁 Final Notes

* The **Two Pointer approach** is the most optimal and recommended
* Code is separated by language and approach for clarity
* Click on any file above to directly view the implementation

⭐ *If this repository helped you, consider giving it a star!*
