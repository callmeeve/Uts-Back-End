transportasi = ["Mobil","Motor"]
barang = ["Tenda","Sleeping Bag","Kompor Portable"]
properti = ["Kost","Homestay","Hotel"]
keranjang = []

print('Selamat Datang di Nyewo\nSilahkan pilih jenis penyewaan yang ada dibawah ini :')
while True:
    jenispenyewaan = input("1. Transportasi \n2. Barang \n3. Properti \nMasukkan jenis penyewaan [1-3]: ")
    if jenispenyewaan == "1":
        print("Anda memilih Jenis Penyewaan 1 yaitu Transportasi")
        print("Pilih Transportasi anda :")
        while True:
            for ii in range(0, len(transportasi)):
                print(f'{ii + 1}. {transportasi[ii]}')
            list_transportasi = int(input('Pilih Penyewaan 1-2: '))
            if list_transportasi == 1:
                keranjang.append(transportasi[0])
                print('==== list keranjang ====')
                for a in range(0, len(keranjang)):
                    print(f'{a +1}. {keranjang[a]} x1')
                break
            elif list_transportasi == 2:
                keranjang.append(transportasi[1])
                print('==== list keranjang ====')
                for a in range(0, len(keranjang)):
                    print(f'{a +1}. {keranjang[a]} x1')
                break
            else:
                print("Silahkan masukkan jenis penyewaan yang tersedia")
                continue
    elif jenispenyewaan == "2":
        print("Anda memilih Jenis Penyewaan 2 yaitu Barang")
        print("Pilih Barang anda :")
        while True:
            for ii in range(0, len(barang)):
                print(f'{ii + 1}. {barang[ii]}')
            list_barang = int(input('Pilih Penyewaan 1-3: '))
            if list_barang == 1:
                keranjang.append(barang[0])
                print('==== list keranjang ====')
                for a in range(0, len(keranjang)):
                    print(f'{a +1}. {keranjang[a]} x1')
                break
            elif list_barang == 2:
                keranjang.append(barang[1])
                print('==== list keranjang ====')
                for a in range(0, len(keranjang)):
                    print(f'{a +1}. {keranjang[a]} x1')
                break
            elif list_barang == 3:
                keranjang.append(barang[2])
                print('==== list keranjang ====')
                for a in range(0, len(keranjang)):
                    print(f'{a +1}. {keranjang[a]} x1')
                break
            else:
                print("Silahkan masukkan jenis penyewaan yang tersedia")
                continue
    elif jenispenyewaan == "3":
        print("Anda memilih Jenis Penyewaan 3 yaitu Properti")
        print("Pilih Properti anda :")
        while True:
            for ii in range(0, len(properti)):
                print(f'{ii + 1}. {properti[ii]}')
            list_properti = int(input('Pilih Menu 1-3: '))
            if list_properti == 1:
                keranjang.append(properti[0])
                print('==== list keranjang ====')
                for a in range(0, len(keranjang)):
                    print(f'{a +1}. {keranjang[a]} x1')
                break
            elif list_properti == 2:
                keranjang.append(properti[1])
                print('==== list keranjang ====')
                for a in range(0, len(keranjang)):
                    print(f'{a +1}. {keranjang[a]} x1')
                break
            elif list_properti == 3:
                keranjang.append(properti[2])
                print('==== list keranjang ====')
                for a in range(0, len(keranjang)):
                    print(f'{a +1}. {keranjang[a]} x1')
                break
            else:
                print("Silahkan masukkan jenis penyewaan yang tersedia")
                continue
    else:
        print("Jenis Penyewaan tidak ada")
        continue
    validasi_menu = input('Ada yang ingin ditambahkan[Y/N]? ')
    if validasi_menu == "Y" or validasi_menu == "y":
        continue
    else:
        print("Terima kasih, pesanan anda akan segera ditangani")
        break