# import math
print("=========== Selamat datang di toko andi tersenyum ===========")
totalBelanja = int(input("Total Belanja : "))
diskonPertama = int(totalBelanja-(totalBelanja*0.02))
diskonKedua = int(totalBelanja-(totalBelanja*0.05))
diskonKetifa = int(totalBelanja-(totalBelanja*10/100))
if totalBelanja < 100000:
    print("Tidak ada diskon Maka yang anda bayar adalah Rp ",totalBelanja)
elif totalBelanja >= 100000:
    print("Biaya yang harus di bayarkan adalah Rp ",diskonPertama)
elif totalBelanja >= 500000:
    print("Biaya yang harus di bayarkan adalah Rp ",diskonKedua)
elif totalBelanja >= 1000000:
    print("Biaya yang harus di bayarkan adalah Rp ",diskonKetifa)
    

