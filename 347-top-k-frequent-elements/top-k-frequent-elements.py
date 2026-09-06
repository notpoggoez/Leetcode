from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] +=1 
        
        largest = max(freq.values())
        bucket = [[] for i in range(largest+1)] 
        for key, value in freq.items():
            bucket[value].append(key)
        
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)

                if len(res) == k:
                    return res  