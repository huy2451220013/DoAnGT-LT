class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(2 * n);   // mảng kết quả có 2n phần tử

        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];         // nửa đầu
            ans[i + n] = nums[i];     // nửa sau
        }

        return ans;
    }
};
