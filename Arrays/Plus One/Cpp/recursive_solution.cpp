#include <bits/stdc++.h>
using namespace std;

void addOne(vector<int>& digits, int index) {
    if (index < 0) {
        digits.insert(digits.begin(), 1);
        return;
    }

    if (digits[index] < 9) {
        digits[index]++;
    } else {
        digits[index] = 0;
        addOne(digits, index - 1);
    }
}

vector<int> plusOne(vector<int>& digits) {
    addOne(digits, digits.size() - 1);
    return digits;
}

int main() {
    vector<int> digits = {9, 9};
    vector<int> result = plusOne(digits);

    for (int d : result)
        cout << d << " ";

    return 0;
}
