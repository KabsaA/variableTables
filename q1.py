def twoSum(nums, target):
        ls = []
        for i in range(0, len(nums)):
            item = target - nums[i]
            nums[i] = "done"
            if item in nums:
                ls.append(i)
                ls.append(nums.index(item))
                return ls

print(twoSum([2,7,11,15],9))
