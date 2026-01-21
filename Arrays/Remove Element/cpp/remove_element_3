#include <iostream>
#include <vector>
using namespace std;

int removeElement(vector<int>& nums, int val) {
    vector<int> new_nums;
    for (int x : nums) {
        if (x != val) new_nums.push_back(x); // store valid elements
    }
    for (int i = 0; i < new_nums.size(); i++) {
        nums[i] = new_nums[i]; // copy back
    }
    return new_nums.size();
}
