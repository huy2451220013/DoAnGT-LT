#include <unordered_map>
#include <vector>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;

        // Bước 1: đếm tần suất
        for (int i = 0; i < nums.size(); i++) {
            freq[nums[i]]++;
        }

        // Bước 2: bucket sort theo tần suất
        vector<vector<int>> bucket(nums.size() + 1);

        for (auto it : freq) {
            int value = it.first;
            int count = it.second;
            bucket[count].push_back(value);
        }

        // Lấy k phần tử có tần suất cao nhất
        vector<int> ans;
        for (int i = nums.size(); i >= 0 && ans.size() < k; i--) {
            for (int j = 0; j < bucket[i].size(); j++) {
                ans.push_back(bucket[i][j]);
                if (ans.size() == k) {
                    break;
                }
            }
        }

        return ans;
    }
};
