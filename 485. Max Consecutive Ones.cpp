#include <algorithm>
class Solution {
public:
   
    
    int findMaxConsecutiveOnes(vector<int>& nums) {
        vector<int> res;
        int max_n = 0 , n = 0;
        for(int i =0 ; i <nums.size();i++){
            if(nums[i] == 0){
                max_n = max(max_n,n);
                n = 0;
            }
            else{
                n++;
            }
        }
        max_n = max(max_n,n);
        return max_n;
    }
    
  
};
