
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
    while len(n_i) < 6:
        n=int(input("Ingrese un numero entre 1 y 36: "))
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
    print(sorted(n))
    print(sorted(y))
    return c
    

print("juego de la tinka ")

print(comparar(num_gan(), num_ing()))