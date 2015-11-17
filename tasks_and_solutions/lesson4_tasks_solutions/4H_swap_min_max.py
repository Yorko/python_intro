nums = map(int, input().split())
i_min, i_max = nums.index(min(nums)), nums.index(max(nums))
nums[i_min], nums[i_max] = nums[i_max], nums[i_min]
print(*nums)