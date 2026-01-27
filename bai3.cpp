#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> pos;  // lưu: giá trị -> chỉ số

        for (int i = 0; i < nums.size(); i++) {
            int need = target - nums[i];

            if (pos.find(need) != pos.end()) {
                return {pos[need], i};
            }

            pos[nums[i]] = i;
        }

        return {};
    }
};
