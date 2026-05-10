class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        size = len(nums)

        for i in range(size):
            hashMap[nums[i]] = i

        for i in range(size):
            complement = target - nums[i]
            if complement in hashMap and hashMap[complement] != i:
                return [i, hashMap[complement]]
            




        