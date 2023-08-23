# Menu Utama
print("Aplikasi Kasir Beta 1.1 (Python 3.11.1)")
print("=======================================\r\n\r\n")
x = 0

# Masuk
file_namaPengguna = open("namaPengguna.txt", mode = "r")
file_kataSandi = open("kataSandi.txt", mode = "r")
baca_namaPengguna = file_namaPengguna.readlines()
baca_kataSandi =  file_kataSandi.readlines()
while x == 0:
    namaPengguna = input("Masukkan nama pengguna Anda: ") + "\n"
    namaPengguna_sesuai = False
    i = 0
    while i <= len(baca_namaPengguna) - 1:
        if namaPengguna == baca_namaPengguna[i]:
            namaPengguna_sesuai = True
            break
        i += 1
    if namaPengguna_sesuai == False:
        print("Nama pengguna tidak terdaftar!")
    else:
        kataSandi_sesuai = False
        while x == 0:
            kataSandi = input("Masukkan kata sandi Anda: ") + "\n"
            if kataSandi == baca_kataSandi[i]:
                kataSandi_sesuai = True
                break
            if kataSandi_sesuai == False:
                print("Kata sandi salah!")
            else:
                break
    if namaPengguna_sesuai == True and kataSandi_sesuai == True:
        break
namaPengguna = namaPengguna.strip()
print("Selamat datang, ", namaPengguna, ".")

print("Menu:\r\na. Registrasi Barang\r\nb. Transaksi")
pilihan = input("Pilihan: ")

# Menu A
if pilihan == "a" or pilihan == "A":
    while x == 0:
        nama_barang = input("Ketikkan nama barang atau ketikkan \"selesai\" jika sudah selesai: ") + "\n"
        if nama_barang == "selesai\n":
            break
        harga_barang = input("Ketikkan harga barang: ") + "\n"
        with open("namaBarang.txt", 'a', encoding="utf-8") as file:
            file.write(nama_barang)
        with open("hargaBarang.txt", 'a', encoding="utf-8") as file:
            file.write(harga_barang)
        file = open("hargaBarang.txt", mode = "r")
        baca = file.readlines()
        kode_barang = len(baca)
        print("Registrasi berhasil! Kode barang adalah ", kode_barang, ".")
# Menu B
elif pilihan == "b" or pilihan == "B":
    file_harga = open("hargaBarang.txt", mode = "r")
    file_nama = open("namaBarang.txt", mode = "r")
    baca_harga = file_harga.readlines()
    baca_nama = file_nama.readlines()
    total = []
    while x == 0:
        kode_barang = input("Ketikkan kode barang atau ketikkan \"selesai\" jika sudah selesai: ")
        if kode_barang == "selesai":
            break
        elif int(kode_barang) > len(baca_harga):
            print("Kode barang tidak teregistrasi!")
            continue
        else:
            print("(", kode_barang, ") ", baca_nama[int(kode_barang) - 1], " = ", float(baca_harga[int(kode_barang) - 1]))
            jumlah = input("x ")
            total.append(float(baca_harga[int(kode_barang) - 1]) * int(jumlah))
            continue
    print("Total harga barang adalah Rp", sum(total),".")
    pajak = float(input("Masukkan besaran pajak dalam persen (jangan ketikkan \"%\"): "))
    total_akhir = sum(total) + (sum(total) * pajak / 100.00)
    print("Total akhir adalah: ", total_akhir, ".")
# Invalid
else:
    print("Menu tidak tersedia. Mulai ulang program!")

# Akhir Program
print("Program selesai. Terima kasih telah menggunakan!")