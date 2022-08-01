#include<iostream>
#include<vector>
#include<numeric>
#include <bits/stdc++.h>
class Solution {
public :
    vector<vector<int>> res;
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int>  t ;
        sort(candidates.begin(),candidates.end());
        int n =  candidates.size();
        backtracking(0,t,n,target,candidates);
        return res;
        
    }
    void backtracking(int start,vector<int> t ,int n , int target , vector<int> c){
        if(accumulate(t.begin(),t.end(),0)  == target) {
            res.push_back(t);
        }
        
        if(accumulate(t.begin(),t.end(),0) >  target){
            return ;
        }
        
        for(int i = start ; i < n; i++ ){
            if(i > start && c[i] ==  c[i-1]){
                continue ;
            }
            t.push_back(c[i]) ;
            backtracking(i+1,t,n,target,c);
            t.pop_back();
        }
        
        
    }
    
};
