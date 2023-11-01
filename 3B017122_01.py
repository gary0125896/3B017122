a = int(input("請輸入星星數量："))

for i in range(1, a, 2):
    print(" " * ((a - i) // 2) + "*" * i)

print("*" * a)

for i in range(a - 2, 0, -2):
    print(" " * ((a - i) // 2) + "*" * i)