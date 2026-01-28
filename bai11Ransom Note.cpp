class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int cnt[26] = {0};

        // Đếm chữ trong magazine
        for (int i = 0; i < magazine.length(); i++) {
            cnt[magazine[i] - 'a']++;
        }

        // Dùng chữ để tạo ransomNote
        for (int i = 0; i < ransomNote.length(); i++) {
            if (cnt[ransomNote[i] - 'a'] == 0) {
                return false;   // không đủ chữ
            }
            cnt[ransomNote[i] - 'a']--;
        }

        return true;
    }
};
