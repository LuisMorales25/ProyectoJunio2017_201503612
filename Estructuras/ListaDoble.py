from NodoListaDoble import Nodo
from graphviz import Digraph

g = Digraph('g', filename='lista.gv', node_attr={'shape': 'record', 'style':'filled', 'fillcolor': 'skyblue','height': '.1'})
#g.node_attr.update(color='lightblue2', style='filled')
class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero=None
        self.Ultimo=None

    def vacia(self):
        if self.primero==None:
            return True
        else:
            return False

    def agregar_inicio(self,dato,oponente,totalTiros,tirosAcertados,tirosFallados,gano,damage):
        if self.vacia():
            self.primero = self.Ultimo=Nodo(dato,oponente,totalTiros,tirosAcertados,tirosFallados,gano,damage)
        else:
            aux=Nodo(dato,oponente,totalTiros,tirosAcertados,tirosFallados,gano,damage)
            aux.siguiente=self.primero
            self.primero.anterior=aux
            self.primero=aux
            #g.edge(self.Ultimo.anterior,self.Ultimo)
        #self.__unirNodos()

    def Graficar(self):
            temporal = self.primero            
            while temporal != None:
               # archi.write('node'+str(contador)+'[label="' + str(temporal.NombreOponente)+ '"];\n')
                if temporal.siguiente != None:
                   #g.node(temporal.oponente,"user: "+temporal.dato+"\\n oponente: "+temporal.oponente+"\\n total de tiros: "+temporal.totalTiros+"\\n tiros acertados: "+temporal.tirosAcertados+"\\n tiros fallados: "+temporal.tirosFallados+"\\n gano: "+temporal.gano+"\\n danio: "+temporal.damage)
                   #g.node(temporal.siguiente.oponente,"user: "+temporal.siguiente.dato+"\\n oponente: "+temporal.siguiente.oponente+"\\n total de tiros: "+temporal.siguiente.totalTiros+"\\n tiros acertados: "+temporal.siguiente.tirosAcertados+"\\n tiros fallados: "+temporal.siguiente.tirosFallados+"\\n gano: "+temporal.siguiente.gano+"danio:"+temporal.siguiente.damage)
                   g.node(temporal.oponente,"user: "+temporal.dato+"|| oponente: "+temporal.oponente+"|| total de tiros: "+temporal.totalTiros+"|| tiros acertados: "+temporal.tirosAcertados+"|| tiros fallados: "+temporal.tirosFallados+"|| gano: "+temporal.gano+"|| danio: "+temporal.damage)
                   g.node(temporal.siguiente.oponente,"user: "+temporal.siguiente.dato+"|| oponente: "+temporal.siguiente.oponente+"|| total de tiros: "+temporal.siguiente.totalTiros+"|| tiros acertados: "+temporal.siguiente.tirosAcertados+"|| tiros fallados: "+temporal.siguiente.tirosFallados+"|| gano: "+temporal.siguiente.gano+"danio:"+temporal.siguiente.damage)
                   g.edge(temporal.oponente, temporal.siguiente.oponente)
                   g.edge(temporal.siguiente.oponente,temporal.oponente)
                temporal = temporal.siguiente

            g.view()

    def agregar_final(self, dato,totalTiros,tirosAcertados,tirosFallados,damage):
        if self.vacia():
            self.primero=self.Ultimo=Nodo(dato,totalTiros,tirosAcertados,tirosFallados,damage)
        else:
            aux=self.Ultimo
            self.Ultimo=aux.siguiente=Nodo(dato,totalTiros,tirosAcertados,tirosFallados,damage)
            self.Ultimo.anterior=aux
        #self.__unirNodos()

    def __unirNodos(self):
        if self.primero != None:
            self.primero.anterior=self.Ultimo
            self.Ultimo.siguiente=self.primero

    def recorrer_inicio_fin(self):
        aux=self.primero
        while aux:
            print(aux.dato+" "+aux.oponente+" "+aux.totalTiros+" "+aux.tirosAcertados+" "+aux.tirosFallados+" "+aux.gano+" "+aux.damage)
            aux=aux.siguiente
            if aux==self.primero:
                break
       #print self.primero.dato  

   

 

    def recorrer_fin_inicio(self):
        aux=self.Ultimo
        while aux:
            print(aux.dato)
            aux=aux.anterior
            if aux==self.Ultimo:
                break
        print self.Ultimo.dato

    def eliminar_inicio(self):
        if self.vacia():
            print "estructura vacia"
        elif self.primero==self.Ultimo:
            self.primero=self.Ultimo=None
        else:
            self.primero=self.primero.siguiente
        self.__unirNodos()

    def eliminar_ultimo(self):
        if self.vacia():
            print "estructura vacia"
        elif self.Ultimo==self.primero:
            self.Ultimo=self.primero=None
        else:
            self.Ultimo=self.Ultimo.anterior
        self.__unirNodos()

    def buscar(self,dato):
        aux =self.primero
        while aux:
            if aux.dato==dato:
                return True
            else:
                aux=aux.siguiente
                if aux==self.primero:
                    return False

    def buscar1(self,nodo,dato):
        aux =nodo.primero
        while aux:
            if aux.dato==dato:
                return nodo
            else:
                aux=aux.siguiente
                if aux==self.primero:
                    return False

