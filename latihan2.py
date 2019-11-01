array = []
total = 0
n = int(input("Masukkan banyaknya elemen array: "))
for x in range(n):
    nilai = float(input("Masukkan bilangan ke-{} : ".format(x+1)))
    array.append(nilai)
    if nilai == 0 :
         break
print("\nHasil bilangan terbesar adalah: {}".format(max(array)))
