# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:58:28 2021

@author: Dell
"""


#contoh paket makan

#Menu makan
#A = Nasi
#B = Ketang
#C = Jagung
#D = Ayam Bakar
#E = Rendang
#F = Cah Kangkung
#G = Sayur Asem
#H = Es Teh

Menu =  {'A':set(['B','H']),
         'B':set(['A','C','H']),
         'C':set(['B','D','E']),
         'D':set(['C','E','F','G','H']),

         'E':set(['C','D']),
         'F':set(['D','G']),
         'G':set(['F','G','H']),
         'H':set(['A','B','D','G'])}
    
def bfs(graf, mulai, paket):
    start = [[mulai]]
    entry = set()
    
    while start:
        # masukkan antrian paling depan ke variabel menu
        menu = start.pop(0)
        # simpan node yang dipilih ke variabel state, misal menu = B, H maka simpan A ke variabel state
        state = menu[-1]
    
        # cek state apakah sama dengan paket, jika ya maka return menu
        if state == paket:
            return menu
        # jika state tidak sama dengan paket, maka cek apakah state tidak ada di entry
        elif state not in entry:
        # jika state tidak ada di entry maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                menu_baru = list(menu) #masukkan isi dari variabel jalur ke variabel menu_baru
                menu_baru.append(cabang) #update atau tambah isi menu_baru dengan cabang
                start.append(menu_baru) #update atau tambah queue dengan menu_baru
                # tandai state yang sudah dikunjungi sebagai entry
            entry.add(state)

def dfs(graf, mulai, paket):
    start = [[mulai]]
    entry = set()

    while start:
        #hitung panjang tumpukan dan masukkan ke variabel panjang_tumpukan
        panjang_tumpukan = len(start)-1
        
        # masukkan tumpukan paling atas ke variabel menu
        menu = start.pop(panjang_tumpukan)

        # simpan node yang dipilih ke variabel state, misal menu = C,D maka simpan E ke variabel state
        state = menu[-1]

        # cek state apakah sama dengan menu, jika ya maka return paket
        if state == paket:
            return paket
        # jika state tidak sama dengan menu, maka cek apakah state tidak ada atau entry
        elif state not in entry:
            # jika state tidak ada di entry maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                menu_baru = list() #masukkan isi dari variabel menu ke variabel menu_baru
                menu_baru.append(cabang) #update atau tambah isi menu_baru dengan cabang
                start.append(menu_baru) #update atau tambah queue dengan menu_baru

            # tandai state yang sudah dikunjungi sebagai entry
            entry.add(state)
            #cek isi tumpukan
            isi = len(start)
            if isi == 0:
                print("Tidak ditemukan")
                
