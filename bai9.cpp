class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = 0;
        int i = s.length() - 1;

        // Bỏ qua khoảng trắng ở cuối
        while (i >= 0 && s[i] == ' ') {
            i--;
        }

        // Đếm độ dài từ cuối cùng
        while (i >= 0 && s[i] != ' ') {
            len++;
            i--;
        }

        return len;
    }
};
