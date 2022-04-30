class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        prefix = strs[0]
        n =  len(strs)
        for i in range(1,n):
            while prefix and strs[i][:len(prefix)] !=  prefix :
                prefix =  prefix[:len(prefix) -1]
            if not prefix :
                break
        return prefix
