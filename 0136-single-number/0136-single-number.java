class Solution {
    public int singleNumber(int[] nums) {
        int n = nums[0];
        for(int i=0;i<nums.length-1;i++){
            n=n^nums[i+1];
        }
        return n;
    }
}