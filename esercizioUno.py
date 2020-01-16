


import random

#funzione che permette la distanza di 9 posizioni da un numero ad un altro
def novePause(arrayNumeri):
    j = 0
    for j in range (0,9):
        arrayNumeri.append("*")

    return(arrayNumeri)


#array numeri
numeri = []


#primo inserimento
i = 0
firstNum= random.randint(0,9)
numeri.insert(i,firstNum)
novePause(numeri)
i=i+10

secNum = random.randint(0,9)

if(numeri[0] == secNum):
    print(numeri[0])
    print("non sono ammessi numeri uguali consecutivi\n")
else:
    numeri.insert(i, secNum)
    novePause(numeri)
    i=i+10

    #inserimenti successivi al primo
    while(len(numeri)<70):
        #numeri generati randomicamente tra 0 e 9
        newNum = random.randint(0,9)
        if(numeri[i-10] == newNum):
            print('non sono ammessi numeri uguali consecutivi\n')
            print('fine')
            break
        numeri.insert(i,newNum)
        novePause(numeri)
        i=i+10

print(len(numeri))
print(numeri)
print('FINE')