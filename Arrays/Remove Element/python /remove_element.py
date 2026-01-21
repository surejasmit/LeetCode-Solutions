def remove_element(nums, val):
    k = 0  # pointer for next valid element
    for i in range(len(nums)):
        if nums[i] != val:
            # Place the valid element at index k
            nums[k] = nums[i]
            k += 1  # move to next position
    return k  # number of elements not equal to val
