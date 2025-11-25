def sum_list_rec(nums):
    if not nums:
        return 0
    return nums[0] + sum_list_rec(nums[1:])
