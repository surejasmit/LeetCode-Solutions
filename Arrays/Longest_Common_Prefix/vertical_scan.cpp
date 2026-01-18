#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        
        size_t minLen = strs[0].size();
        for (const string& str : strs) {
            minLen = min(minLen, str.size());
        }
        
        for (size_t i = 0; i < minLen; i++) {
            char ch = strs[0][i];
            for (size_t j = 1; j < strs.size(); j++) {
                if (strs[j][i] != ch) {
                    return strs[0].substr(0, i);
                }
            }
        }
        return strs[0].substr(0, minLen);
    }
};
