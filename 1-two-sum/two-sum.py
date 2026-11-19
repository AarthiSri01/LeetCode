class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res={} #val:index -> form of storing the values in the hashmap
        for i,n in enumerate(nums):
            diff=target-n
            if diff in res:
                return [res[diff],i]
            res[n]=i
        return
        