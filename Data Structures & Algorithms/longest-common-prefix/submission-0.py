class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                if prefix == '':
                    return ''
                prefix = prefix[:-1]
        
        return prefix
