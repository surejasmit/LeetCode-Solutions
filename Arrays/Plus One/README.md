#Plus One

## 📌 Problem Statement

You are given a large integer represented as an array of digits digits
  Each element contains a single digit

 Digits are stored from most significant to least significant

You need to add one (+1) to the integer and return the resulting array of digits.---

## 🔍 Example

```text
Input:  digits = [1,2,3]
Output: [1,2,4]

```

```text
Input:  digits = [4,3,2,1]
Output: [4,3,2,2]

```text
Input:  digits = [9,9,9]
Output: [1,0,0,0]
```

## 🧠 Key Observations

* The array is **already sorted**
* Duplicate elements appear **next to each other**
* The problem requires **in-place modification**

---

## ✅ Approach 1: Using Set (Your Approach)

### 💡 Idea

   Addition starts from the last digit
  
  If the digit is less than 9, just add 1 and stop
  
  If the digit is 9, it becomes 0 and generates a carry
  
  Carry may propagate to the left
  
  If all digits are 9, array size increases by one


### 📂 Repository Structure & File Navigation

This repository is organized so that **each approach has its own code file**. The README only explains the logic — the actual implementations are kept separate for clean structure and easy access.

```text
Plus-One/
│
├── README.md
│
├── Python/
│   ├── reverse_traversal.py        # Optimal approach
│   ├── number_conversion.py        # Int/String conversion
│   └── recursive_solution.py       # Recursive carry handling
│
├── Cpp/
│   ├── reverse_traversal.cpp       # Optimal C++ solution (recommended)
│   ├── number_conversion.cpp       # Conversion-based approach
│   └── recursive_solution.cpp      # Recursive approach

```

---

## 🔍 Approach 1: Set-Based Method

**File:** `Python/reverse_traversal.py`
**C++ File:** `Cpp/reverse_traversal.cpp`

### Explanation

Traverse the array from right to left

If the digit is less than 9:

Add 1 and return the result immediately

If the digit is 9:

Set it to 0 and continue

If all digits become 0:

Insert 1 at the beginning

### Key Points

* Uses in-place modification
* No extra memory needed
* Most efficient and interview-preferred

### Complexity

* Time: O(n)
* Space: O(1)

---

## 🔍 Approach 2: Number Conversion Method

**File:** `Python/number_conversion.py`
**C++ File:** `Cpp/number_conversion.cpp`

### 💡Idea

* Convert digit array → number
* Add 1
* Convert the number back into digits


### ⚠️ Key Points

* Very easy to implement
* Not safe for very large numbers
* Usually not allowed in interviews

### Complexity

* Time: O(n)
* Space: O(n)

---

## 🔍 Approach 3: Recursive Carry Handling

**File:** `Python/recursive_solution.py`
**C++ File:** `Cpp/recursive_solution.cpp`

### 💡 Idea

* Handle carry using recursion
* Start from the last digit
* If carry reaches beyond first digit, insert 1

###⚠️ Key Points

* Clean logic
* Uses recursion stack
* Slightly higher space usage

### Complexity

* Time: O(n)
* Space: O(n)(recursion stack)

---

## 📊 Approach Comparison

| Approach    | Time       | Space | Interview Friendly |
| ----------- | ---------- | ----- | ------------------ |
| Reverse Traversal   | O(n)       | O(1)  | ✅ Yes                |
|Number Conversion | O(n)       | O(n)  | ❌ No                 |
| Recursive Method  | O(n) | O(n)  | ⚠️ Maybe           |

---

## 🏁 Final Notes

* Reverse Traversal is the most optimal and recommended approach
* Always think about carry propagation
* Code is separated by language and approach for readability
* Prefer in-place solutions for interviews

⭐ *If this repository helped you, consider giving it a star!*
