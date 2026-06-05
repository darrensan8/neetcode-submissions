class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict: dict[str, int] = {}
        tDict: dict[str, int] = {}
        for letters in s:
            sDict[letters] = sDict.get(letters, 0) + 1

        for letter in t:
            tDict[letter] = tDict.get(letter, 0) + 1

        return sDict == tDict
            
            