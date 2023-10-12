1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming dan synchronous programming adalah dua pendekatan berbeda dalam mengeksekusi tugas di dalam program. Berikut adalah perbedaan utama antara keduanya:

- Synchronous Programming:
Dalam synchronous programming, tugas-tugas dieksekusi secara berurutan satu per satu.
Satu tugas harus selesai sebelum tugas berikutnya dimulai.
Ini adalah pendekatan linear dan blok program hingga tugas saat ini selesai.
- Asynchronous Programming:
Dalam asynchronous programming, tugas-tugas dieksekusi secara simultan dan tidak harus menunggu tugas sebelumnya selesai.
Tugas yang membutuhkan waktu, seperti operasi I/O (input/output), dapat berjalan di latar belakang tanpa menghentikan eksekusi program utama.
Biasanya, asynchronous programming menggunakan callback, promise, async/await, atau event-driven untuk mengelola tugas yang berjalan secara paralel.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma event-driven programming adalah pendekatan di mana program merespons terhadap peristiwa yang terjadi, seperti tindakan pengguna atau pesan yang diterima. Maksudnya adalah program akan menunggu dan merespons peristiwa yang terjadi tanpa harus berjalan secara linear. Contoh penerapannya adalah dalam pembuatan aplikasi web dengan JavaScript, seperti mengendalikan elemen HTML seperti tombol, form input, atau menangani permintaan AJAX yang dipicu oleh peristiwa tertentu.

3. Jelaskan penerapan asynchronous programming pada AJAX.

Penerapan asynchronous programming pada AJAX (Asynchronous JavaScript and XML) adalah pendekatan di mana permintaan HTTP dibuat ke server tanpa menghentikan eksekusi program utama. Ini memungkinkan halaman web untuk tetap responsif dan memungkinkan pengguna berinteraksi dengan situs web tanpa harus menunggu respon dari server.

4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

Fetch API adalah API baru dalam JavaScript yang menyediakan antarmuka untuk membuat permintaan HTTP dengan lebih banyak fleksibilitas dan dukungan bawaan untuk promise. Ini memungkinkan Anda mengelola permintaan secara lebih kuat dan mudah dibaca.
jQuery adalah library JavaScript yang telah ada selama beberapa waktu dan memiliki dukungan kuat untuk AJAX. Ini memberikan antarmuka yang lebih sederhana untuk melakukan permintaan AJAX.

Menurut saya, apabila kita ingin membangun aplikasi modern dan ingin memanfaatkan fitur terbaru JavaScript, Fetch API mungkin menjadi pilihan yang lebih baik. Namun, jika kita bekerja dalam lingkungan yang sudah menggunakan jQuery atau membutuhkan integrasi dengan plugin jQuery yang ada, maka jQuery dapat tetap menjadi pilihan yang valid. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat fungsi get_product_json di views.py, menambahkan path url di urls.py
- Membuat fungsi add_product_ajax di views.py, menambahkan path url di urls.py
- Menampilkan data product dengan fetch API dengan cara membuat fungsi get_products di main.html untuk mengambil data get_product_json dan fungsi refreshProducts untuk menampilkan cards dan merefresh secara asinkronus
- Membuat form dan button untuk membuat produk baru dengan AJAX
- Membuat fungsi addProduct dengan memanggil fungsi add_product_ajax dengan metode POST dan menambahkan button untuk fungsi tersebut
- Membuat fungsi deleteitem di views.py dan menambahkan path url di urls.py
- Membuat fungsi deleteitem di main.html untuk menghapus item dan menambahkan button untuk fungsi tersebut