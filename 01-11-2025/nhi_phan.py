# Tìm kiếm nhị phân 

nums = list(map(int, input("Nhập mảng đã sắp xếp: ").split()))
target = int(input("Nhập số cần tìm: "))
left = 0
right = len(nums) - 1
index = -1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        index = mid
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(index)
