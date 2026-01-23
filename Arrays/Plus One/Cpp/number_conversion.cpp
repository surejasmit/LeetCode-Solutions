#include <bits/stdc++.h>
using namespace std;

vector<int> plusOne(vector<int>& digits) {
    long long num = 0;

    for (int d : digits)
        num = num * 10 + d;

    num += 1;

    vector<int> result;
    while (num > 0) {
        result.push_back(num % 10);
        num /= 10;
    }

    reverse(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> digits = {1, 2, 3};
    vector<int> result = plusOne(digits);

    for (int d : result)
        cout << d << " ";

    return 0;
}
