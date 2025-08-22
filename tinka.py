
import random


#creo lista de los numeros ganadores
def num_gan(): 
    n_g=list()
    while len(n_g) < 6:
        numero=random.randint(1, 36)   
        if numero not in n_g:
            n_g.append(numero)
            continue
    return n_g


#crear lista de los numeros ingresados
def num_ing():     
    n_i=list()
    print("Ingrese 6 numeros entre 1 y 36, sin repetirlos.")
    while len(n_i) < 6:
        n=int(input("Ingrese su numero: "))
        if n not in n_i and 1<=n<=36:
            n_i.append(n)
    
        else:
            print("Numero invalido o repetido. Intente de nuevo.")
            continue

    return n_i

#comparar numeros 
def comparar(n,y):
    
    c=0
    for x in range(len(n)):
        if n[x] in y:  
            c=c+1

    print("Numeros ganadores:")
    print(n)
    print("Numeros ingresados:")
    print(y)
    return c
    

print("===== Bienvenido a La Tinka =====")

aciertos = comparar(num_gan(), num_ing())

print("Su numero de aciertos fue:", aciertos)
if 1 < aciertos <= 3:
    print("Usted ha ganado otro Intento")

if aciertos == 4:
    print("USTED HA GANADO 5000 SOLES")

if aciertos == 5:
    print("USTED HA GANADO 10000 SOLES")

if aciertos == 6:
    print("USTED HA EL PREMIO MAYOR ")
    print("!! 7 MILLONES DE SOLES !!")
    print("!! FELICITACIONES !!")
else:
    print("Lo sentimos, no ha ganado esta vez.")