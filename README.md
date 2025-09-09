# Penjelasan TUGAS 2 PBP

## Penjelasan Langkah-Langkah yang dilakukan
### Membuat sebuah proyek django baru

**1. Mengaktifkan virtual environment**
``` 
python -m venv env
env\Scripts\activate
```

Tujuannya agar project yang dibuat memiliki lingkungan Python yang terisolasi. Sehingga nantinya library yang diinstal hanya berlaku di env itu.

**2. Menyiapkan Dependencies dan Membuat Proyek Django**
Saya membuat requirements.txt dengan isi seperti yang dijelaskan di tutorial 0. Kemudian saya lakukan instalasi terhadap dependencies dengan perintah berikut.
```
pip install -r requirements.txt
django-admin startproject football_news .
```
Kemudian setelah itu saya melakukan konfigurasi environment variables dan proyek seperti step by step yang dijelaskan di tutorial 0 (membuat file .env dan .env.prod, modifikasi settings.py untuk menambahkan environment variables, menambahkan allowed host, menambah konfigurasi production, dan mengubah konfigurasi database).

### Membuat aplikasi dengan nama main pada proyek tersebut.
Saya menjalankan perintah berikut di cmd
```
python manage.py startapp main
```
lalu menambahkan 'main' di INSTALLED_APPS di settings.py

### Membuat model pada aplikasi main dengan nama Product dan menambah atributnya
1. Saya menambah kelas Product di models.py dan atribut wajib sesuai yang sudah diinstruksikan di deskripsi tugas 2.
2. Saya melakukan migrasi model supaya perubahan yang saya buat di models.py tercatat dan diterapkan ke database oleh Django dengan menjalankan perintah berikut.
```
python manage.py makemigrations
python manage.py migrate
```

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
Saya membuat sebuah fungsi di views.py yang akan mengirim data (nama aplikasi, nama, kelas) ke template html.

### Membuat sebuah routing pada urls.py
1. Saya mendefinisikan routing pada urls.py pada aplikasi main untuk memetakan fungsi pada views.py
2. Kemudian, saya menambahkan routing pada urls.py di level proyek agar ketika membuka alamat domain utama, request diarahkan ke urls.py milik aplikasi main sehingga langsung menampilkan halaman utama

## Jawaban pertanyaan
### Alur request client ke web
![Diagram alur request client ke web](images/diagram.png)
**1. Client buka browser lalu akses url**
**2. Browser mengirimkan HTTP request ke server lewat internet**
**3. Django menerima request lewat manage.py**
**4. Django melakukan pengecekan url lewat urls.py**
Jika tidak ditemukan url yang cocok, akan dikembalikan "404 Error Not Found". Jika ditemukan, request akan diarahkan ke fungsi/class di views.py
**5. Processing lewat views.py**
Views.py berisi kode Python yang akan dieksekusi untuk request tersebut. Jika ada kebutuhan untuk mengambil atau memproses data dari database, views.py akan memanggil models.py kemudian data yang sudah diambil akan dikembalikan ke views.py
**6. Template (HTML)**
View lalu merender file HTML template dengan data yang sudah diambil dari model. 
**7. Response ke Client**
Django membungkus hasil render dalam objek HttpResponse. Response ini dikirim balik lewat internet ke browser user. Browser akan menampilkan halaman sesuai isi HTML yang diterima.

### Peran settings.py dalam proyek Django
settings.py merupakan file konfigurasi utama dalam proyek django. Dalam file settings.py kita dapat mengatur konfigurasi database (database apa yang ingin digunakan), aplikasi yang aktif (INSTALLED_APPS), menentukan domain/host mana yang boleh mengakses aplikasi (ALLOWED_HOST), dan lain-lain.

### Migrasi database di Django
Pertama, kita mendefinisikan model dalam class models.py. Lalu kita melakukan perintah berikut di cmd
```
python manage.py makemigrations
```
Perintah tersebut menginstruksikan Django untuk membaca perubahan di models.py dan membuat file migrasi di folder migrations. File ini berisi instruksi-instruksi SQL (buat tabel baru, hapus kolom, hapus tabel).

Setelah itu kita menjalankan perintah berikut di cmd.
```
python manage.py migrate
```
Perintah tersebut akan menerjemahkan file migrasi tadi menjadi perintah SQL yang dieksekusi ke database. Database akan diperbarui sesuai dengan definisi model.
Django akan menyimpan riwayat migrasi di tabel khusus bernama django_migrations di database. Jadi, Django tahu migrasi mana yang sudah diterapkan, mana yang belum.

### Framework Django sebagai awal pembelajaran pengembangan perangkat lunak
Menurut saya, Django dijadikan sebagai permulaan pembelajaran pengembangan perangkat lunak karena Django menggunakan bahasa pemrograman Python yang beginner-friendly. Selain itu, Django juga menggunakan arsitektur MTV (Model–Template–View), yaitu arsitektur yang memisahkan bagian data, logika, dan tampilan, sehingga membantu pemula memahami alur kerja website secara lebih terstruktur dan mudah. Dengan Django, pemula bisa langsung membuat aplikasi web lengkap dari backend sampai tampilan, sehingga lebih cepat memahami alur kerja sebuah aplikasi secara menyeluruh.