# 1. Two Sum

## 🔍 Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

---

## 🧠 Solution 1: Two Pointer Approach
- Sort the array
- Use two pointers to find the target sum
- Does NOT return original indices

📄 **Code File:** [`two_pointer.py`](./two_pointer.py)

---

## 🧠 Solution 2: Hash Map Approach (Optimal)
- Uses a dictionary to store visited elements
- Returns original indices
- One-pass solution

📄 **Code File:** [`hashmap.py`](./hashmap.py)

---

## ⏱️ Complexity Comparison

| Approach     | Time       | Space | Original Indices |
|-------------|------------|-------|------------------|
| Two Pointer | O(n log n) | O(1)  | ❌ No           |
| Hash Map    | O(n)       | O(n)  | ✅ Yes          |

---

## 📌 Recommendation
The **Hash Map approach** is preferred in interviews due to its optimal time complexity.
