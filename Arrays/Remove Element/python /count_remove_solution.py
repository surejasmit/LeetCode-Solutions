def remove_element(nums, val):
    new_nums = [x for x in nums if x != val]  # keep valid elements
    for i in range(len(new_nums)):
        nums[i] = new_nums[i]  # copy back
    return len(new_nums)
