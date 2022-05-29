import re
class Solution:
    def get_state(self,word):
        state = 0
        for i in word :
            index = ord(i)  - ord('a')
            state |= 1 <<  index
        return state
    
    def maxProduct(self, words: List[str]) -> int:
        words.sort(reverse = True)
        n = len(words) 
        x = 0
        max_x = 0
        first = 0
        second = 0
        z = {}
        for i in range(n):
            z[i] =  self.get_state(words[i])
            
        print(z)
        for i in range(n):
            for j in range(i+1,n):
                if (z[i] & z[j]) == 0:
                    x =  len(words[i]) * len(words[j])
                    max_x =  max(x,max_x)
                    print(words[i],words[j])
        return (max_x)
    
