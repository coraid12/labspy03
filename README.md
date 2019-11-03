# Tugas Pemrograman
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
    
# Hasil Latihan 1
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
     - break

3. Langkah Terakhir print menggunakan:

- print("\nHasil bilangan terbesar adalah: {}".format(max(array)))

# Hasil latihan 2
![lat02](https://user-images.githubusercontent.com/56239989/68085630-83f4d480-fe75-11e9-980c-553e07db57b6.jpg)

# Program 1

1.Langkah pertama inputkan variabel modal,laba,dan untung ,sebagai berikut:

- modal = 100000000
- laba = 0
- untung = 0 

2.Selanjutnya masukan prosessnya :

 for i in range(1,9,1):
       - if(i<3):
       - laba = 0
       - untung = untung + laba
      - elif(i<5):
       - laba = modal*1/100
       - untung = untung + laba
      - elif(i<8):
       - laba = modal*5/100
       - untung = untung + laba
      - else:
       - laba = modal*2/100
       - untung = untung + laba
