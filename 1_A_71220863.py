namaMahasiswa = input("Masukan Nama Mahasiswa : ")
nimMahasiswa = input("Masukan Nim Mahasiswa : ")
if nimMahasiswa [0:2] == "71" and int(nimMahasiswa[2:4]) <=22 and int(nimMahasiswa[2:4]) >=20:
    print(f'{namaMahasiswa}, Merupakan mahasiswa informatika angkatan 20 hingga 22')
else:
    print(f'{namaMahasiswa},bukan merupakan mahasiwa informatika angkatan 20 hingga 22')