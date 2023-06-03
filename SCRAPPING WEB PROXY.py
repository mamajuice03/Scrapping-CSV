#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup as bs

URL = 'https://proxyway.com/reviews'

for page in range(1, 4):
    print("\n")
    print("Sub Titles Page:", page, "\n")

    req = requests.get(f'{URL}/page/{page}')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('h3', class_='archive-list__title')

    for i, title in enumerate(titles):
        print(f"{i+1} {title.text}")


# In[17]:


import csv
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://proxyway.com/reviews'

data = []

for page in range(1, 4):
    print("\n")
    print("Sub Titles Page:", page, "\n")

    req = requests.get(f'{URL}/page/{page}')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('h3', class_='archive-list__title')

    for i, title in enumerate(titles):
        print(f"{i+1} {title.text}")
        data.append({
            'Page Number': f'Page {page}',
            'Title Number': f'Title {i+1}',
            'Title Name': title.text
        })

# Menyimpan data ke dalam file CSV
filename = 'proxywaydata.csv'
fieldnames = ['Page Number', 'Title Number', 'Title Name']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("Data telah disimpan ke dalam file", filename)


# In[ ]:


Penjelasan kode In [2]:
    
1. Pertama, kode mengimpor modul requests untuk mengirim permintaan HTTP dan modul BeautifulSoup dari library bs4 untuk mem-parsing HTML.

2. URL yang akan di-scrape ditetapkan sebagai 'https://proxyway.com/reviews' dan disimpan dalam variabel URL.

3. Dilakukan perulangan untuk tiga halaman pertama dengan menggunakan for page in range(1, 4):.

4. Pada setiap iterasi, subjudul halaman yang sedang diproses dicetak dengan menggunakan print("Sub Titles Page:", page, "\n").

5. Dilakukan permintaan GET ke URL halaman tertentu dengan menggunakan requests.get(f'{URL}/page/{page}'). URL yang dikirimkan disesuaikan dengan nomor halaman saat ini.

6. Setelah mendapatkan respon dari permintaan, teks respon tersebut diubah menjadi objek BeautifulSoup dengan menggunakan bs(req.text, 'html.parser'). Ini memungkinkan untuk mem-parsing dan mengekstrak data dari halaman.

7. Dilakukan pencarian semua elemen <h3> dengan kelas CSS 'archive-list__title' di dalam halaman menggunakan find_all('h3', class_='archive-list__title'). Hasilnya disimpan dalam variabel titles.

8. Dilakukan perulangan untuk setiap elemen judul yang ditemukan dengan menggunakan for i, title in enumerate(titles):.

9. Pada setiap iterasi, nomor judul (berindeks dari 1) dan teks judulnya dicetak menggunakan print(f"{i+1} {title.text}").


# In[ ]:


Penjelasan kode In [17] :

1. Pertama, kode mengimpor modul csv untuk memungkinkan penulisan data ke file CSV, modul requests untuk mengirim permintaan HTTP, dan modul BeautifulSoup dari library bs4 untuk mem-parsing HTML.

2. URL yang akan di-scrape ditetapkan sebagai 'https://proxyway.com/reviews' dan disimpan dalam variabel URL.

3. Dibuat sebuah list kosong dengan nama data yang akan digunakan untuk menyimpan data yang akan ditulis ke file CSV.

4. Dilakukan perulangan untuk tiga halaman pertama dengan menggunakan for page in range(1, 4):.

5. Pada setiap iterasi, subjudul halaman yang sedang diproses dicetak dengan menggunakan print("Sub Titles Page:", page, "\n").

6. Dilakukan permintaan GET ke URL halaman tertentu dengan menggunakan requests.get(f'{URL}/page/{page}'). URL yang dikirimkan disesuaikan dengan nomor halaman saat ini.

7. Setelah mendapatkan respon dari permintaan, teks respon tersebut diubah menjadi objek BeautifulSoup dengan menggunakan bs(req.text, 'html.parser'). Ini memungkinkan untuk mem-parsing dan mengekstrak data dari halaman.

8. Dilakukan pencarian semua elemen <h3> dengan kelas CSS 'archive-list__title' di dalam halaman menggunakan find_all('h3', class_='archive-list__title'). Hasilnya disimpan dalam variabel titles.

9. Dilakukan perulangan untuk setiap elemen judul yang ditemukan dengan menggunakan for i, title in enumerate(titles):.

10. Pada setiap iterasi, nomor judul (berindeks dari 1) dan teks judulnya dicetak menggunakan print(f"{i+1} {title.text}"). Selain itu, data tersebut ditambahkan ke dalam list data dalam bentuk dictionary.

11. Setelah selesai mengumpulkan data dari tiga halaman, data tersebut akan disimpan ke dalam file CSV.

12. Ditentukan nama file CSV yang akan digunakan sebagai proxywaydata.csv.

13. Ditentukan nama-nama field (kolom) dalam file CSV sebagai fieldnames.

14. Dibuka file CSV dengan menggunakan pernyataan with open(filename, 'w', newline='') as csvfile:. Ini akan memastikan bahwa file CSV akan ditutup setelah penggunaan.

15. Membuat objek writer dari csv.DictWriter dengan menggunakan writer = csv.DictWriter(csvfile, fieldnames=fieldnames). Ini memungkinkan penulisan data ke file CSV dalam format dictionary.

16. Menulis header kolom ke file CSV menggunakan writer.writeheader().

17. Menulis data ke file CSV menggunakan writer.writerows(data). Data yang telah dikumpulkan dari tiga halaman akan ditulis dalam bentuk baris-baris di file CSV.

18. Setelah semua data ditulis ke file CSV, cetak pesan yang mengkonfirmasi bahwa data telah disimpan ke dalam file dengan menggunakan print("Data telah disimpan ke dalam file", filename).

