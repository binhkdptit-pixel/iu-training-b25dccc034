# Tìm kiếm tuyến tính trong một danh sách

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
found = -1
for i in range(n):
    if arr[i] == k:
        found = i
        break
print(found)

