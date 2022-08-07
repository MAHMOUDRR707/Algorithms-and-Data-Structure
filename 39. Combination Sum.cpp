class Solution {
public:
    vector<vector<int>> combinationSum(vector<int> candidates, int target) {       sort(candidates.begin(),candidates.end());
        vector<vector<int>> ans;
        vector<int>temp;
        helper(target,candidates,ans,temp,0);
        return ans;
        
    }
    void helper(int target,vector<int> candidates,vector<vector<int>> &ans,vector<int> temp,int start){
         if (target == 0){
            ans.push_back(temp);
            return;
        }
        if (target <  candidates[start]) {
            return ;
        }
       
       for(int i = start ; i <candidates.size();i++){
              temp.push_back(candidates[i]);
              helper(target-candidates[i],candidates,ans,temp,i);  
              temp.pop_back();
            }      
    }
    
};
