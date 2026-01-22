import bisect

def searchInsert(nums, target):
    return bisect.bisect_left(nums, target)
