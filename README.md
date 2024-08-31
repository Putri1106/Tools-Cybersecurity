# Tools Cybersecurity

## Daftar Isi

- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Catatan Keamanan](#catatan-keamanan)
- [Video Demo](#video-demo)

## Fitur

1. **Monitor Bandwidth**: Menampilkan data penggunaan bandwidth secara real-time dalam MB.
2. **Send Email**: Mengirim email dari akun Gmail ke alamat email tujuan dengan subjek dan pesan yang ditentukan.
3. **Send WhatsApp Message**: Mengirim pesan WhatsApp ke nomor tujuan menggunakan Twilio.

## Instalasi

### Prasyarat

- Python 3.x
- Paket Python yang diperlukan (lihat `requirements.txt` di bawah)

### Instalasi Paket

1. **Clone Repositori**

   ```bash
   git clone https://github.com/username/repository.git
   cd repository
   ```

2. **Instal Paket yang Diperlukan**

   Buat lingkungan virtual (opsional tetapi disarankan):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Instal paket yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

   **requirements.txt**:

   ```
   psutil
   pyfiglet
   twilio
   ```

## Penggunaan

1. **Jalankan Aplikasi**

   ```bash
   python main.py
   ```

2. **Pilih Opsi**

   - **Monitor Bandwidth**: Memulai pemantauan bandwidth.
   - **Send Email**: Mengirim email. Anda akan diminta untuk memasukkan email pengirim, email penerima, subjek, dan pesan.
   - **Send WhatsApp Message**: Mengirim pesan WhatsApp. (Pastikan akun Twilio dan nomor WhatsApp sudah benar.)
   - **Exit**: Keluar dari aplikasi.

## Catatan Keamanan

- **Jangan** commit informasi sensitif seperti kata sandi atau kunci API ke repositori. Gunakan file konfigurasi atau variabel lingkungan untuk menyimpan informasi sensitif.
- Jika Anda menggunakan `smtplib` untuk mengirim email, pastikan untuk tidak menyimpan kata sandi di dalam kode sumber. Sebaiknya gunakan file konfigurasi atau variabel lingkungan.

### Mengganti Kunci API dan Kata Sandi

Jika Anda mendapati informasi sensitif terkomit di repositori, segera lakukan perubahan pada kunci API atau kata sandi tersebut. Hapus informasi sensitif dari riwayat commit dengan menggunakan `git filter-repo` atau alat lain yang sesuai.

### Video Demo
https://drive.google.com/file/d/1PAm6OcuEGI7OB0GdGTd9TOwMJZuycv6i/view?usp=sharing

---
## Clone Repository
https://github.com/Putri1106/Tools-Cybersecurity.git
