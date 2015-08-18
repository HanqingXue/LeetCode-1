class Solution {
public:
    int addDigits(int num) {
        while (num > 9) {
            int x = 0;
            string s = to_string(num);
            for (int i = 0; i < s.length(); i ++)
                x += (s[i] - '0');
            num = x;
        }
        return num;
    }
};