#include <bits/stdc++.h>
using namespace std;

int removeDuplicates(vector<int>& nums) {
    auto it = unique(nums.begin(), nums.end());
    nums.resize(distance(nums.begin(), it));
    return nums.size();
}

int main() {
    vector<int> nums = {1,1,2};
    int k = removeDuplicates(nums);

    cout << k << endl;
    for (int num : nums) cout << num << " ";
}
