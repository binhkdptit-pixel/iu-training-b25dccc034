# Tìm kiếm ma trận 2D

ma_tran = [[1, 3, 5, 7], [2, 4, 6, 8], [9, 12, 15, 18], [20, 30, 40, 50]]
target = 13

m = len(ma_tran)
n = len(ma_tran[0])
trai = 0
phai = m * n -1
found = False
while trai <= phai:
    mid = (trai + phai) // 2
    hang = mid // n
    cot = mid % n
    gia_tri = ma_tran[hang][cot]
    
    if gia_tri == target:
        found = True
        break
    elif gia_tri < target:
        trai = mid + 1
    else:
        phai = mid - 1

print(found)