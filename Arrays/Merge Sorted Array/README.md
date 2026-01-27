#  Remove Duplicates from Sorted Array (LeetCode 26)

> ⚠️ **Note:** This problem is often confused with LeetCode 88.
> The correct problem number for **Remove Duplicates from Sorted Array** is **LeetCode 26**.

---

## 📌 Problem Statement

Given a **sorted integer array** `nums`, remove the duplicate elements **in-place** such that each unique element appears only once.

The **relative order** of the elements must be preserved.

Return the number of unique elements `k`, such that:

* The first `k` elements of `nums` contain the unique values
* The remaining elements beyond index `k` are not important

> ❗ You must modify the array **in-place** and aim for **O(1)** extra space in the optimal solution.

---

## 🔍 Examples

### Example 1

```text
Input:  nums = [1,1,2]
Output: 2
Updated nums = [1,2,_]
```

### Example 2

```text
Input:  nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5
Updated nums = [0,1,2,3,4,_,_,_,_,_]
```

---

## 🧠 Key Observations

* The array is **already sorted**
* Duplicate elements appear **adjacent** to each other
* Only the **first k elements** matter after removing duplicates
* Instead of deleting elements, we can **overwrite duplicates**

---

## 📂 Repository Structure

Each approach is implemented in a **separate file** for clarity and easy comparison.

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

### 💡 Idea

* Use a `set` to track elements that have already appeared
* Traverse the array from left to right
* If an element is **not in the set**, place it at the next valid index
* Increment the index for each unique element

### ✅ Why It Works

* A set guarantees uniqueness
* The index counter represents the count of unique elements

### ❌ Drawbacks

* Uses extra memory
* Does **not** satisfy strict in-place constraints

### ⏱️ Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

---

## 🔍 Approach 2: Two Pointer Technique (Optimal)

### 💡 Idea

This approach takes full advantage of the **sorted array** property.

* Use one pointer `i` to track the position of the **last unique element**
* Use another pointer `j` to scan the array
* When `nums[j] != nums[i]`:

  * Increment `i`
  * Assign `nums[i] = nums[j]`

### 🧠 Intuition

Since duplicates are adjacent:

* We only need to compare each element with the last unique value
* All unique elements are compacted at the beginning of the array

### ✅ Advantages

* True **in-place** solution
* No extra memory required
* Most **interview-preferred** approach

### ⏱️ Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

## 🔍 Approach 3: Built-in / STL Method

### 💡 Idea

* **Python:** Convert the array to a `set`, sort it, and copy back
* **C++:** Use `std::unique()` followed by resizing the array

### ⚠️ Notes

* Code is concise and readable
* Internally uses extra memory
* Not ideal for strict interview constraints

### ⏱️ Complexity

* **Time Complexity:** O(n log n)
* **Space Complexity:** O(n)

---

## 📊 Approach Comparison

| Approach       | Time       | Space | In-Place | Interview Friendly |
| -------------- | ---------- | ----- | -------- | ------------------ |
| Set-Based      | O(n)       | O(n)  | ❌ No     | ❌ No               |
| Two Pointer    | O(n)       | O(1)  | ✅ Yes    | ✅ Yes              |
| Built-in / STL | O(n log n) | O(n)  | ❌ No     | ❌ No               |

---

## 🏁 Final Notes

* The **Two Pointer approach** is the optimal and recommended solution
* This problem is a classic example of **in-place array manipulation**
* Frequently asked in **FAANG & product-based interviews**

⭐ *If this repository helped you, consider giving it a star!*
