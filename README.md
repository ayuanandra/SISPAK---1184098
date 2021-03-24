# SISPAK---1184098

Breadth First Search (BFS) adalah algoritma yang melakukan pencarian ekstensif atau melebar. Pencarian pertama mengunjungi sebuah node, yaitu mengunjungi sebuah node terlebih dahulu, dan kemudian mengunjungi semua node yang berdekatan dengan node tersebut.
Depth First Search (DFS) adalah teknik untuk memperluas ke simpul paling dalam di tree.

Contoh paket makan

Variabel
A = Paket 1
B = Paket 2
C = Paket 3
D = Paket 4
E = Paket 5
F = Paket 6
G = Paket 7
H = Paket 8

Maka Menu makan, 
A = Nasi
B = Ketang
C = Jagung
D = Ayam Bakar
E = Rendang
F = Cah Kangkung
G = Sayur Asem
H = Es Teh

Menu =  {'A':set(['B','H']),
         'B':set(['A','C','H']),
         'C':set(['B','D','E']),
         'D':set(['C','E','F','G','H']),

         'E':set(['C','D']),
         'F':set(['D','G']),
         'G':set(['F','G','H']),
         'H':set(['A','B','D','G'])}

Dalam BFS Node diperlukan sebagai referensi untuk mengakses node tetangga. Setiap node yang dikunjungi memasuki antrian hanya sekali. 
Dalam DFS setelah mencapai level terdalam, jejak akan kembali ke level 1 sebelumnya untuk melacak simpul anak kedua di pohon biner simpul kanan, lalu kembali ke langkah sebelumnya dengan menelusuri simpul anak pertama ke level terdalam lagi , dan seterusnya.
