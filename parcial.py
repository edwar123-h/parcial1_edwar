parrafo = 'La educación en valores es fundamental para cualquier persona,pues lo que aprendemos en los primeros  infruye en el prisma con el vemos el mundo'



listapalabras = parrafo.split()

frecuenciapalab = [listapalabras.count(w) for w in listapalabras]

print("parrafo\n" + parrafo +"\n")
print("contador\n" + str(list(zip(listapalabras, frecuenciapalab))))