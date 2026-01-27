class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;

        while (i < s.length() && j < t.length()) {
            if (s[i] == t[j]) {
                i++;   // tìm được ký tự tiếp theo của s
            }
            j++;       // luôn dịch sang phải trong t
        }

        return i == s.length();
    }
};
