parrafo = 'La educación EN valores es fundamental para cualquier persona,pues lo que aprendemos en los primeros  infruye en el prisma con el vemos el mundo'



listapalabras = parrafo.split()

frecuenciapalab = [listapalabras.count(w) for w in listapalabras]

print("parrafo\n" + parrafo +"\n")
print("contador\n" + str(list(zip(listapalabras, frecuenciapalab))))

def contar(parrafo):
    contar = {'minusculas':0, 'mayusculas': 0}

    for listapalabras in parrafo:
        if listapalabras.isupper():
            contar ['mayusculas'] += 1
        elif listapalabras.islower():
            contar ['minusculas'] += 1
    return contar
    