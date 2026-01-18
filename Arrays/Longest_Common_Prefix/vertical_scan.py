class Solution(object):
    def longestCommonPrefix(self, strs):
        s = ""
        min_length = min(len(word) for word in strs)
        for p in range(min_length):
            q = strs[0][p]
            mark = True
    
            for y in range(1,len(strs)):
                if strs[y][p] == q:
                    continue
                else:
                    mark = False
                    break
    
            if mark:
                s += q
            else:
                break
        return s
