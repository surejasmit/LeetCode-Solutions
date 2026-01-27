def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0  # pointer for last unique element

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


# Example usage
nums = [0,0,1,1,1,2,2,3,3,4]
k = remove_duplicates(nums)
print(k)        # Output: 5
print(nums)     # [0,1,2,3,4,2,2,3,3,4]
