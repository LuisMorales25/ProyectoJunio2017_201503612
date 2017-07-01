from ABB import ArbolBB
from ListaDoble import ListaDoblementeEnlazada
from MatrizDispersa import MatrizDispersa
from arbolEspejo import EspejoArbolBB

lista=ListaDoblementeEnlazada()
lista.agregar_inicio("bart","faasd","5","15","3","si","bastante")
#lista.agregar_inicio("bart","faasd2","52","152","32","si2","bastante2")
lista.agregar_inicio("maria","faasd2","6","16","4","si","poco")
lista.agregar_inicio("zoom","faasd3","7","17","5","si","bastante")
#lista.agregar_inicio("joder4","faasd4","7","17","5","si","bastante")
lista.recorrer_inicio_fin()
lista.Graficar()

arbol=ArbolBB()
arbol.insertar1("luis","ad1",1)
arbol.insertar1("ale","ad2",0)
arbol.insertar1("pablo","ad3",0)
arbol.insertar1("maria","dfas",0)
arbol.insertar1("bart","ad4",0)
arbol.insertar1("zoom","qrw",0)
arbol.mostrarEnPosOden(arbol.raiz)
arbol.graficarABB()
#arbol.nivel(arbol.raiz)
#arbol.grafica2ABB(arbol.raiz)
print "*************"
arbolEspejo=EspejoArbolBB()
arbolEspejo.insertar1("luis","ad1",1)
arbolEspejo.insertar1("ale","ad2",0)
arbolEspejo.insertar1("pablo","ad3",0)
arbolEspejo.insertar1("maria","dfas",0)
arbolEspejo.insertar1("bart","ad4",0)
arbolEspejo.insertar1("zoom","qrw",0)
arbolEspejo.mostrarEnOrdenABB(arbolEspejo.raiz)
#arbolEspejo.graficarABB()
	
aux=arbol.buscar1(arbol.raiz,"bart").valor
aux2=lista.buscar(aux)
print aux2
#print arbol.raiz.conectado
##print ((arbol.buscar(arbol.raiz,"luis")).valor)
#arbol.modificar(arbol.raiz,"luis","carlos")
#print "datos nuevos"
#arbol.eliminar("pablo")
#print"ya se elimino pablo"
#arbol.mostrarEnOrdenABB(arbol.raiz)
#arbol.reporteABB(arbol.raiz)

ma=MatrizDispersa()
ma.CrearMatriz(5,5)
ma.Adicionar(3,2,4)#dato,fila,columna
#ma.Adicionar(1,1,4)
#ma.Adicionar(2,1,3)
#ma.Adicionar(3,1,1)
#ma.Adicionar(3,1,2)
#ma.Adicionar(4,2,2)
#ma.Adicionar(7,4,2)
#ma.Adicionar(8,4,3)
#ma.Adicionar(6,2,3)
#ma.Adicionar(4,3,3)
#ma.Adicionar(6,3,3)
#ma.Adicionar(10,20,15)
#ma.nave(7,1,1,1,1)
#ma.nave(2,2,3,3,1)
#ma.nave(5,7,3,3,2)#columna,fila,tipo,modo,direccion
##ma.Imprimir(ma.m)
#ma.graficarMatriz()
print "************"
"""
ma.m1=MatrizDispersa()#satelite
ma.m2=MatrizDispersa()#avion
ma.m3=MatrizDispersa()#barco
ma.m4=MatrizDispersa()#submarino
ma.m1.CrearMatriz(10,10)
ma.m2.CrearMatriz(10,10)
ma.m3.CrearMatriz(10,10)
ma.m4.CrearMatriz(10,10)
ma.cubo("B",1,1,1,None)
ma.cubo("J",3,3,1,1)
ma.cubo("H",3,4,3,2)
ma.cubo("C",5,1,1,1)
ma.cubo("D",8,1,1,1)
ma.cubo("G",2,3,3,2)
ma.cubo("E",6,3,3,1)
ma.cubo("B",7,4,3,1)
ma.cubo("B",3,2,1,0)
ma.cubo("H",5,2,2,0)
ma.m1.Imprimir(ma.m1.m)
ma.m2.Imprimir(ma.m2.m)
ma.m3.Imprimir(ma.m3.m)
ma.m4.Imprimir(ma.m4.m)
"""