# inisiasi matrix
A = [[7,5]]
B = [[3],[8]]

# inisiasi hasil perkalian matriks
C = []

# mengetahui baris dan kolom
Baris_A = len(A)
Kolom_A = len(A[0])

Baris_B = len(B)
Kolom_B = len(B[0])
# Cetak details matriks
print (A)
print("Baris matriks A adalah ", Baris_A)
print("Kolom matriks A adalah ", Kolom_A)

print (B)
print("Baris matriks B adalah ", Baris_B)
print("Kolom matriks B adalah ", Kolom_B)

# cek kondisi Matrix untuk Perkalian
if (Kolom_A !=Baris_B):
    print ("Matriks A dengan B tidak dapat dikalikan")
else:
    print ("Matriks A dengan B dapat dikalikan dan hasilnya adalah: ")
    #print (A[0][0])
    #print (A[0][0])
    #print (A[0][1])
    #print (A[1][0])
    C=(A[0][0]*B[0][0])+(A[0][1]*B[1][0])
    print(C)
