import random

numeri = []
noveNumeri = []

#controlla se il numero generato è gia presente all'interno dell'array di appoggio
def confronto(numero,arrayNumeri):

    #se presente ne genera un altro e richiama se stessa ricorsivamente
    if(numero in arrayNumeri):
        newNumero = random.randint(0, 9)
        confronto(newNumero,arrayNumeri)
    else:
        #altrimenti aggiunge il numero all'array di appoggio
        arrayNumeri.append(numero)


#genera un intero random tra 0 e 9 e chiama il confronto
def addNum():
        numero = random.randint(0, 9)
        confronto(numero, noveNumeri)


for j in range(7):
    for i in range(10):
        addNum()
    #ogni 10 numeri inseriti diversi tra loro, si inserisce il contenuto nell'array numeri e si pulisce l'array di appoggio
    numeri=numeri + noveNumeri
    del noveNumeri[0:10]

print("\nla dimensione dell'array è:",len(numeri))
print("l'array è : \n",numeri)
print("\n FINE")
