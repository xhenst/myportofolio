Nama : Kayla Alifah Khairunisa

NPM : 2506611931

Kelas : PBP E


### Tugas 1

1. Iya, saya menggunakan elemen semantik HTML5 seperti <section> pada website portofolio saya. Saya menggunakan <section> untuk memisahkan bagian Profile dan Education agar struktur halaman lebih terorganisir. Penggunaan elemen tersebut membantu saya mengelompokkan konten berdasarkan fungsinya, sehingga lebih mudah dibaca dan dikelola meskipun website yang dibuat masih berupa static web.
2. Tantangan yang saya temukan adalah menjaga layout tetap rapi saat berpindah dari desktop ke mobile. Saya menggunakan Grid untuk menampilkan tiga card Education secara horizontal di desktop, lalu mengubahnya menjadi satu card per baris di mobile. Saya mengeceknya melalui responsive mode pada browser agar tampilannya tetap nyaman dan tidak perlu scroll ke samping.
3. Karena website saya masih berupa static web, informasi yang ditampilkan masih harus diperbarui secara manual melalui kode HTML. Hal ini membuat website kurang fleksibel ketika saya ingin menambahkan atau memperbarui informasi. Pada iterasi berikutnya, saya ingin menambahkan fitur navigasi yang lebih interaktif, sehingga pengunjung dapat berpindah antarbagian website dengan lebih mudah.


### Tugas 2

1. Alur yang terjadi ketika pengguna membuka halaman portofolio baru adalah:
Browser → urls.py proyek → urls.py aplikasi → view → model → template → Browser

    - urls.py proyek menerima URL request dari pengguna dan menentukan aplikasi mana yang menangani URL tersebut.
    - urls.py aplikasi mencocokkan URL dengan pola URL yang tersedia dan mengarahkannya ke fungsi atau class view yang sesuai.
    - view menangani request tersebut. Jika halaman membutuhkan data portofolio, view mengambil data dari model melalui database.
    - Model merepresentasikan struktur dan data yang disimpan di database, misalnya nama proyek, deskripsi, tahun, dan teknologi yang digunakan.
    - Setelah mendapatkan data, view mengirimkannya sebagai context ke template.
    - Template menggunakan data tersebut untuk membentuk tampilan HTML.
2. Data sebaiknya disimpan pada model karena model terhubung dengan database, sehingga data dapat diubah, ditambah, atau dihapus tanpa mengubah template. Hal ini membuat aplikasi lebih mudah dipelihara dan dikembangkan.
3.  makemigrations = membuat file migrasi berdasarkan perubahan pada model.
    migrate = menerapkan perubahan tersebut ke database.

    - Contoh perubahan model yang mengharuskan menjalankan kedua perintah ini adalah ketika menambahkan field baru pada model.