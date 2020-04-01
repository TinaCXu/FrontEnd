class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # list = input()
        #loop the strings in list
        var = 0
        idx = 0
        choose = []
        while strs[var][idx] == strs[var+1][idx] and var <= len(strs)-2:
            var += 1
            if var == len(strs)-1:
                choose.append((strs[var][idx]))
                idx += 1
                var = 0
            else:
                continue

        Output = ''.join(choose)
        return(Output)