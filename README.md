# Aplikasi Rental Mobil
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### _Context_
_Project_ ini merupakan implementasi program rental mobil emggunakan Python. Program ini memungkinkan pengguna untuk mencari dan menampilkan informasi detail kendaraan rental berdasarkan merk dan model. Aplikasi ini dibangun dengan tujuan memberikan kemudahan dalam mengakses data kendaraan rental suatu perusahaan.

## _Key Features_
- Daftar seluruh kendaraan rental
- Pencarian kendaraan berdasarkan nomor polisi kendaraan
- Filter merk kendaraan

## _Objective_
- Menyediakan pencarian informasi detail kendaraan
- Memudahkan pengguna dalam mengakses setiap fitur di dalamnya
- Membantu pengguna untuk mencari detail kendaraan secara efisien

## _Data Description_
| No | Nama Kolom | Type | Range | Deskripsi |
| ------ | ------ | ---- | ----- | --------- |
| 1 | Merk | `str` | - | Merk kendaraan |
| 2 | Model | `str` | - | Model dari suatu merk kendaraan |
| 3 | No. Polisi | `str` | min. 7 karakter | No. Polisi/plat nomor kendaraan (unik) |
| 4 | Tahun | `int` | - | Tahun produksi kendaraan |
| 5 | Harga Sewa | `int` | - | Harga sewa kendaraan perhari |

## Batasan
- __Standar penulisan nomor polisi__: Program ini hanya bisa digunakan pada kendaraan bernomor polisi standar, tidak bisa menggunakan nomor polisi _custom_
 
## Fitur tersedia
### Menu Utama
