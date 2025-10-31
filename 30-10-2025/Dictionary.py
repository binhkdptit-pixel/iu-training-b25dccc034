# Từ điển và map

# Tạo một từ điển từ đầu vào lưu tên và số điện thoại
phone_book = {}
n = int(input())

for _ in range(n):
    entry = input().split()
    name = entry[0]
    phone_number = entry[1]
    phone_book[name] = phone_number
try:
    while True:
        query = input()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
except EOFError:
    pass
