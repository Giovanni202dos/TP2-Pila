'''
Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno,
desarrollar las funciones necesarias para resolver las siguientes actividades:
a. mostrar los nombre películas estrenadas en el año 2014;
b. indicar cuántas películas se estrenaron en el año 2018;
c. mostrar las películas de Marvel Studios estrenadas en el año 2016.
'''
from pila import Pila

#clase para las peliculas
class Pelicula():
    titulo, studio_cinematográfico, anio_de_estreno= None, None, None


#funcion para mostrar el titulo de de una peli estrenada en 2014
def mostrar_peli_estrenadas_en_2014(pila):  
    pila_aux= Pila()                        
    while(not pila.pila_vacia()):           
        dato = pila.desapilar()              
        if dato.anio_de_estreno== 2014:          
            print('la pelicula estrenada en 2014 es: ', dato.titulo)
        pila_aux.apilar(dato) 
    
    # finalmente lo desapilamos de la auxiliar para guardarla nuevamente en la original
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())

#funcion para contar cuantas peliculas se estrenaron en cierto anio
def cantidad_de_peliculas_estrenadas_en_un_anio_determinado(pila, anio):
    contador=0
    pila_aux= Pila()
    while(not pila.pila_vacia()):
        dato = pila.desapilar()
        if dato.anio_de_estreno== anio:
            contador+=1
            print('la pelicula estrenada en', anio, ' es: ', dato.titulo)
        pila_aux.apilar(dato)

    #desapilamos de la auxiliar para volver a guardarlo en la original
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())
    return contador

#funcion para mostrar las pelis con un studio cinematografico x en el anio x
def mostrar_peli_con_un_studio_cinemat_x_con_anio_x(pila, studio, anio):
    pila_aux= Pila()
    while(not pila.pila_vacia()):
        dato = pila.desapilar()
        if (dato.studio_cinematográfico== studio) and (dato.anio_de_estreno== anio):
            print('las peliculas hechas en el studio', studio,' y anio ', anio, ' es: ', dato.titulo)
        pila_aux.apilar(dato)

    #desapilamos de la auxiliar para volver a guardarlo en la original
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())
    
      
#pila donde van a estar apiladas varias pelicula
pila_peliculas= Pila()
#objeto de la clase pelicula que voy a usar para guardar la pelicula
pelicula_aux= Pelicula()

#peliculas ya cargadas
pelicula_aux.titulo = 'batman'
pelicula_aux.studio_cinematográfico = 'eeuuu'
pelicula_aux.anio_de_estreno= 2014
pila_peliculas.apilar(pelicula_aux)

pelicula_aux=Pelicula()     #se crea un nuevo objeto en memoria(porque sino lo punteros o ubicaciones se mezclan)
pelicula_aux.titulo = 'spider-man'
pelicula_aux.studio_cinematográfico = 'marvel studio'
pelicula_aux.anio_de_estreno = 2016
pila_peliculas.apilar(pelicula_aux)

pelicula_aux=Pelicula()
pelicula_aux.titulo = 'thor'
pelicula_aux.studio_cinematográfico = 'marvel studio'
pelicula_aux.anio_de_estreno = 2016
pila_peliculas.apilar(pelicula_aux)

mostrar_peli_estrenadas_en_2014(pila_peliculas)
print('cantidad de peliculas estrenadas', cantidad_de_peliculas_estrenadas_en_un_anio_determinado(pila_peliculas, 2016))
mostrar_peli_con_un_studio_cinemat_x_con_anio_x(pila_peliculas, 'marvel studio', 2016)