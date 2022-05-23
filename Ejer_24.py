'''
Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:
a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
uno la cima de la pila;
b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
'''
from pila import Pila

#funcion para saber en que posicion esta un determinado personaje(tomando como posicion 1 la cima)
def posicion_de_un_personaje_x(pila, name1):
    posicion=0
    posicion_aux=0
    pila_aux=Pila()
    while(pila.pila_vacia()== False) and (posicion==0):  #mientras la pila este vacia o no se haya encontrado el personaje se repitira el bucle
        dato=pila.desapilar()
        posicion_aux+=1
        if (dato.nombre== name1):
            posicion= posicion_aux
        pila_aux.apilar(dato)
    #lo volvemos a guardar en la pila original  
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())

    if posicion!=0:    
        return posicion
    else:
        return print('no se encontro el personaje')


#funcion para mostrar personajes con pelis mayor a una cantidad x
def personaje_que_participo_mas_de_x_canti_de_pelis(pila, cantidad):
    pila_aux=Pila()
    while(pila.pila_vacia()== False):
        dato=pila.desapilar()
        if (dato.cantidad_de_peli_de_la_saga_en_que_participo> cantidad):
            print('personaje con cantidad de pelis mayores a: ', cantidad,' es: ', dato.nombre)
            print('cantidad de peliculas: ', dato.cantidad_de_peli_de_la_saga_en_que_participo)   
        pila_aux.apilar(dato)
    #lo volvemos a guardar en la pila original  
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())

#funcion para saber en cuantas pelis participo un personaje
def cantidad_de_pelis_de_un_personaje(pila, name):
    pila_aux=Pila()
    encontro=False
    while((pila.pila_vacia()== False) and (encontro==False)):
        dato=pila.desapilar()
        if (dato.nombre== name):
            encontro=True
            print('el personaje', name,' participo en peliculas con una cantidad de: ', dato.cantidad_de_peli_de_la_saga_en_que_participo)   
        pila_aux.apilar(dato)
    #lo volvemos a guardar en la pila original  
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())

#funcion para mostra un personaje que empieza con determinada letra
def encontrar_personaje_apartir_de_una_letra(pila, letra):
    pila_aux=Pila()
    while(pila.pila_vacia()== False):
        dato=pila.desapilar()
        if (dato.nombre[0:1]== letra):      
            print('el personaje cuyo nombre empieza con: ', letra,' es:', dato.nombre)  
        pila_aux.apilar(dato)
    #lo volvemos a guardar en la pila original  
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())

#clase de personaje
class Personaje():
    nombre, cantidad_de_peli_de_la_saga_en_que_participo= None, None

pila_de_personajes= Pila()
personaje_aux= Personaje()

#pilas ya cargada
personaje_aux.nombre = 'carlos'
personaje_aux.cantidad_de_peli_de_la_saga_en_que_participo = 3
pila_de_personajes.apilar(personaje_aux)

personaje_aux = Personaje()
personaje_aux.nombre = 'Rocket Raccoon'
personaje_aux.cantidad_de_peli_de_la_saga_en_que_participo = 6
pila_de_personajes.apilar(personaje_aux)

personaje_aux = Personaje()
personaje_aux.nombre = 'dante'
personaje_aux.cantidad_de_peli_de_la_saga_en_que_participo = 5
pila_de_personajes.apilar(personaje_aux)

personaje_aux = Personaje()
personaje_aux.nombre = 'lauti'
personaje_aux.cantidad_de_peli_de_la_saga_en_que_participo = 8
pila_de_personajes.apilar(personaje_aux)

personaje_aux = Personaje()
personaje_aux.nombre = 'Black Widow'
personaje_aux.cantidad_de_peli_de_la_saga_en_que_participo = 10
pila_de_personajes.apilar(personaje_aux)

print('a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;')
print(posicion_de_un_personaje_x(pila_de_personajes, 'Rocket Raccoon'))

print('b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;')
personaje_que_participo_mas_de_x_canti_de_pelis(pila_de_personajes, 5)

print('c. determinar en cuantas películas participo la Viuda Negra (Black Widow);')
cantidad_de_pelis_de_un_personaje(pila_de_personajes, 'Black Widow')

print('d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.')
encontrar_personaje_apartir_de_una_letra(pila_de_personajes, 'c')
encontrar_personaje_apartir_de_una_letra(pila_de_personajes, 'd')
encontrar_personaje_apartir_de_una_letra(pila_de_personajes, 'g')



