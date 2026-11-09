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


### Penggunaan AI Tugas 4

Dalam tugas ini, saya menggunakan Gemini sebatas untuk membantu mencari tahu penyebab *error* (troubleshooting) saat menerapkan pembatasan hak akses, serta meminta referensi dasar Flexbox untuk merapikan *navbar*.

**Lampiran Prompting:**

* **Troubleshooting & Styling:** Bagaimana cara membuat elemen *login* dan *register* terdorong ke paling kanan *navbar* menggunakan CSS? Selain itu, kenapa muncul *error* "Invalid block tag" dan "ValueError: perm_list" saat saya mencoba menerapkan *permission*?

**AI Disclosure & Analisis**

* **Tools yang Digunakan:** Gemini
* **Analisis Keterbatasan AI:** Jawaban AI sering kali bersifat terlalu umum atau kurang pas dengan logika tugas. Misalnya, AI sempat menggabungkan kondisi untuk *Superuser* dan *Editor* dalam satu blok, sehingga pembatasan tombol tidak berfungsi dengan benar. Selain itu, untuk urusan UI/UX, angka *margin* atau *gap* yang disarankan AI jarang langsung cocok dengan desain atau proporsi *website* yang sedang saya buat.
* **Perbaikan Manual:** Untuk mengatasi hal tersebut, saya harus merombak dan memisahkan logika `if` di *template* HTML secara manual agar tombol Edit dan Hapus muncul sesuai hak akses masing-masing peran. Saya juga mengatur ulang nilai *margin* dan *gap* pada CSS secara mandiri dengan *trial and error* hingga posisi *navbar* dan jarak antar teks benar-benar presisi sesuai dengan desain yang saya inginkan.


### Tugas 5

1. *Debouncing* adalah teknik pemrograman yang digunakan untuk menunda atau membatasi frekuensi eksekusi suatu fungsi dalam rentang waktu tertentu, sehingga fungsi tersebut baru akan berjalan setelah pengguna berhenti melakukan aksi (seperti berhenti mengetik) selama jeda waktu yang telah ditentukan. Teknik ini sangat penting diterapkan pada fitur pencarian berbasis AJAX agar server tidak kewalahan menerima kiriman permintaan secara terus-menerus di setiap ketukan tombol. Tanpa *debouncing*, setiap huruf yang diketik akan langsung memicu *fetch request* baru yang dapat membebani sumber daya server, memperlambat performa aplikasi, serta berpotensi menimbulkan masalah *race condition* pada data yang ditampilkan.

2. Dalam JavaScript asinkron, penggunaan `await` berfungsi untuk menunda eksekusi kode selanjutnya di dalam fungsi `async` sampai sebuah *Promise* benar-benar selesai diproses (*resolved*). Ketika kita menggunakan `fetch()`, `await` memastikan bahwa program menunggu hingga koneksi jaringan selesai mengembalikan respons penuh dari server sebelum lanjut membaca atau mengonversi data tersebut menjadi format JSON. Jika kita tidak menggunakan `await`, fungsi `fetch()` akan langsung mengembalikan objek *Promise* yang masih berstatus *pending* alih-alih data aslinya, sehingga baris kode berikutnya akan gagal membaca data dan memicu *error*.

3. Serangan XSS (*Cross-Site Scripting*) adalah kerentanan keamanan web di mana penyerang dapat menyisipkan skrip berbahaya—seperti kode JavaScript atau tag HTML injeksi—ke dalam halaman web yang nantinya akan dieksekusi oleh peramban pengguna lain. Data yang ditampilkan melalui AJAX dan JavaScript jauh lebih rentan terhadap serangan ini daripada data dari *template* Django karena Django secara otomatis melakukan *escaping* karakter khusus di sisi server. Sebaliknya, ketika JavaScript menyisipkan data mentah dari respons JSON ke dalam DOM menggunakan properti seperti `innerHTML`, peramban akan langsung membaca dan menjalankan kode apa pun yang terkandung di dalamnya, sehingga memerlukan penanganan keamanan tambahan seperti fungsi `escapeHtml` di sisi *frontend* dan `strip_tags` di sisi *backend*.

### Penggunaan AI Tugas 5

Dalam tugas ini, saya menggunakan Gemini untuk membantu mengimplementasikan materi dan pola dari Tutorial 05—seperti pemuatan data asinkron via AJAX, pencarian dinamis dengan *debouncing*, form tambah data berbasis modal, serta perlindungan keamanan XSS (*client-side* `escapeHtml` dan *backend* `strip_tags`)—secara *end-to-end* ke dalam modul **Experience** pada portofolio.

**Lampiran Prompting:**
* **Implementasi Tutorial 5 ke Modul Experience:** Berdasarkan konsep AJAX, modal, dan pencegahan XSS yang dipelajari di Tutorial 05, bantu saya mengimplementasikannya ke modul *Experience* di Django, termasuk membuat fungsi `fetch` data, pengaturan form modal interaktif, pencarian tanpa *reload*, serta penerapan fungsi keamanan `escapeHtml` dan `strip_tags`.

**AI Disclosure & Analisis**
* **Tools yang Digunakan:** Gemini
* **Analisis Keterbatasan AI:** AI terkadang menyarankan struktur HTML mentah atau penggunaan *class* CSS generik yang tidak sesuai dengan desain *custom* tema proyek saya. AI juga kerap memberikan pemetaan *field* atau nama variabel yang berbeda dengan struktur model *Experience* yang saya miliki, sehingga elemen kartu tidak langsung menyatu dengan gaya halaman *Experience*.
* **Perbaikan Manual:** Untuk mengatasi keterbatasan tersebut, saya melakukan verifikasi dan penyesuaian kode secara manual, menyelaraskan struktur elemen HTML kartu *Experience* agar mendaur ulang kelas CSS yang sudah ada di halaman *Education* (`education-card-item`, `education-card-header`, dll.), memastikan *endpoint* URL Django terpanggil dengan benar, serta menguji coba fungsionalitas CRUD AJAX secara langsung di *browser* dan terminal Django.

**Log Interaksi AI:**
1. **Integrasi AJAX GET & Render Card:** Menyesuaikan skrip `fetch` agar mengambil data *experience* dari server dan merendernya secara dinamis ke dalam DOM.
2. **Pencarian Dinamis & Debouncing:** Mengonfigurasi *event listener* pada kolom pencarian agar menyaring data *experience* secara asinkron.
3. **Sinkronisasi Tampilan dengan Education:** Menata ulang struktur elemen kartu *Experience* agar menggunakan kelas CSS yang konsisten dengan halaman *Education*.
4. **Implementasi Keamanan XSS:** Menambahkan fungsi `escapeHtml` pada tingkat *frontend* untuk seluruh teks dinamis serta menambahkan metode `clean_*` menggunakan `strip_tags` pada kelas `ExperienceForm` di sisi *backend*.



### Tugas 6

1. **REST (Representational State Transfer)** adalah gaya arsitektur yang digunakan untuk merancang API agar komunikasi antara client dan server memiliki struktur dan aturan yang konsisten. REST menggunakan resource sebagai objek utama yang diakses melalui URL serta memanfaatkan HTTP method seperti GET, POST, PUT, PATCH, dan DELETE untuk menentukan tindakan terhadap resource tersebut. Mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful karena JSON hanya merupakan format pertukaran data, sedangkan REST juga memiliki prinsip lain seperti penggunaan resource yang jelas, stateless communication, penggunaan HTTP method sesuai fungsinya, dan HTTP status code yang tepat. Perbedaan `PUT` dan `PATCH` terletak pada cakupan perubahan datanya. `PUT` digunakan untuk memperbarui keseluruhan data suatu resource, sedangkan `PATCH` digunakan untuk memperbarui sebagian data saja tanpa harus mengirim seluruh field. Contohnya, `PUT` digunakan ketika ingin mengganti seluruh informasi Experience, sementara `PATCH` digunakan ketika hanya ingin mengubah judul Experience tanpa mengubah informasi lainnya.

2. **Serializer** pada Django REST Framework berfungsi untuk mengubah data model Django menjadi format yang dapat dikirim melalui API, seperti JSON, serta mengubah data yang diterima dari client menjadi data yang dapat diproses oleh Django. Serializer juga bertanggung jawab melakukan validasi input sebelum data disimpan ke database agar data yang masuk sesuai dengan aturan yang telah ditentukan. Dibandingkan merakit dictionary secara manual menggunakan `JsonResponse` seperti pada Tutorial 05, serializer lebih praktis karena tidak perlu menyusun dictionary untuk setiap field secara manual, menyediakan validasi data, mendukung proses CRUD, serta membuat struktur data dan aturan validasi lebih terorganisasi. Dengan demikian, pengelolaan data API menjadi lebih konsisten, terstruktur, dan mudah dikembangkan.

3. **Autentikasi (authentication)** adalah proses untuk memverifikasi identitas pengguna yang mengakses API, sedangkan **otorisasi (authorization)** adalah proses menentukan tindakan apa saja yang boleh dilakukan oleh pengguna berdasarkan identitas dan hak aksesnya. Pada Django REST Framework, autentikasi ditangani melalui authentication class, sedangkan otorisasi ditangani melalui permission class. Contohnya pada fitur Experience, pengunjung dapat melihat data, pengguna biasa dapat memberikan star, Editor dapat memperbarui data menggunakan PATCH, dan pemilik memiliki hak untuk menambahkan serta menghapus data. Pemeriksaan hak akses harus dilakukan melalui permission class di server karena menyembunyikan tombol tertentu pada template hanya membatasi tampilan antarmuka dan tidak benar-benar mencegah pengguna mengirim request API secara langsung. Dengan permission class, server tetap memeriksa setiap request sehingga pengguna hanya dapat melakukan tindakan sesuai dengan hak aksesnya.

4. **CSRF (Cross-Site Request Forgery)** merupakan serangan yang memanfaatkan session pengguna yang masih aktif untuk mengirimkan request tanpa sepengetahuan pengguna tersebut. Ketika API menggunakan `SessionAuthentication`, browser akan mengirimkan cookie session secara otomatis bersama request. Oleh karena itu, request yang mengubah data seperti POST, PUT, PATCH, dan DELETE memerlukan token CSRF sebagai perlindungan tambahan untuk memastikan bahwa request berasal dari sumber yang sah. Token CSRF membantu mencegah pihak lain memanfaatkan session pengguna untuk melakukan perubahan data tanpa izin. Test yang menggunakan `force_authenticate` tidak cukup untuk membuktikan perlindungan CSRF berjalan karena metode tersebut melewati proses autentikasi normal Django REST Framework, sehingga mekanisme session dan pemeriksaan CSRF tidak diuji sebagaimana mestinya. Untuk menguji perlindungan tersebut, digunakan `APIClient(enforce_csrf_checks=True)` dan `.login()` agar autentikasi dilakukan melalui session seperti penggunaan browser.

### Penggunaan AI Tugas 6

Dalam tugas ini, saya menggunakan Gemini sebagai alat bantu selama proses pengembangan modul **Experience** untuk memahami dan menyesuaikan implementasi Django REST Framework (DRF) dengan struktur proyek yang sudah ada. Penggunaan AI dilakukan secara bertahap, mulai dari mendiskusikan perubahan endpoint dari implementasi sebelumnya ke DRF, memahami penyesuaian serializer dan permission class, hingga mengevaluasi hasil implementasi melalui pengujian API.

**Lampiran Prompting:**

* **Penyesuaian Endpoint Experience ke DRF:** Mendiskusikan bagian-bagian implementasi Experience yang perlu disesuaikan setelah menggunakan Django REST Framework, termasuk perubahan proses pengambilan dan pengiriman data melalui endpoint API.
* **Penyesuaian Serializer:** Mendiskusikan error yang muncul pada `ExperienceSerializer`, khususnya terkait pemetaan field model dan penggunaan `SerializerMethodField` untuk data seperti `star_count` dan `is_starred`.
* **Pengaturan Hak Akses:** Mendiskusikan penerapan `IsPortfolioOwnerOrEditorOrReadOnly` agar hak akses pemilik, Editor, pengguna biasa, dan pengunjung sesuai dengan ketentuan tugas.
* **Penyesuaian Testing:** Mendiskusikan penyusunan test menggunakan `APITestCase`, termasuk cara memeriksa perubahan database ketika request ditolak, pengujian validasi input, dan fungsionalitas star.
* **Pengujian CSRF:** Mendiskusikan penggunaan `APIClient(enforce_csrf_checks=True)` dan `.login()` untuk memahami cara menguji perlindungan CSRF pada API yang menggunakan `SessionAuthentication`.

**AI Disclosure & Analisis**

* **Tools yang Digunakan:** Gemini
* **Analisis Keterbatasan AI:** AI terkadang memberikan contoh kode yang belum sepenuhnya sesuai dengan struktur model, serializer, dan endpoint yang sudah ada pada proyek saya. Beberapa saran juga masih memerlukan penyesuaian, terutama terkait field yang tersedia pada model Experience, konfigurasi permission class, serta perilaku autentikasi dan CSRF. Pada bagian testing, AI juga memberikan asumsi awal mengenai data dan relasi model yang perlu diperiksa kembali agar pengujian sesuai dengan implementasi sebenarnya.
* **Perbaikan Manual:** Saya melakukan penyesuaian secara bertahap dengan memeriksa kode yang sudah ada, mencocokkan saran AI dengan struktur proyek, serta memahami error yang muncul selama proses implementasi. Saya juga menjalankan pengujian melalui terminal Django untuk memeriksa apakah endpoint, aturan permission, dan fungsionalitas yang diterapkan sudah berjalan sesuai kebutuhan.

**Log Interaksi AI:**

1. **Migrasi Integrasi ke DRF:** Mendiskusikan penyesuaian implementasi Experience dari penggunaan endpoint sebelumnya ke endpoint Django REST Framework.
2. **Penyesuaian Serializer:** Mengevaluasi error pada serializer, khususnya pemetaan field model dan penggunaan field tambahan seperti `star_count` dan `is_starred`.
3. **Integrasi CRUD dengan DRF:** Mendiskusikan penyesuaian fungsi JavaScript pada halaman Experience agar operasi tambah, edit, hapus, dan pengambilan data menggunakan endpoint DRF.
4. **Implementasi Permission Berdasarkan Role:** Mengevaluasi aturan akses untuk pengunjung, pengguna biasa, Editor, dan pemilik agar sesuai dengan ketentuan tugas.
5. **Penyusunan dan Evaluasi Testing:** Mendiskusikan error dan penyesuaian test API, termasuk pemeriksaan isi database, validasi input, star, serta pengujian CSRF.