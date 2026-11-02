class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        
        int is_incre = true;
        int is_decre = true;
        int n = nums.size();

        for(int i=0; i<n-1; i++){

            if(nums[i] > nums[i+1]){
                is_incre = false;
            }
            if(nums[i] < nums[i+1]){
                is_decre = false;
            }
        }

        return is_incre || is_decre;
    }
};