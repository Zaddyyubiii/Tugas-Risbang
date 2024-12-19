nama = input("Tuliskan nama kamu: ")

print(f'''------------------------------------
Selamat datang {nama} di Ayubi Store
------------------------------------''')

print('''Kami menjual beberapa barang seperti
Buku, Pulpen, Pensil''')

#Daftar barang
barang1 = ["Buku","Pulpen","Pensil"]
barang2 = ["buku","pulpen","pensil"]

#Menginput barang buku
input_barang = input("Tuliskan barang yang ingin kamu pilih: ")
if input_barang == barang1[0] or input_barang == barang2[0]:
    print("\nHarga buku satunya ialah 5000")
    kuantitas_buku = int(input(f"Tuliskan berapa banyak buku yang ingin {nama} beli: "))
    harga_buku = 5000 * (kuantitas_buku)
    print(f"\nTotal harga adalah {harga_buku}")
    #Untuk kuantitas buku lebih dari 10
    if kuantitas_buku > 10:
        harga_akhir_buku = int((harga_buku) * 0.80)
        print(f"Selamat kamu mendapat diskon 20%\nSehingga total harga menjadi {harga_akhir_buku}")
        print(f"\nKonfirmasi: Pelanggan {nama} memesan {kuantitas_buku} buku\nDengan total harga {harga_akhir_buku}")
        
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
    #Untuk kuantitas buku 5-10            
    elif kuantitas_buku >= 5 and kuantitas_buku <= 10:
        harga_akhir_buku = int((harga_buku) * 0.90)
        print(f"Selamat kamu mendapat diskon 10%\nSehingga total harga menajdi {harga_akhir_buku}")
        print(f"\nKonfirmasi: Pelanggan {nama} memesan {kuantitas_buku} buku\nDengan total harga {harga_akhir_buku}")
        
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
    #Untuk kuantitas buku kurang dari 5           
    elif kuantitas_buku < 5:
        harga_akhir_buku = int((harga_buku) * 1)
        print(f"Maaf kamu tidak mendapat diskon\nSehingga total harga tetap {harga_akhir_buku}")
        print(f"\nKonfirmasi: Pelanggan {nama} memesan {kuantitas_buku} buku\nDengan total harga {harga_akhir_buku}")
        
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
#Menginput barang pulpen                
elif input_barang == barang1[1] or input_barang == barang2[1]:
    print("\nHarga pulpen satunya ialah 3000")
    kuantitas_pulpen = int(input(f"Tuliskan berapa banyak pulpen yang ingin {nama} beli: "))
    harga_pulpen = 3000 * (kuantitas_pulpen)
    print(f"\nTotal harga adalah {harga_pulpen}")
    #Untuk kuantitas pulpen lebih dari 10
    if kuantitas_pulpen > 10:
        harga_akhir_pulpen = int((harga_pulpen) * 0.80)
        print(f"Selamat kamu mendapat diskon 20%\nSehingga total harga menjadi {harga_akhir_pulpen}")
        print(f"\nKonfirmasi: Pelanggan {nama} memesan {kuantitas_pulpen} pulpen\nDengan total harga {harga_akhir_pulpen}")
        
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
    #Untuk kuantitas pulpen 5-10            
    elif kuantitas_pulpen >= 5 and kuantitas_pulpen <= 10:
        harga_akhir_pulpen = int((harga_pulpen) * 0.90)
        print(f"Selamat kamu mendapat diskon 10%\nSehingga total harga menjadi {harga_akhir_pulpen}")
        print(f"\nKonfirmasi: Pelanggan {nama} memesan {kuantitas_pulpen} pulpen\nDengan total harga {harga_akhir_pulpen}")
        
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
    #Untuk kuantitas pulpen kurang dari 5            
    elif kuantitas_pulpen < 5:
        harga_akhir_pulpen = int((harga_pulpen) * 1)
        print(f"Maaf kamu tidak mendapat diskon\nSehingga total harga tetap {harga_akhir_pulpen}")
        print(f"\nKonfirmasi: Pelanggan {nama} memesan {kuantitas_pulpen} pulpen\nDengan total harga {harga_akhir_pulpen}")
        
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
#Menginput barang pensil                
elif input_barang == barang1[2] or input_barang == barang2[2]:
    print("\nHarga pensil satunya ialah 2000")
    kuantitas_pensil = int(input(f"Tuliskan berapa banyak pensil yang ingin {nama} beli: "))
    harga_pensil = 2000 * (kuantitas_pensil)
    print(f"\nTotal harga adalah {harga_pensil}")
    #Untuk kuantitas pensil lebih dari 10
    if kuantitas_pensil > 10:
        harga_akhir_pensil = int((harga_pensil) * 0.80)
        print(f"Selamat kamu mendapat diskon 20%\nSehingga total harga menjadi {harga_akhir_pensil}")
        print(f"\nKonfirmasi: Pelanggan {nama} memesan {kuantitas_pensil} pulpen\nDengan total harga {harga_akhir_pensil}")
        
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
    #Untuk kuantitas pensil 5-10            
    elif kuantitas_pensil >= 5 and kuantitas_pensil <= 10:
        harga_akhir_pensil = int((harga_pensil) * 0.90)
        print(f"Selamat kamu mendapat diskon 10%\nSehingga total harga menjadi {harga_akhir_pensil}")
        print(f"\nKonfirmasi: Pelanggan {nama} memesan {kuantitas_pensil} pensil\nDengan total harga {harga_akhir_pensil}")
        
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
    #Untuk kuantitas pensil kurang dari 5            
    elif kuantitas_pensil < 5:
        harga_akhir_pensil = int((harga_pensil) * 1)
        print(f"Maaf kamu tidak mendapat diskon\nSehingga total harga tetap {harga_akhir_pensil}")
        print(f"\nKonfirmasi: Pelanggan {nama} memesan {kuantitas_pensil} pensil\nDengan total harga {harga_akhir_pensil}")
        
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
                
#Menginput data barang yang salah                    
else: 
    print("\nMaaf barang tersebut tidak kami jual")
    exit()

        
        
        
                    
                    
        

