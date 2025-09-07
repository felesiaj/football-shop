# Penjelasan TUGAS 2 PBP

## Membuat sebuah proyek django baru

### 1. Mengaktifkan virtual environment
``` 
python -m venv env
env\Scripts\activate
```

Tujuannya agar project yang dibuat memiliki lingkungan Python yang terisolasi. Sehingga nantinya library yang diinstal hanya berlaku di env itu.

### 2. Menyiapkan Dependencies dan Membuat Proyek Django
Saya membuat requirements.txt dengan isi seperti yang dijelaskan di tutorial 0. Kemudian saya lakukan instalasi terhadap dependencies dengan perintah berikut.
```
pip install -r requirements.txt
django-admin startproject football_news .
```
Kemudian setelah itu saya melakukan konfigurasi environment variables dan proyek seperti step by step yang dijelaskan di tutorial 0 (membuat file .env dan .env.prod, modifikasi settings.py untuk menambahkan environment variables, menambahkan allowed host, menambah konfigurasi production, dan mengubah konfigurasi database).

## Membuat aplikasi dengan nama main pada proyek tersebut.

### 1. Membuat aplikasi baru dengan nama main
Saya menjalankan perintah berikut di cmd
```
python manage.py startapp main
```
lalu menambahkan 'main' di INSTALLED_APPS di settings.py

## Membuat model pada aplikasi main dengan nama Product dan menambah atributnya
1. Saya menambah kelas Product di models.py dan atribut wajib sesuai yang sudah diinstruksikan di deskripsi tugas 2.
2. Saya melakukan migrasi model supaya perubahan yang saya buat di models.py tercatat dan diterapkan ke database oleh Django dengan menjalankan perintah berikut.
```
python manage.py makemigrations
python manage.py migrate
```

## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
Saya membuat sebuah fungsi di views.py yang akan mengirim data (nama aplikasi, nama, kelas) ke template html.

## Membuat sebuah routing pada urls.py
1. Saya mendefinisikan routing pada urls.py pada aplikasi main untuk memetakan fungsi pada views.py
2. Kemudian, saya menambahkan routing pada urls.py di level proyek agar ketika membuka alamat domain utama, request diarahkan ke urls.py milik aplikasi main sehingga langsung menampilkan halaman utama