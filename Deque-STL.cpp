#include <iostream>
#include <deque> 
#include <algorithm>
using namespace std;

bool comp(int a, int b){
    return b >a ;
}
void printKMax(int arr[], int n, int k){
	//Write your code here.
    
    deque<int> z ;
    for(auto i  = 0 ; i <n ; ++i){
        while(!z.empty() && arr[i] >  z.back()){
            z.pop_back();
        }
        z.emplace_back(arr[i]);
        if (i+1 >=k ){
            cout << z.front() <<" ";
            if(arr[i+1-k] >=  z.front()){
                z.pop_front();
                
            }
        }  
        
    }
    cout << endl;
}

int main(){
  
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
    	for(i=0;i<n;i++)
      		cin >> arr[i];
    	printKMax(arr, n, k);
    	t--;
  	}
  	return 0;
}
