# Tugas Kecil III IF2211 Strategi Algoritma
Implementasi Algoritma A* untuk Menentukan Lintasan Terpendek

## Deskripsi Singkat
Program ini dapat menentukan lintasan terpendek dari suatu titik ke titik lain menggunakan prinsip algoritma A* (A star). Program menerima input berupa file berisi jumlah sipul, koordinat masing-masing simpul, dan matriks ketetanggaan. Setelah itu, program akan meminta masukan simpul awal dan simpul tujuan kemudian menampilkan hasil pencarian rute beserta visualisasinya menggunakan graf/peta.

Contoh input file graf adalah :
```
12
-6.884893 107.611445 A
-6.885191 107.613017 B
-6.885257 107.613733 C
-6.887256 107.611540 D
-6.887386 107.613611 E
-6.887910 107.608289 F
-6.893882 107.608450 G
-6.893230 107.610447 H
-6.893605 107.611944 I
-6.893780 107.613036 J
-6.894759 107.611723 K
-6.894883 107.608839 L
0 1 0 1 0 0 0 0 0 0 0 0
1 0 1 1 0 0 0 0 0 0 0 0
0 1 0 0 1 0 0 0 0 0 0 0
1 1 0 0 1 1 0 0 0 0 0 0
0 0 1 1 0 0 0 0 0 1 0 0
0 0 0 1 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 1 0 0 0 1
0 0 0 0 0 0 1 0 1 0 0 0
0 0 0 0 0 0 0 1 0 1 1 0
0 0 0 0 1 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 1 0 0 1
0 0 0 0 0 0 1 0 0 0 1 0
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
