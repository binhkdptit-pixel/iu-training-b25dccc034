# Chấm điểm thi 


n = int(input().strip())
students = []
   
# vòng lặp for
for i in range(1, n + 1):
    name = input().strip()
    diem1 = float(input().strip())
    diem2 = float(input().strip())

    if diem1 > 10: diem1 /= 10      # Trường hợp nhập nhầm và tính theo thang điểm 100
    if diem2 > 10: diem2 /= 10


    diem_trung_binh = (diem1 + diem2)/2
# Phân loại thứ hạng 

    if diem_trung_binh < 5.0:
       rank = "TRUOT"
    elif diem_trung_binh < 8.0:
       rank = "CAN NHAC"
    elif diem_trung_binh < 9.5:
       rank = "DAT"
    else:
       rank = "XUAT SAC"
    
    code = f"TS{str(i).zfill(2)}"
    students.append((diem_trung_binh, code, name, rank))

students.sort()
for diem_trung_binh, code, name, rank in students:
   print(f"{code} {name} {diem_trung_binh:.2f} {rank}")

    
    
