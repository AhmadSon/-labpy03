# program mencari nilai terbesar dengan perulangan
max = 0
while True:
    n = int(input("Masukkan bilangan: "))
    if max < n :
        max = n
    if n == 0:
        break
print("Bilangan terbesar adalah: ",max)
