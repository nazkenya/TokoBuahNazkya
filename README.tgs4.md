1. Django UserCreationForm adalah form bawaan yang disediakan oleh Django yang digunakan untuk pembuatan pengguna baru di web Django. 
Kelebihan:
- Mudah digunakan: Django UserCreationForm adalah kelas form yang sudah siap pakai, sehingga Anda - tidak perlu menulis kode dari awal.
- Aman: Django UserCreationForm menggunakan verifikasi kata sandi yang kuat untuk mencegah serangan brute force.
- Fleksibel: Anda dapat menyesuaikan Django UserCreationForm untuk memenuhi kebutuhan Anda.
Kekurangan
- Tidak dapat digunakan untuk membuat pengguna dengan peran khusus, seperti administrator atau moderator, Anda tidak dapat menggunakan Django UserCreationForm secara langsung. Anda perlu membuat kelas form yang diperluas dari Django UserCreationForm dan menambahkan bidang untuk peran pengguna.

2. Dalam konteks Django, autentikasi (authentication) dan otorisasi (authorization) adalah dua konsep yang sangat penting untuk mengelola akses pengguna dalam aplikasi web. Perbedaan antara keduanya adalah sebagai berikut:

Autentikasi (Authentication):
--> Autentikasi adalah proses verifikasi identitas pengguna. Ini memastikan bahwa pengguna yang mencoba mengakses aplikasi adalah mereka yang mengklaim diri mereka dan memiliki kredensial yang valid untuk masuk.
Contoh: Ketika pengguna memasukkan nama pengguna (username) dan kata sandi (password) mereka saat login, server Django memeriksa apakah kredensial ini cocok dengan yang ada di database. Jika cocok, pengguna dianggap berhasil diautentikasi.

Otorisasi (Authorization):
--> Otorisasi adalah proses menentukan hak akses atau izin yang dimiliki oleh pengguna yang telah diotentikasi. Ini mengatur apa yang dapat dilihat atau dilakukan oleh pengguna dalam aplikasi.
Contoh: Setelah pengguna berhasil login, Django akan memeriksa peran (role) yang dimiliki pengguna, dan berdasarkan itu, memutuskan apakah pengguna memiliki akses ke halaman tertentu atau dapat melakukan tindakan tertentu dalam aplikasi.

Keduanya penting dalam mengelola keamanan dan fungsionalitas aplikasi web karena autentikasi memastikan bahwa pengguna adalah mereka yang mengklaim diri mereka, sehingga menghindari akses yang tidak sah. Sedangkan otorisasi memastikan bahwa pengguna hanya memiliki akses ke sumber daya dan tindakan yang sesuai dengan peran dan izin mereka, menjaga integritas data dan fitur aplikasi.

3. Cookies adalah file kecil yang disimpan di browser pengguna. Cookies dapat digunakan untuk menyimpan data sesi pengguna, seperti nama pengguna, kata sandi, dan preferensi. Dalam konteks aplikasi web, cookies digunakan untuk menyimpan data sesi pengguna. Data sesi pengguna adalah data yang diperlukan untuk mengidentifikasi pengguna dan memungkinkan mereka untuk berinteraksi dengan aplikasi.

Django menggunakan cookies untuk mengelola data sesi pengguna dengan cara berikut:
1) Ketika pengguna pertama kali masuk, Django membuat cookie yang berisi token sesi.
2) Token sesi ini digunakan untuk mengidentifikasi pengguna di setiap permintaan berikutnya.
3) Django menyimpan data sesi pengguna di database, terkait dengan token sesi.

Berikut adalah beberapa contoh bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna:
- Untuk menyimpan nama pengguna dan kata sandi pengguna: Django menggunakan cookies untuk menyimpan nama pengguna dan kata sandi pengguna, sehingga pengguna tidak perlu memasukkannya lagi setiap kali mereka masuk.
- Untuk menyimpan preferensi pengguna: Django menggunakan cookies untuk menyimpan preferensi pengguna, seperti bahasa dan tema.
- Untuk menyimpan status login pengguna: Django menggunakan cookies untuk menyimpan status login pengguna, sehingga pengguna tetap masuk jika mereka menavigasi ke halaman lain di aplikasi.

4. Penggunaan cookies secara default aman dalam pengembangan web. Namun, ada beberapa risiko potensial yang harus diwaspadai, seperti:

- Kejahatan siber: Cookie dapat diretas oleh penjahat siber untuk mencuri informasi sensitif, seperti kata sandi.
- Kebijakan privasi: Cookie dapat digunakan untuk melacak aktivitas pengguna, yang dapat melanggar kebijakan privasi.
- Cross-Site Scripting (XSS): Jika data dari cookies dieksekusi tanpa sanitasi (misalnya, dalam skrip JavaScript), aplikasi web dapat menjadi rentan terhadap serangan Cross-Site Scripting (XSS). Serangan ini dapat memungkinkan penyerang menyisipkan kode berbahaya dalam cookies dan merusak keamanan aplikasi.
- Cross-Site Request Forgery (CSRF): Cookies yang digunakan untuk mengidentifikasi pengguna dalam permintaan HTTP juga dapat digunakan dalam serangan Cross-Site Request Forgery (CSRF) jika tidak diimplementasikan dengan benar. 

5. Cara mengimplementasikan checklist di atas secara step-by-step
- Membuat fungsi dan form register menggunakan UserCreationForm, dan membuat register.html untuk tampilan web saat user membuat akun. Mengimpor fungsi ke url serta menambahkan path url
- Membuat fungsi login_user menggunakan fungsi authenticate, dan membuat login.html untuk tampilan web saat user login. Mengimpor fungsi ke url serta menambahkan path url
- Membuat fungsi logout_user dan membuat tombol logout di tampilan web utama. Mengimpor fungsi ke url serta menambahkan path url
- Merestriksi halamam utama dengan menambahkan login_required agar tampilan halaman utama hanya bisa diakses apabila user sudah login
- Menambahkan data last login ke halaman main dengan menambahkan cookie di fungsi login_user serta menambahkan kode di fungsi logout agar cookie kehapus saat user melakukan logout. Menambahkan juga informasi last login ke halaman main di file main.html
- Menambahkan user ke model Item serta mengedit fungsi create_product agar product yang baru dibuat hanya diperuntukkan untuk user yang sedang login serta mengubah fungsi show_main untuk mengubah "nama" menjadi username user. 
- Melakukan makemigrations karena saya telah menambahkan attribut pada model Item 
- Membuka halaman web (runserver) lalu menambahkan 2 akun dengan masing-masing 3 dummy data