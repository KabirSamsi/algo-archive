class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for x in range(len(haystack) - len(needle)+1):
            if haystack[x::x+len(needle)+1] == needle:
                return x
            else:
                print(haystack[x:x+len(needle)+1])
        return -1

sol = Solution()
print(sol.strStr("sadbutsad", "sad"))