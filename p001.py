class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = []
        
        for i, num in enumerate(nums):
            difference = target - num

            if difference in num_list:
                return [i, nums.index(difference)]
            
            num_list.append(num)
