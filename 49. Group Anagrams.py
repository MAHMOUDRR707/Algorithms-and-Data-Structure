#link : https://leetcode.com/problems/group-anagrams/submissions/
#time:o(n)
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for i in strs :
            ans[tuple(sorted(i))].append(i)

        return ans.values()

z =  list(input().split())
s =  Solution(z)
print(s)
