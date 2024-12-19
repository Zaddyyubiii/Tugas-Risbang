1. Nama pelanggan akan disimpan di variabel "nama".
2. Menampilkan kalimat selamat datang dengan nama pelanggan didalamnya dengan memasukkan variabel "nama" di dalamnya.
3. Menampilkan barang yang dijual (buku, pulpen, pensil) dengan membuat variabel list/array barang = ["buku", "pulpen", "pensil"]
4. Menyuruh pengguna menginput barang yang ingin dibeli dengan membuat variabel dan juga input yaitu input_barang = input("Tuliskan barang yang ingin kamu pilih: ")
5. Menampilkan harga barang:
    Buku = 5000
    Pulpen = 3000
    Pensil = 2000

6. Menyuruh pengguna menginput berapa banyak/kuantitas yang pengguna inginkan dengan membuat variabel kuantitas_buku = int(input(f"Tuliskan berapa banyak buku yang ingin {nama} beli: "))

7. Menghitung harga tanpa diskon dengan variabel 
    harga_buku = 5000 * (kuantitas_buku)
    harga_pulpen = 3000 * (kuantitas_pulpen)
    harga_pensil = 2000 * (kuantitas_pensil)

8. Menghitung harga diskon bila memesan lebih dari 10 jumlah barang dengan variabel
    harga_akhir_buku = int((harga_buku) * 0.80)
    harga_akhir_pulpen = int((harga_pulpen) * 0.80)
    harga_akhir_pensil = int((harga_pensil) * 0.80)
variabel harga barang dikali dengan 0.80 artinya mendapat diskon 20%

9. Menghitung harga diskon bila memesan antara 5 hingga 10 jumlah barang dengan membuat variabel
    harga_akhir_buku = int((harga_buku) * 0.90)
    harga_akhir_pulpen = int((harga_pulpen) * 0.90)
    harga_akhir_pensil = int((harga_pensil) * 0.90)
variabel harga barang dikali dengan 0.90 artinya mendapat diskon 10%

10. Menghitung harga diskon bila memesan kurang dari 5 jumlah barang
Bila memesan kurang dari 5 jumlah barang, maka tidak akan mendapat diskon.

11. Membuat pernyataan konfirmasi dengan membuat baris/line print(f"\nKonfirmasi: Pelanggan {nama} memesan {kuantitas_buku} buku\nDengan total harga {harga_akhir_buku}")
12. Membuat program konfirmasi pembayaran:
confirm = input("Apakah ingin melanjutkan pembayaran [y/n]: ")
        if confirm == "y":
            print("\nSilahkan kirim uang ke rek 0512xxx xxxx an/ Ayubi Fathan (BRI)")
            print("Terimakasih selamat datang kembali")
            exit()
        else:
            print("\nTolong konfirmasi ulang")
            confirm2 = input("Apakah ingin melanjutkan pembayaran [y/n]: ")
            if confirm2 == "y":
                print("\nSilahkan kirim uang ke rek 0512xxx xxxx an/ Ayubi Fathan (BRI)")
                print("Terimakasih selamat datang kembali")
                exit()
            else:
                print("\nSystem Error")
                exit()
