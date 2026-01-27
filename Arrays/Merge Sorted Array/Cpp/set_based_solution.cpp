#include <bits/stdc++.h>
using namespace std;

int removeDuplicates(vector<int>& nums) {
    unordered_set<int> seen;
    int index = 0;

    for (int num : nums) {
        if (seen.find(num) == seen.end()) {
            seen.insert(num);
            nums[index++] = num;
        }
    }
    return index;
}

int main() {
    vector<int> nums = {0,0,1,1,1,2,2,3,3,4};
    int k = removeDuplicates(nums);

    cout << k << endl;
    for (int i = 0; i < k; i++) cout << nums[i] << " ";
}
