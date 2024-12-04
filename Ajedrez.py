from random import randint

def cant08():
    numero=int(randint(0,8))
    return numero
def cant02():
    numero=int(randint(0,2))
    return numero
def cant01():
    numero=int(randint(0,1))
    return numero

cantPn=cant08()
print('La cantidad de peones negros :'+str(cantPn))
cantPb=cant08()
print('La cantidad de peones blancos :'+str(cantPb))
cantCn=cant02()
print('La cantidad de caballos negros :'+str(cantCn))
cantCb=cant02()
print('La cantidad de caballos blancos :'+str(cantCb))
cantAn=cant02()
print('La cantidad de alfiles negros :'+str(cantAn))
cantAb=cant02()
print('La cantidad de alfiles blancos :'+str(cantAb))
cantTn=cant02()
print('La cantidad de torres negras :'+str(cantTn))
cantTb=cant02()
print('La cantidad de torres blancas :'+str(cantTb))
cantRn=cant01()
print('La cantidad de reinas negras :'+str(cantRn))
cantRb=cant01()
print('La cantidad de reinas blancas :'+str(cantRb))

valorN=cantPn*1+cantCn*3+cantAn*3+cantTn*5+cantRn*9+4
print('El valor de las piezas negras en juego es: '+str(valorN))
valorB=cantPb*1+cantCb*3+cantAb*3+cantTb*5+cantRb*9+4
print('El valor de las piezas blancas en juego es: '+str(valorB))

if valorN > valorB:
    print('Ganaron las negras')
elif valorB > valorN:
    print('Ganaron las blancas')
else:
    print('Empataron')

LNegras=[]
LBlancas=[]

for i in range(cantPn):
    if cantPn >0:
        LNegras.insert(i,'Pn')
for i in range(cantCn):
    if cantCn>0:
        LNegras.insert(i,'Cn')
for i in range(cantAn):
    if cantAn>0:
        LNegras.insert(i,'An')
for i in range(cantTn):
    if cantTn>0:
        LNegras.insert(i,'Tn')
for i in range(cantRn):
        LNegras.insert(i,'Rn')
for i in range(1):
        LNegras.insert(i,'ReyN')

print('Las fichas negras en juego son : ', LNegras)

for i in range(cantPb):
    if cantPb >0:
        LBlancas.insert(i,'Pb')
for i in range(cantCb):
    if cantCb>0:
        LBlancas.insert(i,'Cb')
for i in range(cantAb):
    if cantAb>0:
        LBlancas.insert(i,'Ab')
for i in range(cantTb):
    if cantTb>0:
        LBlancas.insert(i,'Tb')
for i in range(cantRb):
        LBlancas.insert(i,'Rb')
for i in range(1):
        LBlancas.insert(i,'ReyB')

print('Las fichas Blancas en juego son : ', LBlancas)

LFichasEnJuego=[]

for i in range(len(LNegras)):
    LFichasEnJuego.append(LNegras[i])

for i in range(len(LBlancas)):
    LFichasEnJuego.append(LBlancas[i])

print('Listado de fichas en juego :' ,LFichasEnJuego)
print('La cantidad de piezas en juego son:',len(LFichasEnJuego))
cargaDeTablero=[]


for i in range (64):
    cargaDeTablero.insert(i,'vacio')
print('Tablero vacio: ')
print(cargaDeTablero)
    
for i in range (0,len(LFichasEnJuego)):
    posicion=randint(0,63)
    print(posicion)
    if cargaDeTablero[posicion]=='vacio':
        cargaDeTablero[posicion]=LFichasEnJuego[i]
    

#print('Posicion de rey blanco: ')
#print(cargaDeTablero.index('ReyB'))

print('la cantidad de items de la lista cargaDeTablero es:')
print(len(cargaDeTablero))
print(cargaDeTablero)


indiceReyB=cargaDeTablero.index('ReyB')
posicionReyB=indiceReyB+1
print('La posicion del rey blanco es: ',str(posicionReyB))
print ('EL indice del rey blanco es:',str(indiceReyB))

indiceReyN=cargaDeTablero.index('ReyN')
posicionReyN=indiceReyN+1
print('La posicion del rey negro es: ',str(posicionReyN))
print ('EL indice del rey negro es:',str(indiceReyN))













    






    






    



    




















