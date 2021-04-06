# Tugas Kecil III IF2211 Strategi Algoritma
Implementasi Algoritma A* untuk Menentukan Lintasan Terpendek

## Deskripsi Singkat
Program ini dapat menentukan lintasan terpendek dari suatu titik ke titik lain menggunakan prinsip algoritma A* (A star). Program menerima input berupa file berisi jumlah sipul, koordinat masing-masing simpul, dan matriks ketetanggaan. Setelah itu, program akan meminta masukan simpul awal dan simpul tujuan kemudian menampilkan hasil pencarian rute beserta visualisasinya menggunakan graf/peta.

Contoh input file graf adalah :
```
8
-6.235536679520217 106.85527842250073 Smpn73
-6.233743889747193 106.85063836232926 NokiEsports
-6.230013827050964 106.85246231829736 WartegWarmo
-6.226889873483907 106.85824284564163 StasiunTebet
-6.242227419818099 106.85416610947357 SignaturePark
-6.242765361706683 106.8584218079315 StasiunCawang
-6.224294522153229 106.85139329929041 CervinoVillage
-6.23167178187699 106.84564704393786 McDonalds
0 0 0 0 0 0 1 0
0 1 0 0 1 0 1 1
1 1 1 1 0 1 1 0
0 0 1 0 0 1 0 0
0 0 1 1 1 0 0 1
0 1 1 1 0 0 1 1
1 0 0 1 0 1 1 1
1 1 0 0 0 0 1 0
```
Bobot graf menyatakan jarak antar simpul yang dihitung dengan rumus jarak Euclidean. Nilai heuristik yang dipakai didapat dari jarak garis lurus antara suatu simpul ke tujuan.


## Requirements
* Python 3.7 or higher (not tested on older Python version)
* Pip package installer for Python, biasanya sudah bawaan dari instalasi Python

## Instalasi & Cara Penggunaan
* Clone repository:
```
https://github.com/rayfazt/stima-astar.git
```
* Install requirements:
```
pip install -r requirements.txt
```
* Pergi ke folder src:
```
cd src
```
* Jalankan program (Windows):
```
python main.py
```
* Untuk Linux:
```
python3 main.py
```

Pastikan file test case dalam bentuk .txt dan penulisan isinya sesuai format yang telah diberikan.

## Author
* Rayhan Alghifari Fauzta (13519039)
* Raihan Astrada Fathurrahman (13519113)
