Nama : Kayla Alifah Khairunisa

NPM : 2506611931

Kelas : PBP E



### Tugas 1

1. **Penggunaan Elemen Semantik HTML5**
   * Iya, saya menggunakan elemen semantik HTML5 seperti `<section>` pada website portofolio saya. Saya menggunakan `<section>` untuk memisahkan bagian Profile dan Education agar struktur halaman lebih terorganisir. Penggunaan elemen tersebut membantu saya mengelompokkan konten berdasarkan fungsinya, sehingga lebih mudah dibaca dan dikelola meskipun website yang dibuat masih berupa *static web*.

2. **Tantangan Desain Responsif**
   * Tantangan yang saya temukan adalah menjaga *layout* tetap rapi saat berpindah dari desktop ke *mobile*. Saya menggunakan *Grid* untuk menampilkan tiga *card Education* secara horizontal di desktop, lalu mengubahnya menjadi satu *card* per baris di *mobile*. Saya mengeceknya melalui *responsive mode* pada *browser* agar tampilannya tetap nyaman dan tidak perlu *scroll* ke samping.

3. **Keterbatasan Web Statis dan Rencana Pengembangan**
   * Karena website saya masih berupa *static web*, informasi yang ditampilkan masih harus diperbarui secara manual melalui kode HTML. Hal ini membuat website kurang fleksibel ketika saya ingin menambahkan atau memperbarui informasi. Pada iterasi berikutnya, saya ingin menambahkan fitur navigasi yang lebih interaktif, sehingga pengunjung dapat berpindah antarbagian website dengan lebih mudah.


### Tugas 2

1. **Alur Request dan Siklus Django**
   * Alur yang terjadi ketika pengguna membuka halaman portofolio baru adalah:  
     `Browser` → `urls.py proyek` → `urls.py aplikasi` → `view` → `model` → `template` → `Browser`
   * Penjelasan masing-masing komponen:
     * **`urls.py` proyek** menerima URL *request* dari pengguna dan menentukan aplikasi mana yang menangani URL tersebut.
     * **`urls.py` aplikasi** mencocokkan URL dengan pola URL yang tersedia dan mengarahkannya ke fungsi atau *class view* yang sesuai.
     * **`view`** menangani *request* tersebut. Jika halaman membutuhkan data portofolio, *view* mengambil data dari *model* melalui database.
     * **`model`** merepresentasikan struktur dan data yang disimpan di database, misalnya nama proyek, deskripsi, tahun, dan teknologi yang digunakan.
     * **`template`** menerima *context* data dari *view* dan menggunakan data tersebut untuk membentuk tampilan HTML yang dikembalikan ke *browser*.

2. **Alasan Penyimpanan Data pada Model**
   * Data sebaiknya disimpan pada *model* karena *model* terhubung dengan database, sehingga data dapat diubah, ditambah, atau dihapus secara dinamis tanpa harus mengubah kode pada *template*. Hal ini membuat aplikasi lebih mudah dipelihara dan dikembangkan (*maintainability*).

3. **Perbedaan `makemigrations` dan `migrate`**
   * **`makemigrations`**: Berfungsi untuk membuat file migrasi baru berdasarkan perubahan struktur yang baru saja Anda lakukan pada *model*.
   * **`migrate`**: Berfungsi untuk menerapkan perubahan atau file migrasi tersebut secara nyata ke dalam database.
   * **Contoh Kasus**: Perubahan model yang mengharuskan menjalankan kedua perintah ini adalah ketika Anda menambahkan *field* baru (misalnya kolom `is_active` atau tanggal pembuatan) pada suatu *model*.
    ### Tugas 3

1. **Penggunaan ModelForm dan CSRF Token pada Django**
   * **Mengapa menggunakan `ModelForm` alih-alih form HTML manual:** `ModelForm` mempermudah pembuatan form dengan cara menghubungkannya secara langsung dengan model Django yang sudah ada. Keunggulan utamanya meliputi penerapan prinsip DRY (*Don't Repeat Yourself*), validasi otomatis berdasarkan *field* dan tipe data pada model, serta kemudahan dalam menyimpan data ke database (cukup menggunakan `form.save()`) tanpa perlu melakukan pemetaan (*mapping*) data `request.POST` satu per satu secara manual.
   * **Mengapa wajib menambahkan `{% csrf_token %}`:** Tag ini diwajibkan untuk melindungi aplikasi dari serangan *Cross-Site Request Forgery* (CSRF). Token unik ini memastikan bahwa setiap *request* metode mutatif (seperti POST, PUT, atau DELETE) yang diterima server benar-benar dikirimkan secara sadar oleh pengguna melalui halaman aplikasi yang sah, bukan disusupi oleh situs pihak ketiga yang berbahaya.

2. **Keunggulan JSON dibandingkan XML dalam Pengembangan Web Modern**
   * **Ukuran *Payload* Lebih Ringan:** JSON tidak menggunakan tag penutup (*closing tags*) yang berulang seperti XML, sehingga ukuran datanya jauh lebih kecil dan menghemat *bandwidth* jaringan.
   * **Kemudahan *Parsing*:** JSON berakar dari struktur objek JavaScript, membuat proses pembacaan (*parsing*) data secara *native* menjadi sangat cepat dan mudah di hampir semua bahasa pemrograman modern maupun di sisi *browser*, sedangkan XML memerlukan *parser* khusus (seperti DOM/SAX) yang lebih kompleks dan lambat.

3. **Alur View Mengembalikan Data Portofolio dalam JSON dan Pentingnya Serialization**
   * **Alur Fungsi *View*:**
     1. Klien (browser/pengguna) mengirimkan *request* HTTP ke suatu URL *endpoint*.
     2. Fungsi *view* pada Django menerima *request* tersebut.
     3. *View* berinteraksi dengan database melalui Django ORM untuk mengambil data portofolio (misalnya `Portfolio.objects.all()`).
     4. Data dari model yang masih berupa *QuerySet* atau objek Python kompleks di-*serialize* ke dalam bentuk tipe data primitif (seperti *list* berisi *dictionary*).
     5. Data yang sudah di-konversi dikembalikan ke klien menggunakan `JsonResponse` (atau `HttpResponse` dengan *content-type* `application/json`).
   * **Mengapa perlu *Serialization*:** Objek model Django adalah struktur data kompleks di dalam memori Python yang tidak bisa langsung dibaca atau diubah menjadi format teks JSON standar. Proses *serialization* diperlukan untuk menjembatani objek tersebut menjadi tipe data dasar yang kompatibel dengan format JSON agar dapat ditransmisikan secara mulus melalui protokol HTTP.
### Penggunaan AI Tugas 3

Dalam tugas ini, saya menggunakan Gemini untuk membantu membuat fungsi CRUD pada *section* **Project** dan **Experience** berdasarkan modul *Education* yang sudah jadi sebelumnya, serta membantu merapikan gaya CSS.

**Lampiran Prompting:**
* **Fungsi CRUD & Styling:** Berdasarkan kode pada modul *Education* yang sudah ada, bisakah buatkan fungsi CRUD dan sesuaikan kode untuk *section* Project dan Experience agar dapat menerima input melalui website, serta rapikan tampilan CSS-nya.

**AI Disclosure & Analisis**
* **Tools yang Digunakan:** Gemini
* **Analisis Keterbatasan AI:** AI sering kali memberikan hasil yang kurang pas—misalnya memberikan penamaan kelas atau elemen (seperti tombol) yang berbeda dengan struktur kode yang sudah saya buat sebelumnya, sehingga harus saya periksa dan ubah satu persatu. Selain itu, tipe input dan isi data pada setiap modul memiliki karakteristik yang berbeda-beda (*education*, *project*, dan *experience*), sehingga AI tidak bisa langsung menyamakannya secara otomatis.
* **Perbaikan Manual:** Untuk mengatasi keterbatasan tersebut, saya meneliti kembali kode yang dihasilkan AI, menyesuaikan nama kelas/elemen agar konsisten dengan proyek saya, serta menyesuaikan tipe input, *form*, dan logika program secara manual agar setiap modul dapat menerima data dengan benar sesuai struktur aslinya.