from NodoABB import NodoABB
from graphviz import Digraph

g = Digraph('g', filename='ArbolUsuariosEspejo.gv')
g.node_attr.update(color='lightseagreen', style='filled')
g2 = Digraph('g2', filename='ArbolUsuarios2.gv')
class EspejoArbolBB:
    def __init__(self):
        self.raiz=None

    def vacio(self):
        if self.raiz==None:
            return True
        else:
            return False

    def insertar(self,valor,contrasenia):
        if self.vacio():
            self.raiz=NodoABB(valor=valor,contrasenia=contrasenia, es_raiz=True)
        else:
            nodo = self.__get_lugar(valor)
            if valor <= nodo.valor:
                nodo.izquierda=NodoABB(valor=valor,contrasenia=contrasenia, padre=nodo,es_izquierda=True)

            else:
                nodo.derecha=NodoABB(valor=valor,contrasenia=contrasenia, padre=nodo,es_derecha=True)

    def insertar1(self,valor,contrasenia,conectado):
        if self.vacio():
            self.raiz=NodoABB(valor=valor,contrasenia=contrasenia,conectado=conectado, es_raiz=True)
        else:
            nodo = self.__get_lugar(valor)
            if valor <= nodo.valor:
                nodo.derecha=NodoABB(valor=valor,contrasenia=contrasenia, conectado=conectado, padre=nodo,es_izquierda=True)
                g.node(nodo.valor,nodo.valor+"\\n"+nodo.contrasenia)
                g.node(nodo.derecha.valor,nodo.derecha.valor+"\\n"+nodo.derecha.contrasenia)
                g.edge(nodo.valor,nodo.derecha.valor)
                #g.node(nodo.lista,nodo.lista.dato)
                #g.edge(nodo.izquierda.valor,nodo.lista)
            else:
                nodo.izquierda=NodoABB(valor=valor,contrasenia=contrasenia, conectado=conectado, padre=nodo,es_derecha=True)
                g.node(nodo.valor,nodo.valor+"\\n"+nodo.contrasenia)
                g.node(nodo.izquierda.valor,nodo.izquierda.valor+"\\n"+nodo.izquierda.contrasenia)
                g.edge(nodo.valor,nodo.izquierda.valor)
                #g.node(nodo.lista,nodo.lista.dato)
                #g.edge(nodo.derecha.valor,nodo.lista)

    def graficarABB(self):
        g.view()
        return True
    
            
    def __get_lugar(self,valor):
        aux=self.raiz
        while aux:
            temp=aux
            if valor<=aux.valor:
                aux=aux.derecha
            else:
                aux=aux.izquierda
        return temp               

    def grafica2ABB(self,nodo):
        if nodo:
            #print "*******************"
            self.grafica2ABB(nodo.izquierda)
            g2.edge(str(nodo.padre),str(nodo.valor))
            self.grafica2ABB(nodo.derecha)
            #g2.edge(nodo.padre,nodo.valor)
        g2.view()
    
    def mostrarEnOrdenABB(self, nodo):
        if nodo:
            self.mostrarEnOrdenABB(nodo.izquierda)
            #izquierda-raiz-derecha
            print nodo.valor+" "+nodo.contrasenia+" "+str(nodo.conectado)
            self.mostrarEnOrdenABB(nodo.derecha)

    def mostrarEnPosOden(self,nodo):
        #izquierda-derecha-raiz
        if nodo:
            self.mostrarEnPosOden(nodo.izquierda)
            self.mostrarEnPosOden(nodo.derecha)
            print nodo.valor