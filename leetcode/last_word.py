class Solution(object):
    def lengthOfLastWord(self, s):
        current_word = ""
        index = 0
        words = []

        while index < len(s):
            while index < len(s) and s[index] == " ":
                index += 1
            while index < len(s) and s[index] != " ":
                current_word += s[index]
                index += 1
            if current_word != "":
             words.append(current_word)
            current_word = ""
        
        print(words)
        if len(words) == 0:
            return 0
        return len(words[-1])
        
            

sol = Solution()

print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
print(sol.lengthOfLastWord(" "))
print(sol.lengthOfLastWord("luffy is still joyboy"))