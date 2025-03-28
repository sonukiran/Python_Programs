#find the second largest in an array
def second_largest(nums):
    if len(nums) < 2:
        return None
    else:
        nums = sorted(set(nums),reverse=True)
        return nums[1]

nums = [1,4,2,5,6,78,23]
print(f"second largest: {second_largest(nums)}")
    