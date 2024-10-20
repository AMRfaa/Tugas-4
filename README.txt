>>> FLOWCHART <<<
Link : https://drive.google.com/file/d/1XDzxE6Qb16QSaQ6tyvAj8pEPtFLcEeYA/view?usp=sharing

>>> PSEUDOCODE <<<

	begin
		var A is integer
		var B is integer
		var C is integer
		
		Baris_A = len(A)
		Kolom_A = len(A[0])
		Baris_B = len(B)
		Kolom_B = len(B[0])

		if kolom A != baris B
		  print " matriks tidak dapat dikalikan "

		else:
		  print " matriks A dan B bisa dikalikan "
		  for i in range(3):
	            for j in range(3):
	              for k in range(3): 
	                C[i][j] += A[i][k] * B[k][j]
		print "Hasil perkalian matriks A dan B:"
		for baris in C:
		    print(baris)    
	 end
