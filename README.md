# Aplikasi Rental Mobil
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### _Context_
_Project_ ini merupakan implementasi program rental mobil meggunakan Python. Program ini memungkinkan pengguna untuk mencari dan menampilkan informasi detail kendaraan rental berdasarkan merk dan model. Aplikasi ini dibangun dengan tujuan memberikan kemudahan dalam mengakses data kendaraan rental suatu perusahaan.

## _Key Features_
- Daftar kendaraan rental
- Pencarian kendaraan berdasarkan nomor polisi dan merk kendaraan
- Manajemen Pengguna dari mulai tambah, perbarui, sampai ke hapus detail kendaraan


## _Objective_
- Menyediakan pencarian informasi detail kendaraan secara efisien
- Menyediakan sistem yang efisien dan mudah digunakan untuk mengelola inventaris mobil
- Memudahkan pengguna dalam mengatur kendaraan rental
- Mengurangi kesalahan administratif, serta meningkatkan transparansi dan akuntabilitas dalam pengelolaan sumber daya kendaraan.
- Membantu dalam memfasilitasi proses penyewaan mobil oleh karyawan atau anggota perusahaan.

## Batasan
- __Standar penulisan nomor polisi__: Program ini hanya bisa digunakan pada kendaraan bernomor polisi standar, tidak bisa menggunakan nomor polisi _custom_

## _Data Description_
| No | Nama Kolom | Type | Range | Deskripsi |
| ------ | ------ | ---- | ----- | --------- |
| 1 | Merk | `str` | - | Merk kendaraan |
| 2 | Model | `str` | - | Model dari suatu merk kendaraan |
| 3 | No. Polisi | `str` | min. 7 karakter | No. Polisi/plat nomor kendaraan (unik) |
| 4 | Tahun | `int` | - | Tahun produksi kendaraan |
| 5 | Harga Sewa | `int` | - | Harga sewa kendaraan perhari |

## Deskripsi Fitur
### Menu Utama
Menu utama terdiri dari 5 submenu (CRUD): _Create, Read, Update, Delete_, dan _Exit_. Untuk keluar aplikasi pengguna dapat memilih submenu ke-5 'Keluar Aplikasi'.

#### Submenu 1: _Read_

> Fitur utama pada submenu ini untuk menampilkan seluruh data detail kendaraan dari Merk, Model, Nomor Polisi, Tahun Produksi, dan harga sewa perhari. Pengguna juga dapat mencari kendaraan tertentu dengan memasukkan nomor polisi kendaraan. Data yang ditampilkan akan disortir berdasarkan merk kendaraan dan dikelompokkan berdasarkan merk dan model kendaraan.

> Terdapat fitur filter merk agar pengguna dapat melihat hanya merk tertentu saja.

#### Submenu 2: _Create_

> Fitur utama submenu ini untuk menambahkan data kendaraan baru untuk disewakan. Pengguna akan diminta untuk memasukkan nomor polisi terlebih dahulu untuk dicek apabila terdapat duplikasi data kendaraan. Selanjutnya pengguna perlu melengkapi detail kendaraan untuk dimasukkan ke dalam daftar.

> Pengguna juga dapat menambahkan kendaraan lebih dari satu sekaligus.

#### Submenu 3: _Update_

> Fitur ini dapat mengubah detail data dari daftar kendaraan. Penggunakan akan diminta memasukkan nomor polisi kendaraan dan kolom mana yang ingin diperbarui datanya. Program akan memberikan peringatan/notifikasi bila pengguna melakukan pembaruan data pada kolom nomor polisi jika pembaruan datanya berupa duplikasi nomor polisi kendaraan.

#### Submenu 4: _Delete_

> Fitur dalam submenu ini dapat menghapus data kendaraan bila pengguna sudah tidak memerlukannya lagi. Pengguna perlu memasukkan nomor polisi kendaraan untuk dicari yang selanjutnya akan ditampilkan detail kendaraan tersebut dan konfirmasi penghapusan data.

#### Submenu 5: _Exit_

> Pengguna dapat keluar dari aplikasi dengan memilih submenu 5 (_Exit_) pada Menu Utama.


 [![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://www.instagram.com/raka_id/)
