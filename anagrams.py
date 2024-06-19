class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {} # Hashmap Created

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # if countS contains i, increment by value
            countT[t[i]] = 1 + countT.get(t[i], 0) # if countT contains i, increment by value
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False 
        return True
    

test = Solution()

print(test.isAnagram(s='anagas', t='gasnaa')) # True
print(test.isAnagram(s='anaggas', t='gasnaa')) # False 
      