from random import random
n = int(input("Masukkan nilai N: "))
for i in range(n):
    while 1:
        n = random()
        if (n < 0.5):
            break
    print("data ke: ",i, "=>",n)
print("Selesai")