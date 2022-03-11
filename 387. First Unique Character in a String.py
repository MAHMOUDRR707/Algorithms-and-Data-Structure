#link :https://leetcode.com/problems/first-unique-character-in-a-string/
#time:o(n)
class Solution:
    def firstUniqChar(self, s):
        for i in range(len(s)) :
            if  s.count(s[i]) == 1:
                return i
        return -1
