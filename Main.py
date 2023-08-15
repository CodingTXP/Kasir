# Menu Utama
print("Aplikasi Kasir Beta 1.0 (Python 3.11.1)")
print("=======================================\r\n\r\n")
print("Menu:\r\na. Registrasi Barang\r\nb. Transaksi")
pilihan = input("Pilihan: ")

if pilihan == "a" or pilihan == "A":
    nama_barang = input("Ketikkan nama barang: ") + "\n"
    harga_barang = float(input("Ketikkan harga barang: ")) + "\n"
    with open("namaBarang.txt", 'a', encoding="utf-8") as file:
        file.write(nama_barang)
    with open("hargaBarang.txt", 'a', encoding="utf-8") as file:
        file.write(harga_barang)
    file = open("hargaBarang.txt", mode = "r")
    baca = file.readlines()
    kode_barang = len(baca)
    print("Registrasi berhasil! Kode barang adalah ", kode_barang, ".")
elif pilihan == "b" or pilihan == "B":
    x = 0
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
else:
    print("Menu tidak tersedia. Mulai ulang program!")

# Akhir Program
print("Program selesai. Terima kasih telah menggunakan!")