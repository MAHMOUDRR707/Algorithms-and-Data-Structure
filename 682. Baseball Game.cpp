#include <cstdlib>
#include <string>

class Solution {
public:
    int calPoints(vector<string>& ops) {
        int n =  ops.size();
        vector<int> z ;
        int last = 0  ;
        for(string i : ops){
            if (isdigit(i[0]) || i[0] == '-'){
                int w =  stoi(i);
                z.push_back(w);                
            }
            else if (i[0] == 'D'){
                z.push_back(z[last]*2);
            }
            else  if (i[0]  == 'C'){
                z.pop_back();
                }
            else if  (i[0]  == '+'){
                z.push_back(z[last] + z[last-1]);
            }
            last =  z.size() -1 ; 
        }
       
        return accumulate(z.begin(), z.end(),0); 
    }
};
