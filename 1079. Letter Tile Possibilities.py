from itertools  import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        x = 0
        for i in range(1,n+1):
            x+=(len(set(list(permutations(tiles,i)))))
        return x
