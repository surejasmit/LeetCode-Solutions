#include <iostream>
#include <vector>
using namespace std;

int removeElement(vector<int>& nums, int val) {
    int i = 0;
    int n = nums.size();
    while (i < n) {
        if (nums[i] == val) {
            nums[i] = nums[n-1]; // swap with last element
            n--; // shrink array
        } else {
            i++;
        }
    }
    return n; // number of valid elements
}
