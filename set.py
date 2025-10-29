# sử dụng set() và các hàm khác để tính:

def trung_binh(arr):
    unique_numbers = set(arr)
    tong = sum(unique_numbers)
    dem = len(unique_numbers)
    gia_tri_trung_binh = tong / dem
    return round(gia_tri_trung_binh, 3)
if __name__ == '__main__':
    n = int(input())  
    arr = list(map(int, input().split())) 
    result = trung_binh(arr)
    print(result)
