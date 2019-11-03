# Latihan 1

1. Langkah pertama menginputkan penyebutnya :

- num = int(input("Masukan nilai n: ")) 
- jumlah = num+1 
- start = 1 
- stop = jumlah 
- step = 1 

4. Lalu masukan Statment for i in range(start, stop, step):

-for i in range(start,stop,step):
    -if(1 % 0.5):   
        -continue
        
5. Agar angka yang dimasukan random masukan:

    - from random import random    
    - a = random()

6. Yang terakhir cetaklah variable menggunakan:

    - print("Data ke:",i,"=>",(a))
    
    # Hasilnya
![lat01](https://user-images.githubusercontent.com/56239989/68085468-fa90d280-fe73-11e9-84b5-a0c46022a927.jpg)


# Latihan 2

1. Langkah pertama masukan variable yang akan di inputkan bebas:

- array = []
- total = 0
- n = int(input("Masukkan banyaknya elemen array: "))

2. Langkah kedua masukan statment:

- for x in range(n):
    - nilai = float(input("Masukkan bilangan ke-{} : ".format(x+1)))
    - array.append(nilai)
    - if nilai == 0 :
         -- break

3. Langkah Terakhir print menggunakan:

- print("\nHasil bilangan terbesar adalah: {}".format(max(array)))
