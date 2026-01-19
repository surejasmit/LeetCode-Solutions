#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_set<int> seen;
        int i = 0;
        for (int num : nums) {
            if (seen.find(num) == seen.end()) {
                seen.insert(num);
                nums[i++] = num;
            }
        }
        return i;
    }
};
