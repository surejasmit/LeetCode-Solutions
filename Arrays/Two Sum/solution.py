class Solution(object):
    def twoSum(self, nums, target):
        nums.sort()
        left = 0
        right = len(nums) - 1
        l = []

        while left <= right:
            if nums[left] + nums[right] == target:
                l.append(left)
                l.append(right)
                return l
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1



# hash map method
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i

# c++ code

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int left = 0, right = nums.size() - 1;

        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum == target) {
                return {left, right};
            } else if (sum > target) {
                right--;
            } else {
                left++;
            }
        }
        return {};
    }
};
