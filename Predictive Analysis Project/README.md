# Laporan Proyek Machine Learning - Yoan Rifqi Candra

## Domain Proyek

## Latar Belakang
Bank Mandiri (kode saham: BMRI) merupakan salah satu bank terbesar di Indonesia yang memiliki pengaruh besar terhadap sektor keuangan nasional. Sebagai perusahaan publik yang tercatat di Bursa Efek Indonesia (BEI), harga saham BMRI mencerminkan persepsi pasar terhadap kinerja perusahaan serta kondisi makroekonomi Indonesia secara keseluruhan. Dengan tingginya volume transaksi dan fluktuasi harga yang signifikan, prediksi harga saham BMRI menjadi topik yang menarik dan penting untuk investor, analis, maupun pengambil keputusan.

Masalah utama dalam dunia investasi adalah tingginya ketidakpastian pasar. Oleh karena itu, pengembangan model prediksi berbasis machine learning yang mampu mengidentifikasi pola historis dan tren masa depan dari harga saham dapat memberikan nilai tambah besar dalam pengambilan keputusan investasi.

Menurut studi oleh Atsalakis dan Valavanis (2009), penggunaan metode kecerdasan buatan seperti Artificial Neural Networks (ANN) dan Support Vector Machine (SVM) telah terbukti mampu meningkatkan akurasi dalam memprediksi harga saham dibandingkan pendekatan statistik konvensional. Oleh karena itu, penelitian ini akan mengeksplorasi model machine learning dalam memprediksi harga saham BMRI dengan fokus pada akurasi dan keandalan prediksi.

Referensi:
Atsalakis, G. S., & Valavanis, K. P. (2009). Surveying stock market forecasting techniques–Part II: Soft computing methods. Expert Systems with Applications, 36(3), 5932–5941.

## Business Understanding
### Problem Statements
1. Bagaimana tren harga saham BMRI berkembang dari waktu ke waktu?
2. Kapan waktu yang tepat untuk membeli atau menjual saham BMRI?
3. Bagaimana pengaruh volume transaksi terhadap volatilitas harga saham?
4. Bagaimana memprediksi harga saham BMRI di masa depan berdasarkan data historis?

### Goals
1. Menyediakan visualisasi tren historis saham BMRI untuk memberikan wawasan tentang arah pergerakan harga dalam jangka waktu tertentu.
2. Membantu investor menentukan waktu entry dan exit berdasarkan sinyal yang diperoleh dari analisis teknikal dan tren musiman.
3. Mengevaluasi hubungan antara volume transaksi dan harga untuk memahami apakah volume dapat menjadi indikator pendukung pengambilan keputusan.
4. Membangun model prediksi harga saham menggunakan Prophet untuk menghasilkan estimasi harga saham di masa depan.

## Data Understanding
### Sumber Data
Dataset yang digunakan berasal dari data historis harga saham PT Bank Mandiri (Persero) Tbk (kode: BMRI) yang diperoleh melalui platform Investing.com Indonesia. Data tersebut mencakup informasi harian mulai dari awal tahun hingga data terbaru tahun 2025.

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- Data : Tanggal pencatatan harga saham
- Open : Harga pembukaan pada hari tersebut
- High : Harga tertinggi dalam satu hari
- Low : Harga terendah dalam satu hari
- Close : Harga penutupan pada akhir hari
- Volume : Jumlah Saham yang diperdagang hari tersebut
- Change(%) : Selisih antara harga penutupan dan harga pembukaan pada hari tersebut


