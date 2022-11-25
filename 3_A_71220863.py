nilaiPertama = int(input("Masukan Nilai soal 1 :"))
nilaiKedua = int(input("Masukan Nilai soal 2 :"))
nilaiKetiga = int(input("Masukan Nilai soal 3 :"))
masukanUmur = int(input("Masukan Umur anda : "))
jumlahnilaiSatu = (nilaiPertama*50/100)
jumlahnilaiDua = (nilaiKedua*30/100)
jumlahnilaiTiga = (nilaiKetiga*20/100)
ratarataNilai = (jumlahnilaiSatu+jumlahnilaiDua+jumlahnilaiTiga)
print("Rata-rata nilai anda : " + str(ratarataNilai))
if masukanUmur <= 25 :
    if ratarataNilai >= 80:
        print("Selamat anda lulus")
    else: 
        print("Coba lagi tahun depan")
else : 
    if ratarataNilai >= 90:
        print("Selamat anda Lulus")
    else : 
        print("Coba lagi tahun depan")

