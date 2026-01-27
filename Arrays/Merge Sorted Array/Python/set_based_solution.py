def remove_duplicates(nums):
    seen = set()
    index = 0

    for num in nums:
        if num not in seen:
            seen.add(num)
            nums[index] = num
            index += 1

    return index


# Example usage
nums = [0,0,1,1,1,2,2,3,3,4]
k = remove_duplicates(nums)
print(k)        # Output: 5
print(nums)     # [0,1,2,3,4,2,2,3,3,4]
