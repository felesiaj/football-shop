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
