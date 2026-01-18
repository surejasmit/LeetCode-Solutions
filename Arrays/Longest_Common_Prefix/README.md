
# 14. Longest Common Prefix ⭐

🔍 **Problem Statement**  
Given an array of strings `strs`, write a function to find the **longest common prefix** string amongst the array. If there is no common prefix, return an empty string `""`.

---

## 🧠 **Solution 1: Vertical Scanning (C++)**  
✨ Clean STL implementation  
✅ Returns immediately on mismatch  
⚡ Optimized with `substr()`  

📄 **Code File:** [vertical_scan.cpp](vertical_scan.cpp)

---

## 🐍 **Solution 2: Vertical Scanning (Python)**  
🎯 **Your exact original code** - preserved as-is  
🔄 Direct translation logic maintained  
✅ Identical variable names (`p`, `q`, `mark`)  

📄 **Code File:** [vertical_scan.py](vertical_scan.py)

---

## ⏱️ **Complexity Analysis**  
| Approach | ⏱️ Time | 💾 Space |
|----------|---------|----------|
| **C++** | **O(S)** | **O(1)** |
| **Python** | **O(S)** | **O(1)** |

*Where S = total characters across all strings*

---

## 💡 **Key Insights**  
✅ Check **ALL** strings at each position before advancing  
✅ Vertical scanning guarantees longest prefix  
🚀 Both solutions pass all LeetCode test cases  

---

## 🧪 **File Structure**  
