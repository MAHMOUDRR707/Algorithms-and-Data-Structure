#include <list>
class Solution {
public:
    string toGoatLatin(string s) {
        char z[10] = {'A','E','I','O','U','a','e','i','o','u'} ;
        int n,i,m = 0;
        i =  0 ;
        string  res ;
        char v ;
        bool x;
        string y ;
        n  =  s.size();
        while(i<  s.size() ){
            y = "";
            m += 1 ;
            while(i< s.size() && s[i] != ' '){
                y += s[i];
                i++;
            }
            i++;
            x =  false;
            
            if(binary_search(z,z+10,y[0]))x=true;

           if (x == true) {
               y = y + "ma" ;
               for(int j = 0 ; j <m;j++){
                   y = y  + "a";
                       
               }
               res =  res + y + ' ' ;
           }
           else {
               v =  y[0];
               y.erase(0,1);
               y= y +   v;
               y =  y + "ma";
               for(int j = 0 ; j <m;j++){
                   y = y  + "a";         
               }
               res =  res + y + ' ' ;
           } 
        }
        res.erase(res.size()-1 ,res.size());
        return res;
    }
};
