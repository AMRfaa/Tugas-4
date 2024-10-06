# inisisasi matriks
A = [[1,2,3],
     [3,2,1],
     [4,1,4]] 
B = [[3,2,1],
     [4,5,6],
     [3,1,2]]

# inisiasi hasil perkalian matriks
C = [[0,0,0],[0,0,0],[0,0,0]] 

# mengetahui baris dan kolom
Baris_A = len(A)
Kolom_A = len(A[0])

Baris_B = len(B)
Kolom_B = len(B[0])

# Cetak detail matriks
print (A)
print("Baris matriks A adalah ", Baris_A)
print("Kolom matriks A adalah ", Kolom_A)

print (B)
print("Baris matriks B adalah ", Baris_B)
print("Kolom matriks B adalah ", Kolom_B)

# cek kondisi Matrix untuk Perkalian
if (Kolom_A != Baris_B):
    print ("Matriks A dengan B tidak dapat dikalikan")
else:
     print ("Matriks A dengan B dapat dikalikan")  
     for i in range(3):
        for j in range(3):
            for k in range(3): 
               C[i][j] += A[i][k] * B[k][j]
print()
# output perkalian matriks
print("Hasil perkalian matriks A dan B:")
for row in C:
    print(row)    
   
