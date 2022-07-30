#include <algorithm>

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int n =  matrix.size();
        int m = matrix[0].size();
        int res[n+1][m+1] ;
        int sum= 0 ;
        for(int i = 0 ;i < n+1 ; i++){
            for(int j = 0 ; j<m+1 ;j++){
                res[i][j] = 0 ;
            }
        }
        
        for(int i = 1 ;i <= n ; i++){
            for(int j = 1 ; j<= m ;j++){
                if (matrix[i-1][j-1] == '1') {
            res[i][j] =  min({res[i-1][j],res[i][j-1],res[i-1][j-1]}) +1; 
            sum =  max(sum,res[i][j]);
                }
                }
        }
    return sum*sum;
    }
};
