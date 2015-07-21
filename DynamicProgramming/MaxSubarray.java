/*
Time O(n), Space O(n)
One Scan
*/

public class Solution {
    public int maxSubArray(int[] nums) {
        //Initialise a DP array 
        int[] dp = new int[nums.length];
        // Arrays.fill(array, 0); (A default value of 0 for arrays)
        
        // First element is best
        dp[0] = nums[0];
        
        int maxSum = dp[0];
        
        // Compare/Dp step
        for (int i = 1; i < nums.length; i++) {
            dp[i] = Math.max(nums[i], nums[i] + dp[i-1]);
            maxSum = Math.max(dp[i], maxSum);
        }
        return maxSum;
    }
}
