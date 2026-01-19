#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        auto it = unique(nums.begin(), nums.end());
        return it - nums.begin();
    }
};
