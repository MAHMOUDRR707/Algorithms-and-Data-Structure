#include <bits/stdc++.h>
#include <algorithm>
class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        int n =  points.size();
        sort(points.begin(),points.end());
        int x,max_x = 0 ; 
        for(int i = 1 ;i<n;i++){
            x =  points[i][0] - points[i-1][0];
            max_x =  max(max_x,x);
        }
        return max_x;
    }
     
};
