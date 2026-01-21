def remove_element(nums, val):
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            # Swap with last element
            nums[i] = nums[n-1]
            n -= 1  # reduce size of valid array
        else:
            i += 1  # move to next element
    return n  # number of valid elements
