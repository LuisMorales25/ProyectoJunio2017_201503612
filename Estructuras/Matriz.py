from NodoMatriz import NodoMatriz

class matriz:
	def __init__(self):
		self.m=None

	def crear(self,fila,columna):
		self.m=NodoMatriz(0,0,0)
		self.m.sigfil=self.m
		self.m.sigcol=self.m
		i=1
		q=self.m
		while i<=fila:
			nuevoNodo=NodoMatriz(0,i,0)
			q.sigfil=nuevoNodo
			nuevoNodo.sigcol=nuevoNodo
			q=nuevoNodo
			i+=1
		q.sigfil=self.m
		i=1
		q=self.m
		while i<=columna:
			nuevoNodo=NodoMatriz(0,0,i)
			q.sigcol=nuevoNodo
			nuevoNodo.sigfil=nuevoNodo
			q=nuevoNodo
			i+=1
		q.sigcol=self.m

	def imprimir(self, nodo):
		nca=0
		ncc=0
		nt=0
		aux=nodo.sigcol
		print str(nodo.valor) +" "
		while aux.columna!=nodo.columna:
			print str(aux.columna)+" "
			aux=aux.sigcol
		print ""
		aux=nodo.sigfil
		while aux.fila!=nodo.fila:
			print str(aux.fila)+" "
			o=aux
			e=aux.sigcol
			while o!=e:
				nc=e.columna
				nt=nc
				nf=e.fila
				if nf==nca:
					nc=nc-ncc
				for x in range(nc):
					print " "
				print e.valor+" "
				e=e.sigcol
				nca=nf
				ncc=nt
			print" "
			aux=aux.sigfil



