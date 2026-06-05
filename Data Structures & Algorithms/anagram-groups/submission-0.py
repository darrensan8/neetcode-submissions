class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        results = defaultdict(list)

        for letter in strs:
            count = [0] * 26
            for c in letter:
                count[ord(c) - ord('a')] +=1
            results[tuple(count)].append(letter)
        return list(results.values())


        #for words in strs:
