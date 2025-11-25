def sum_list_rec(nums):
    if not nums: #proverqva dali e prazen spisuka
        return 0
    return nums[0] + sum_list_rec(nums[1:])
