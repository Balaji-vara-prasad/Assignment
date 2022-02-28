# 6 Python program to implement binary search
def binarySearch(nums, low, high, ele):
    if high >= low:
        mid = low + (high - low) // 2
        if nums[mid] == ele:
            return mid
        elif nums[mid] > ele:
            return binarySearch(nums, low, mid - 1, ele)
        else:
            return binarySearch(nums, mid + 1, high, ele)
    else:
        return -1


numbers = [1, 4, 6, 7, 12, 17, 25]
x = int(input("Enter the number find: "))
result = binarySearch(numbers, 0, len(numbers) - 1, x)
if result != -1:
    print("Search successful, element found at position ", result)
else:
    print("unsuccessful")
