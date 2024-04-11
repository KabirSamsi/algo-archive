class Solution(object):
    def shortest_word(self, strs):
        if len(strs) == 0:
            return ""
        shortest = strs[0]
        for string in strs:
            if len(string) < len(shortest):
                shortest = string
        return shortest

    def longestCommonPrefix(self, strs):
        shortest = self.shortest_word(strs)
        prefix = ""
        counter = 0
        test_prefix = shortest[0]
        while counter < len(shortest):
            for word in strs:
                if word[:counter+1] != test_prefix:
                    print(word[:counter+1])
                    return prefix
            prefix = test_prefix
            test_prefix = word[:counter+1]
            counter += 1

testCase = Solution()
print(testCase.longestCommonPrefix(["flower", "flow", "flight"]))