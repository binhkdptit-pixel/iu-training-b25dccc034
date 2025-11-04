# Tìm kiếm vị chí chèn

nums = [1, 3, 5, 6]
target = int(input("Nhập target: "))

trai  = 0
phai = len(nums) - 1

while trai <= phai:
    mid = (trai + phai) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        trai = mid + 1
    else:
        phai = mid - 1
else:
    print(trai)
