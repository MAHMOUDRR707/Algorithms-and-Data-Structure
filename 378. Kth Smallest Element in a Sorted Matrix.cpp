class Solution {
public:
    int counter(vector<vector<int>> matrix,int mid,int n){
        int count = 0 ;
        for(int i = 0 ; i <n ; i++){
            for(int j = 0 ; j <n ; j++){
            if(matrix[i][j] <= mid){
                count++;
            }       
        }     
        }
        return count;  
    }
    
    
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n =  matrix.size();
        int l = matrix[0][0] , r = matrix[n-1][n-1];
        int cont ;
        int mid;
        while(l < r){
             mid = l+(r-l)/2;    
             cont = counter(matrix,mid,n);
            if (cont <k){
                l =  mid+1;
            }
            else{
                r = mid;
            }
        } 
         return l ;     
    }
};
