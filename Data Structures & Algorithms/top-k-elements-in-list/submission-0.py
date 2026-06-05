class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for numbers in nums:
            freq[numbers] = freq.get(numbers, 0) +1
        sorted_freq = sorted(freq, key=lambda x: freq[x], reverse=True)[:k]
        return sorted_freq

