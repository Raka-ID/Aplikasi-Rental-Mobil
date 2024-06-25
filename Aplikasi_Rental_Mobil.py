# Menu Aplikasi Rental Kendaraan

# Define Variable
Rental = {
    'Toyota'  : {
                 'Avanza':   {
                                'D 1000 TA': {'Tahun': '2015', 'Price':  900000},
                                'D 1001 TA': {'Tahun': '2023', 'Price': 1100000}
                             },
                 'Innova':   {
                                'D 1000 TI': {'Tahun': '2016', 'Price': 1300000}
                             },
                 'Rush':     {
                                'D 1000 TR': {'Tahun': '2016', 'Price':  800000}
                             }
                },
    'Daihatsu': {
                 'Xenia':    {
                                'D 1000 DX': {'Tahun': '2013', 'Price':  750000},
                                'D 1001 DX': {'Tahun': '2023', 'Price':  675000}},
                 'Gran Max': {
                                'D 1000 DG': {'Tahun': '2015', 'Price':  400000},
                                'D 1001 DG': {'Tahun': '2019', 'Price':  525000}
                    }
                },
    'Honda':    {
                 'Mobilio':  {
                                'D 1000 HM': {'Tahun': '2016', 'Price':  350000},
                                'D 1001 HM': {'Tahun': '2023', 'Price':  465000}},
                 'CR-V':     {
                                'D 1000 HV': {'Tahun': '2015', 'Price':  850000},
                                'D 1001 HV': {'Tahun': '2020', 'Price':  950000}
                             }
                },
    'Suzuki':   {
                 'Ertiga':   {
                                'D 1000 SE': {'Tahun': '2015', 'Price': 1050000},
                                'D 1001 SE': {'Tahun': '2022', 'Price': 1300000}},
                 'APV':      {
                                'D 1000 SA': {'Tahun': '2009', 'Price':  300000},
                                'D 1001 SA': {'Tahun': '2016', 'Price':  650000}
                             }
                },
    'Mitsubishi':{
                 'FE 71 BC': {
                                'D 1000 MF': {'Tahun': '2015', 'Price': 2500000}},
                 'FE 84G BC':{
                                'D 1000 MG': {'Tahun': '2018', 'Price': 3000000}
                             }
                }
         }

# Define Fungsi
def menu_utama():
    print('''\t   ----MENU UTAMA----
        1. Daftar Rental Kendaraan
        2. Tambah Kendaraan
        3. Perbarui Detail Kendaraan
        4. Hapus Kendaraan
        5. Keluar Aplikasi\n''')

def format_nopol(nopol):
    format_nopol = None
    if nopol[1].isspace():
        if nopol[6].isspace():
            format_nopol = nopol
        elif nopol[6].isalpha():
            format_nopol = nopol.replace(nopol[6:], ' ' + nopol[6:])
        else:
            print('Tolong masukkan format Nomor Polisi kendaraan sesuai standar penulisan.')
    elif nopol[1].isdigit():
        if nopol[5].isspace():
            format_nopol = nopol.replace(nopol[1:], ' ' + nopol[1:])
        elif nopol[5].isalpha():
            format_1 = nopol.replace(nopol[5:], ' ' + nopol[5:])
            format_nopol = format_1.replace(format_1[1:], ' ' + format_1[1:])
        else:
            print('Tolong masukkan format Nomor Polisi kendaraan sesuai standar penulisan.')
    elif nopol[1].isalpha():
        if nopol[2].isspace():
            if nopol[7].isspace():
                format_nopol = nopol
            elif nopol[7].isalpha():
                format_nopol = nopol.replace(nopol[7:], ' ' + nopol[7:])
            else:
                print('Tolong masukkan format Nomor Polisi kendaraan sesuai standar penulisan.')
        elif nopol[2].isdigit():
            if nopol[6].isspace():
                format_nopol = nopol.replace(nopol[2:], ' ' + nopol[2:])
            elif nopol[6].isalpha():
                format_1 = nopol.replace(nopol[6:], ' ' + nopol[6:])
                format_nopol = format_1.replace(format_1[2:], ' ' + format_1[2:])
            else:
                print('Tolong masukkan format Nomor Polisi kendaraan sesuai standar penulisan.')
    else:
        print('Tolong masukkan format Nomor Polisi kendaraan sesuai standar penulisan.')
    return format_nopol

# 1. Fungsi Submenu Read
def submenu_read():
    print('''\t==== Daftar Rental Kendaraan ====
        1. Daftar Seluruh Kendaraan
        2. No. Polisi Kendaraan Tertentu
        3. Daftar Merk Kendaraan Tertentu
        4. Kembali ke Menu Utama\n''')

def daftar_column():
    print('-----------------------------Daftar Kendaraan----------------------------\n')
    print(' Merk\t\t| Model\t\t| No. Polisi\t| Tahun\t| Harga Sewa (Rp)\t')
    print('----------------+---------------+---------------+-------+----------------')

def seluruh_daftar(suatu_dictionary):
    sortir = dict(sorted(suatu_dictionary.items()))
    for merk, models in sortir.items():
        for model, Nopol in models.items():
            for nopol, details in Nopol.items():
                year = details['Tahun']
                price = details['Price']
                print(f' {merk}   \t| {model}    \t| {nopol}\t| {year}\t| {price:,}\t')
    print()

def kendaraan_nopol(suatu_nopol):
    cari = False
    for merk, models in Rental.items():
        for model, Nopol in models.items():
            for nopol, details in Nopol.items():
                if nopol == suatu_nopol:
                    year = details['Tahun']
                    price = details['Price']
                    daftar_column()
                    print(f' {merk}   \t| {model}    \t| {nopol}\t| {year}\t| {price:,}\t')
                    print()
                    cari = True
                    break       # Menghentikan Loop paling dalam
            if cari:
                break       # Menghentikan Loop di tengah
        if cari:
            break       # Menghentikan Loop paling luar
    if not cari:
        print(f"Kendaraan dengan nomor polisi \'{input_mentah}\' tidak ditemukan.\n")

def filter_merk(suatu_merk):
    if suatu_merk in Rental.keys():
        daftar_column()
        for merk, models in Rental.items():
            if merk == suatu_merk:      # Dibatasi pada inputan(merk) saja
                for model, Nopol in models.items():
                    for nopol, details in Nopol.items():
                        year = details['Tahun']
                        price = details['Price']
                        print(f' {merk}   \t| {model}    \t| {nopol}\t| {year}\t| {price:,}\t')
        print()
    else:
        print(f'Model kendaraan \'{suatu_merk}\' tidak ada pada daftar kendaraan\n')

# 2. Fungsi Create
def submenu_create():
    print('''\t==== Menambahkan Daftar Kendaraan Baru ====
        1. Menambahkan 1 Kendaraan
        2. Menambahkan Kendaraan Lebih dari 1
        3. Kembali ke Menu Utama\n''')

def tambah_kendaraan(suatu_nopol):
    # Mengecek Duplikasi
    cek = False
    for merk, models in Rental.items():
        for model, Nopol in models.items():
            for nopol, details in Nopol.items():
                if nopol == suatu_nopol:
                    print(f'Kendaraan dengan nomor polisi \'{suatu_nopol}\' sudah ada dalam daftar')
                    print()
                    cek = True
                    break
            if cek:
                break
        if cek:
            break

    # Menambahkan Kendaraan Baru
    if not cek:
        print(f"Kendaraan dengan nomor polisi \'{suatu_nopol}\' belum ada di dalam daftar")

        # Input Merk
        while True:
            input_merk = input('Masukkan merk kendaraan: ').capitalize()
            # Batasan (Merk tidak boleh angka)
            if input_merk.isdigit():
                print('Merk yang anda masukkan berupa angka.\n')
            elif input_merk.isalnum():
                if input_merk.isalpha():
                    break
                else:
                    print('Merk yang anda masukkan mengandung angka.\n')
            else:
                break
        
        # Input Model
        input_model = input('Masukkan model kendaraan: ')

        # Input Tahun Produksi
        while True:
            try:
                input_tahun = int(input('Masukkan tahun produksi kendaraan dalam angka: '))
                if input_tahun > 0:
                    break
                else:
                    print('Tolong Masukkan dalam bilangan bulat positif.\n')
            except:
                print('Tolong masukkan dalam bentuk angka.\n')
        
        # Input Harga Sewa
        while True:
            try:
                input_price = int(input('Masukkan harga sewa kendaraan dalam angka: '))
                if input_price > 0:
                    break
                else:
                    print('Tolong Masukkan dalam bilangan bulat positif.\n')
            except:
                print('Tolong masukkan dalam bentuk angka')
        print()

        while True:
            print(f'Merk\t\t: {input_merk}\nModel \t\t: {input_model}\nNo. Polisi\t: {suatu_nopol}\nTahun produksi\t: {input_tahun}\nHarga sewa (Rp)\t: {input_price:,}')
            konfirmasi = input('Bila data di atas sudah benar, tambahkan ke dalam daftar kendaraan (y/n)?: ').lower()
            print()

            # Konfirmasi bila 'y' maka data disimpan
            if konfirmasi == 'y':
                if input_merk in Rental:    # Cek bilamana sudah ada merk yang sama dengan key pada dictionary
                    if input_model in Rental[input_merk]:    # Cek bilamana sudah ada model yang sama dengan key di dictionary
                        Rental[input_merk][input_model].update({suatu_nopol: {'Tahun': input_tahun, 'Price': input_price}}) # input kendaraan baru (merk dan model sudah ada)
                        print('Data berhasil disimpan\n')
                        break
                    else:
                        Rental[input_merk][input_model] = {suatu_nopol: {'Tahun': input_tahun, 'Price': input_price}} # input kendaraan baru (merk sudah ada)
                        print('Data berhasil disimpan\n')
                        break
                else:
                    Rental[input_merk] = {input_model: {suatu_nopol: {'Tahun': input_tahun, 'Price': input_price}}} # input kendaraan baru 
                    print('Data BERHASIL disimpan\n')
                    break

            # Konfirmasi bila 'n' maka data diabaikan
            elif konfirmasi == 'n':
                print('Menambah kendaraan baru DIBATALKAN\n')
                break   # Kembali ke Menu Utama

            # bila input selain y/n
            else:
                print('Invalid input. Tolong masukkan pilihan yang sesuai')

# 3. Fungsi Update
def submenu_update():
    print('''\t====Perbarui Data Kendaraan====
        1. Perbarui Data Kendaraan Berdasarkan No. Polisi
        2. Kembali ke Menu Utama\n''')

def perbarui_kendaraan(suatu_nopol):
    # (suatu_nopol = input_nopol --> Sebagai Primary Key)

    # Mengecek Primary Key Dalam Data Dictionary
    cek = False
    for merk, models in Rental.items():
        for model, Nopol in models.items():
            for nopol, details in Nopol.items():
                if nopol == suatu_nopol:

                    # Data Ditemukan
                    year, price = details['Tahun'], details['Price']
                    print(f'Kendaraan dengan No. Polisi \'{suatu_nopol}\' ada di dalam daftar kendaraan\n')
                    daftar_column()
                    print(f' {merk}   \t| {model}    \t| {nopol}\t| {year}\t| {price:,}\t\n')   # Menampilkan detail kendaraan dari suatu primary key

                    # Konfirmasi Lanjut Untuk Memperbarui Data
                    while True:
                        menu_3_1 = input('Lanjut perbarui data kendaraan di atas (y/n): ').lower()
                        print()

                        # 'Y' untuk lanjut
                        if menu_3_1 == 'y':
                            print('\t====Pilihan Kolom====\n\t1. Merk\n\t2. Model\n\t3. Nopol (No. Polisi)\n\t4. Tahun (Produksi)\n\t5. Harga (Sewa)\n')
                            input_column = input('Masukkan kolom yang datanya ingin diperbarui (1-5): ').lower()
                            print()

                            # Perbaruan Data pada Kolom Merk
                            if input_column == '1' or input_column == 'merk':
                                while True:
                                    input_merk = input('Masukkan merk kendaraan: ').capitalize()
                                    # Batasan (Merk tidak boleh angka)
                                    if input_merk.isdigit():
                                        print('Merk yang anda masukkan berupa angka.\n')
                                    elif input_merk.isalnum():
                                        if input_merk.isalpha():
                                            break
                                        else:
                                            print('Merk yang anda masukkan mengandung angka.\n')
                                    else:
                                        break

                                while True:     # Menghindari inputan selain 'y' atau 'n'
                                    print(f'Kolom \'Merk\' kendaraan dengan No. Polisi \'{suatu_nopol}\' akan diperbarui menjadi \'{input_merk}\'')
                                    yn = input('Konfirmasi (y/n): ').lower()
                                    print()
                                    if yn == 'y':
                                        Rental[merk][model].pop(suatu_nopol)
                                        Rental[input_merk].update({model: {suatu_nopol:{'Tahun': year, 'Price': price}}})
                                        print('BERHASIL perbarui data kendaraan.\n')
                                        break
                                    elif yn == 'n':
                                        print('BATAL memperbarui data kendaraan.\n')
                                        break
                                    else:
                                        price('Invalid input. Tolong masukkan pilihan yang sesuai\n')

                            # Perbaruan Data pada Kolom Model
                            elif input_column == '2' or input_column == 'model':
                                while True:
                                    input_model = input('Masukkan model kedaraan: ')
                                    print(f'Kolom \'Model\' kendaraan dengan No. Polisi \'{suatu_nopol}\' akan diperbarui menjadi \'{input_model}\'')
                                    yn = input('Konfirmasi (y/n): ').lower()
                                    print()
                                    if yn == 'y':
                                        input_model_2 = input_model.capitalize()
                                        Rental[merk][model].pop(suatu_nopol)
                                        Rental[merk][input_model_2] = {suatu_nopol:{'Tahun': year, 'Price': price}}
                                        print('BERHASIL perbarui data kendaraan.\n')
                                        break
                                    elif yn == 'n':
                                        print('BATAL memperbarui data kendaraan.\n')
                                        break
                                    else:
                                        price('Invalid input. Tolong masukkan pilihan yang sesuai\n')

                            # Perbaruan Data pada Kolom No. Polisi
                            elif input_column == '3' or input_column == 'nopol' or input_column == 'no. polisi':
                                # Cek penulisan nomor polisi
                                while True:
                                    input_mentah = input('Masukkan nomor polisi kendaraan baru: ').upper()
                                    print()
                                    if len(input_mentah) < 7 or input_mentah[0].isdigit():
                                        print('Tolong masukkan nomor polisi kendaraan sesuai standar penulisan.')
                                        print('Note: nomor polisi custom tidak dapat ditambahkan.\n')
                                    else:
                                        input_nopol = format_nopol(input_mentah)
                                        if input_nopol == None:
                                            print('Note: nomor polisi custom tidak dapat ditambahkan.\n')
                                            break
                                        else:
                                            break
                                # Cek bila ada duplikat pada No. Polisi (harus unik)
                                cek = False
                                for merk, models in Rental.items():
                                    for model, Nopol in models.items():
                                        for nopol, details in Nopol.items():
                                            if nopol == input_nopol:
                                                print(f'Kendaraan dengan nomor polisi \'{input_nopol}\' sudah ada dalam daftar\n')
                                                cek = True
                                                break
                                        if cek:
                                            break
                                    if cek:
                                        break

                                # Menambahkan Kendaraan Baru pada Kolom Polisi
                                if not cek:
                                    while True:
                                        print(f'Kolom \'No. Polisi\' kendaraan dengan No. Polisi \'{suatu_nopol}\' akan diperbarui menjadi \'{input_nopol}\'')
                                        yn = input('Konfirmasi (y/n): ').lower()
                                        print()
                                        if yn == 'y':
                                            cek = False
                                            for merk, models in Rental.items():
                                                for model, Nopol in models.items():
                                                    for nopol, details in Nopol.items():
                                                        if nopol == suatu_nopol:
                                                            Rental[merk][model].pop(suatu_nopol)
                                                            Rental[merk][model].update({input_nopol:{'Tahun': year, 'Price': price}})
                                                            print('BERHASIL perbarui data kendaraan.\n')
                                                            cek = True
                                                            break
                                                    if cek:
                                                        break
                                                if cek:
                                                    break
                                            break
                                        elif yn == 'n':
                                            print('BATAL pembaruan data kendaraan.\n')
                                            break
                                        else:
                                            print('Invalid input. Tolong masukkan pilihan yang sesuai\n')

                            # Perbaruan Data pada Kolom Tahun
                            elif input_column == '4' or input_column == 'tahun' or input_column == 'tahun produksi' or input_column == 'produksi':
                                while True:
                                    
                                    # Input Tahun harus bilangan bulat positif
                                    while True:
                                        try:
                                            input_tahun = int(input('Masukkan tahun produksi kendaraan dalam angka: '))
                                            if input_tahun > 0:
                                                break
                                            else:
                                                print('Tolong Masukkan dalam bilangan bulat positif.\n')
                                        except:
                                            print('Tolong masukkan dalam bentuk angka.\n')

                                    print(f'Kolom \'Tahun\' kendaraan dengan No. Polisi \'{suatu_nopol}\' akan diperbarui menjadi \'{input_tahun}\'')
                                    yn = input('Konfirmasi (y/n): ').lower()
                                    print()
                                    if yn == 'y':
                                        Rental[merk][model][suatu_nopol].update({'Tahun': input_tahun})
                                        print('BERHASIL perbarui data kendaraan.')
                                        break
                                    elif yn == 'n':
                                        print('BATAL memperbarui data kendaraan.\n')
                                        break
                                    else:
                                        price('Invalid input. Tolong masukkan pilihan yang sesuai\n')

                            # Perbaruan Data pada Kolom Harga Sewa (Price)
                            elif input_column == '5' or input_column == 'harga' or input_column == 'harga sewa' or input_column == 'sewa':
                                while True:

                                    # Input Harga Sewa harus bilangan bulat positif
                                    while True:
                                        try:
                                            input_price = int(input('Masukkan harga sewa kendaraan dalam angka: '))
                                            if input_price > 0:
                                                break
                                            else:
                                                print('Tolong Masukkan dalam bilangan bulat positif.\n')
                                        except:
                                            print('Tolong masukkan dalam bentuk angka')

                                    print(f'Kolom \'Harga Sewa\' kendaraan dengan No. Polisi \'{suatu_nopol}\' akan diperbarui menjadi \'{input_price}\'')
                                    yn = input('Konfirmasi (y/n): ').lower()
                                    print()
                                    if yn == 'y':
                                        Rental[merk][model][suatu_nopol].update({'Price': input_price})
                                        print('BERHASIL perbarui data kendaraan.\n')
                                        break
                                    elif yn == 'n':
                                        break
                                    else:
                                        price('Invalid input. Tolong masukkan pilihan yang sesuai\n')

                            # Invalid Input (pilihan di luar kolom yang tersedia)
                            else:
                                print('Kolom yang anda masukkan tidak ada di dalam daftar/invalid\n')
                            break

                        # 'N' Untuk Batal Memperbarui Data
                        elif menu_3_1 == 'n':
                            print('BATAL memperbarui data kendaraan.\n')
                            break
                        else:
                            print('Invalid input. Tolong masukkan pilihan yang sesuai\n')
                    cek = True  # Iterasi dihentikan untuk loop selanjutnya
                    break       # Iterasi dihentikan
            if cek:
                break
        if cek:
            break

    # Primary Key Pada Data Dictionary Tidak Ditemukan
    if not cek:
        print(f"Kendaraan dengan nomor polisi \'{suatu_nopol}\' tidak ditemukan.\n")

# 4. Fungsi Delete
def submenu_delete():
    print('''\t====Hapus Data Kendaraan====
        1. Hapus Data Kendaraan Berdasarkan No. Polisi
        2. Kembali ke Menu Utama\n''')

def hapus_kendaraan(suatu_nopol):
    cek = False
    for merk, models in Rental.items():
        for model, Nopol in models.items():
            for nopol, details in Nopol.items():
                if nopol == suatu_nopol:

                    # Data Ditemukan
                    year, price = details['Tahun'], details['Price']
                    print(f'Kendaraan dengan No. Polisi \'{suatu_nopol}\' ada di dalam daftar kendaraan\n')
                    daftar_column()
                    print(f' {merk}   \t| {model}    \t| {nopol}\t| {year}\t| {price:,}\t\n')   # Menampilkan detail kendaraan dari suatu primary key

                    # Konfirmasi Lanjut Untuk Menghapus Data
                    while True:
                        menu_4_1 = input('Lanjut hapus data kendaraan di atas (y/n): ').lower()
                        print()

                        # 'Y' untuk lanjut
                        if menu_4_1 == 'y':
                            print(f'Kendaraan dengan No. Polisi {input_nopol} merk {merk} model {model} BERHASIL DIHAPUS\n')
                            Rental[merk][model].pop(suatu_nopol)
                            break

                        # 'N' Untuk Batal Memperbarui Data
                        elif menu_4_1 == 'n':
                            print(f'Kendaraan dengan No. Polisi \'{input_nopol}\' merk \'{merk}\' model \'{model}\' BATAL DIHAPUS\n')
                            break

                        # Invalid input selain y/n
                        else:
                            print('Invalid input. Tolong masukkan pilihan yang sesuai\n')
                    cek = True  # Iterasi dihentikan untuk loop selanjutnya
                    break       # Iterasi dihentikan
            if cek:
                break
        if cek:
            break

    # Primary Key Pada Data Dictionary Tidak Ditemukan
    if not cek:
        print(f"Kendaraan dengan nomor polisi \'{suatu_nopol}\' tidak ditemukan.\n")

#=============================================================================================================================================

print('========APLIKASI PENYEWAAN KENDARAAN========\n')     # Judul Utama

# Menu Utama
while True:
    menu_utama()
    menu = input('Silakan tentukan pilihan (1-5): ')
    print()

#=============================================================================================================================================

# Fitur Read
    if menu == '1':
        while True:
            submenu_read()
            menu_1 = input('Silakan Pilih Sub-Menu Daftar Rental Kendaraan (1-4): ')
            print()

            # Submenu 1 (Menampilkan Daftar Seluruh Kendaraan)
            if menu_1 == '1':

                # Bila tidak ada daftar kendaraan
                if len(Rental.keys()) == 0:
                    print('Tidak ada data kendaraan. Tambahkan kendaraan baru.')

                # Menampilkan seluruh daftar kendaraan
                else:
                    daftar_column()
                    seluruh_daftar(Rental)

            # Submenu 2 (Kendaraan Tertentu Berdasarkan No. Polisi [Primary Key])
            elif menu_1 == '2':
                while True:
                    input_mentah = input('Masukkan Nomor Polisi kendaraan yang hendak ditampilkan: ').upper()
                    print()
                    if len(input_mentah) < 7 or input_mentah[0].isdigit():
                        print('Tolong masukkan nomor polisi kendaraan sesuai standar penulisan.')
                    else:
                        input_nopol = format_nopol(input_mentah)
                        kendaraan_nopol(input_nopol)
                        break

        #------------------------------------------------------------------------------
            # Submenu 3 (Filter Berdasarkan Merk Kendaraan)
            elif menu_1 == '3':
                input_merk = input('Masukkan merk kendaraan yang hendak ditampilkan: ').capitalize()
                print()
                filter_merk(input_merk)

            # Ke Menu Utama
            elif menu_1 == '4':
                break

            # Invalid Input Submenu Read
            else:
                print('Invalid input. Tolong masukkan pilihan yang sesuai\n')

#=============================================================================================================================================

# Fitur Create
    elif menu =='2':
        while True:
            submenu_create()
            menu_2 = input('Silakan Pilih Sub-Menu Menambahkan Daftar Rental Kendaraan (1-3): ')
            print()

            # Submenu 1 (Menambahkan 1 Kendaraan)
            if menu_2 == '1':
                while True:
                    input_mentah = input('Masukkan Nomor Polisi kendaraan yang hendak ditambahkan: ').upper()
                    print()
                    if len(input_mentah) < 7 or input_mentah[0].isdigit():
                        print('Tolong masukkan nomor polisi kendaraan sesuai standar penulisan.')
                        print('Note: nomor polisi custom tidak dapat ditambahkan.\n')
                    else:
                        input_nopol = format_nopol(input_mentah)
                        if input_nopol == None:
                            print('Note: nomor polisi custom tidak dapat ditambahkan.\n')
                            break
                        else:
                            tambah_kendaraan(input_nopol)
                            break

            # Submenu 2 (Menambahkan Kendaraan Lebih Dari 1 Sekaligus)
            elif menu_2 == '2':

                try:    # Memisahkan input selain angka
                    menu_2_2 = int(input('Berapa banyak kendaraan yang ingin dimasukkan: '))
                    print()
                    if menu_2_2 > 0:
                        for i in range(1, menu_2_2 + 1):
                            while True:
                                input_mentah = input(f'Masukkan No. Polisi kendaraan ke-{i}: ').upper()
                                print()
                                if len(input_mentah) < 7 or input_mentah[0].isdigit():
                                    print('Tolong masukkan nomor polisi kendaraan sesuai standar penulisan.')
                                    print('Note: nomor polisi custom tidak dapat ditambahkan.\n')
                                else:
                                    input_nopol = format_nopol(input_mentah)
                                    if input_nopol == None:
                                        print('Note: nomor polisi custom tidak dapat ditambahkan.\n')
                                        break
                                    else:
                                        tambah_kendaraan(input_nopol)
                                        break
                except:
                    print('Invalid input. Input yang dimasukkan bukan berupa bilangan bulat positif\n')

            # Ke Menu Utama
            elif menu_2 == '3':
                break

            # Invalid Input Submenu Create
            else:
                print('Invalid input. Tolong masukkan pilihan yang sesuai\n')

#=============================================================================================================================================

# Fitur Update
    elif menu =='3':
        while True:
            submenu_update()
            menu_3 = input('Silakan Pilih Sub-menu Perbarui Data Kendaraan (1-2): ')
            print()

            # Submenu 1 (Perbarui Data Kendaraan)
            if menu_3 == '1':

                # Input Primary Key
                while True:
                    input_mentah = input('Masukkan Nomor Polisi kendaraan yang hendak diperbarui: ').upper()
                    print()
                    if len(input_mentah) < 7 or input_mentah[0].isdigit():
                        print('Tolong masukkan nomor polisi kendaraan sesuai standar penulisan.')
                        print('Note: nomor polisi custom tidak dapat ditambahkan.\n')
                    else:
                        input_nopol = format_nopol(input_mentah)
                        if input_nopol == None:
                            print('Note: nomor polisi custom tidak dapat ditambahkan.\n')
                            break
                        else:
                            perbarui_kendaraan(input_nopol)
                            break

            # Submenu 2 (Kembali ke Menu Utama)
            elif menu_3 == '2':
                break

            # Invalid input Submenu Update
            else:
                print('Invalid input. Tolong masukkan pilihan yang sesuai\n')

#=============================================================================================================================================

# Fitur Delete
    elif menu == '4':
        while True:
            submenu_delete()
            menu_4 = input('Silakan Pilih Sub-Menu Hapus Daftar Rental Kendaraan (1-2): ')
            print()

            # Submenu 1 (Hapus Data Kendaraan)
            if menu_4 == '1':
                while True:
                    input_mentah = input('Masukkan Nomor Polisi kendaraan yang hendak dihapus: ').upper()
                    print()
                    if len(input_mentah) < 7 or input_mentah[0].isdigit():
                        print('Tolong masukkan nomor polisi kendaraan sesuai standar penulisan.')
                        print('Note: nomor polisi custom tidak ada di dalam daftar.\n')
                    else:
                        input_nopol = format_nopol(input_mentah)
                        print()
                        if input_nopol == None:
                            print('Kendaraan yang anda cari tidak ada di dalam daftar kendaraan.\n')
                            break
                        else:
                            hapus_kendaraan(input_nopol)
                            break

            elif menu_4 == '2':
                break

            else:
                print('Invalid input. Tolong masukkan pilihan yang sesuai\n')

#=============================================================================================================================================

# Exit Program
    elif menu == '5':
        print('Terima Kasih sudah menggunakan program')
        break

# invalid input
    else:
        print('Invalid input. Tolong masukkan pilihan yang sesuai\n')
