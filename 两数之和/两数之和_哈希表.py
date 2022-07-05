from re import I


class solution:
    def twoSum(self,nums:list[int],target:int) -> list[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
    
nums = [11,9,2,7]
target = 9
test = solution()
print(test.twoSum(nums, target))

        