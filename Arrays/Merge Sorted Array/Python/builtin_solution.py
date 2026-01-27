def remove_duplicates(nums):
    unique = sorted(set(nums))
    k = len(unique)

    for i in range(k):
        nums[i] = unique[i]

    return k


# Example usage
nums = [1,1,2]
k = remove_duplicates(nums)
print(k)        # Output: 2
print(nums)     # [1,2,2]
