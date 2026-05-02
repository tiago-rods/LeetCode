class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fqMap = {} 
        for num in nums:
            fqMap[num] = fqMap.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in fqMap.items():
            buckets[freq].append(num)

        result = []

        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
                
        return result  