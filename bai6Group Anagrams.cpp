#include <unordered_map>
#include <algorithm>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;

        for (int i = 0; i < strs.size(); i++) {
            string key = strs[i];
            sort(key.begin(), key.end());   // sắp xếp chữ cái

            mp[key].push_back(strs[i]);     // gom vào nhóm
        }

        vector<vector<string>> ans;
        for (auto it : mp) {
            ans.push_back(it.second);
        }

        return ans;
        
    }
};
