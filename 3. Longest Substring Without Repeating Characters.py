#link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
#time :o(n)
class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0 
        end  =0 
        ans = 0 
        c = 0
        z = set()
        n = len(s)
        for i in range(n) :
            if s[i] not in z :
                z.add(s[i])
                c =  i - start +1 
                ans =  max(ans,c)
                
            else :
                while s[i] !=  s[start] :
                    z.remove(s[start])
                    start += 1
                start +=1
        
        return ans
    
