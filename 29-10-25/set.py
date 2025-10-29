# Sử dụng set() và các hàm khác để tính:

def trung_binh(arr):
    so_duy_nhat = set(arr)
    tong = sum(so_duy_nhat)
    dem = len(so_duy_nhat)
    gia_tri_trung_binh = tong / dem
    return round(gia_tri_trung_binh, 3)
n = int(input())
arr = list(map(int, input().split()))
ket_qua = trung_binh(arr)
print(ket_qua)
