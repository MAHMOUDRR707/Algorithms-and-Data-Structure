class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
      vector<unsigned int>res(target+1);
      res[0] = 1 ;
      for(int i =1 ;i<target+1;i++){
          for(int j= 0;j<nums.size();j++){
              if (nums[j] <= i){
                  res[i] +=  res[i-nums[j]];
              }
          }
      }

    return res[target];
    }
};
