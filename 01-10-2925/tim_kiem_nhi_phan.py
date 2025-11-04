# Tìm kiếm nhị phân cơ bản

n = int(input())
arr = list(map(int, input().split()))
gia_tri_can_tim = int(input())
trai = 0
phai = n - 1
ket_qua = -1
# Dùng vòng lặp để tìm kiếm
while trai <= phai:
    giua = (trai + phai) // 2
    if arr[giua] == gia_tri_can_tim:
        ket_qua = giua
        break
    elif arr[giua] < gia_tri_can_tim:
        trai = giua + 1
    else:
        phai = giua - 1
print(ket_qua)