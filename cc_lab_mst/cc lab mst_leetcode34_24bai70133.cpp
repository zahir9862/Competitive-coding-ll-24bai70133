#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {

        int n = nums.size();

        // Find first occurrence
        int left = 0, right = n - 1;
        int first = -1;

        while (left <= right) {

            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                first = mid;
                right = mid - 1;
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        // Find last occurrence
        left = 0;
        right = n - 1;
        int last = -1;

        while (left <= right) {

            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                last = mid;
                left = mid + 1;
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        return {first, last};
    }
};

int main() {

    // Input
    vector<int> nums = {5, 7, 7, 8, 8, 10};
    int target = 8;

    // Create object
    Solution obj;

    // Call function
    vector<int> result = obj.searchRange(nums, target);

    // Display output
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;

    return 0;
}