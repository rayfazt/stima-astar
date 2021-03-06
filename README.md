# Tugas Kecil III IF2211 Strategi Algoritma
Implementasi Algoritma A* untuk Menentukan Lintasan Terpendek

## Deskripsi Singkat
Program ini dapat menentukan lintasan terpendek dari suatu titik ke titik lain menggunakan prinsip algoritma A* (A star). Program menerima input berupa file berisi jumlah sipul, koordinat masing-masing simpul, dan matriks ketetanggaan berbobot. Setelah itu, program akan meminta masukan simpul awal dan simpul tujuan kemudian menampilkan hasil pencarian rute beserta visualisasinya menggunakan graf/peta.

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
0 0.17686726502403394 0 0.2632517439789043 0 0 0 0 0 0 0 0
0.17686726502403394 0 0.07946859144593632 0.28192895069042706 0 0 0 0 0 0 0 0
0 0.07946859144593632 0 0 0.23737731468051107 0 0 0 0 0 0 0
0.2632517439789043 0.28192895069042706 0 0 0.22933116685049545 0.3665819638890329 0 0 0 0 0 0
0 0 0.23737731468051107 0.22933116685049545 0 0 0 0 0 0.7145925075720253 0 0
0 0 0 0.3665819638890329 0 0 0.6650237807660428 0 0 0 0 0
0 0 0 0 0 0.6650237807660428 0 0.23232125564821227 0 0 0 0.11943352380600843
0 0 0 0 0 0 0.23232125564821227 0 0.17062232500909322 0 0 0
0 0 0 0 0 0 0 0.17062232500909322 0 0.12224166728949747 0.13076103083345564 0
0 0 0 0 0.7145925075720253 0 0 0 0.12224166728949747 0 0 0
0 0 0 0 0 0 0 0 0.13076103083345564 0 0 0.3190155925057135
0 0 0 0 0 0 0.11943352380600843 0 0 0 0.3190155925057135 0
```
Bobot graf menyatakan jarak antar simpul yang dihitung dengan rumus jarak Euclidean. Nilai heuristik yang dipakai didapat dari jarak garis lurus antara suatu simpul ke tujuan.


## Requirements
* Python 3.7 or higher (not tested on older Python version)

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
