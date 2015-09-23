class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // Boyer–Moore majority vote algorithm
        // https://www.cs.utexas.edu/~moore/best-ideas/mjrty/index.html
        int count = 0;
        int element = nums[0];
        for (int i = 0; i < nums.size(); i++) {
            if (count == 0) {
                element = nums[i];
                count++;
            }
            else if (count != 0 && nums[i] == element) {
                count++;
            }
            else {
                count--;
            }
        }
        return element;
    }
};
