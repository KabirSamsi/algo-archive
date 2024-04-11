class Solution(object):
    def isValid(self, s):
        parenstack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in ('(', '[', '{'):
                parenstack.append(char)
            elif char in (')', ']', '}'):
                print(parenstack)
                if len(parenstack) == 0:
                    return False
                if parenstack.pop() != pairs[char]:
                    return False
        return True
    
sol = Solution()

print(sol.isValid('()[]'))