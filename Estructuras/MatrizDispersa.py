from NodoMatrizDispersa import NodoMatrizDispersa
from graphviz import Digraph
g = Digraph('g', filename='matriz.gv', node_attr={'shape': 'record', 'style':'filled', 'fillcolor': 'seashell2','height': '.1'})
class MatrizDispersa(object):
	"""docstring for MatrizDispersa"""
	def __init__(self):
		self.m=None
		self.m1=None
		self.m2=None
		self.m3=None
		self.m4=None

	def CrearMatriz(self,f,c):
		#print(str(f) + " " + str(c))
		self.m=NodoMatrizDispersa(0,0,0)
		self.m.siguientefila=self.m
		self.m.siguientecol=self.m
		i=1
		q=self.m
		while (i<=f):
			nuevo=NodoMatrizDispersa(0,i,0)
			q.siguientefila=nuevo
			nuevo.siguientecol=nuevo
			q=nuevo
			i+=1
		q.siguientefila=self.m
		#print(str(self.m.dato))
		i=1
		q=self.m
		#print(str(q.dato)+" antes de while")
		while (i<=c):
			nuevo=NodoMatrizDispersa(0,0,i)
			q.siguientecol=nuevo
			nuevo.siguientefila=nuevo
			q=nuevo
			i+=1
		q.siguientecol=self.m
		#print(str(q.dato))

	def Arriba(self,f,c):
		aux=self.m.siguientecol
		while (aux.col!=c):
			aux=aux.siguientecol
		aux1=aux.siguientefila
		aux2=aux1.siguientefila
		while (aux1.fila<f and aux2.fila!=0):
			aux=aux1
			aux1=aux1.siguientefila
			aux2=aux2.siguientefila
		if (aux1.fila<f):
			return aux1
		else:
			return aux

	def Izquierda(self,f,c):
		aux=self.m.siguientefila
		while aux.fila!=f:
			aux=aux.siguientefila
		aux1=aux.siguientecol
		aux2=aux1.siguientecol
		while (aux1.col<0 and aux2.col!=0):
			aux	=aux1
			aux1=aux1.siguientecol
			aux2=aux2.siguientecol
		if aux1.col<c:
			return aux1
		else:
			return aux

	def Adicionar(self,dato,f,c):
		q=self.Arriba(f,c)
		p=self.Izquierda(f,c)
		nuevo=NodoMatrizDispersa(dato,f,c)
		nuevo.siguientefila=q.siguientefila
		q.siguientefila=nuevo
		nuevo.siguientecol=p.siguientecol
		p.siguientecol=nuevo

	def Imprimir(self,M):

		o=NodoMatrizDispersa(0,0,0)
		nca=ncc=nt=0
		e=NodoMatrizDispersa(0,0,0)
		aux=M.siguientecol
		print(str(M.dato)+" |"),
		#g.node("0",str(M.dato))
		auxcol=1
		#g.node(str(auxcol),str(auxcol))
		#g.edge("0",str(auxcol))
		#g.rankdir=LR		
		g.edge(("c"+str(M.dato)),("c"+str(aux.col)))
		while aux.col!=M.col:
			auxcol2=auxcol
			auxcol2+=1
			#g.node(str(auxcol2),str(auxcol2))
			#g.edge(str(auxcol),str(auxcol2))
			auxcol+=1
			print(str(aux.col)+" |"),#columna
			#g.rankdir=g.LR
			g.graph_attr['rankdir'] = 'LR'
			g.edge(("c"+str(aux.col)),("c"+str(aux.col+1)))
			aux=aux.siguientecol
		print("")
		aux=M.siguientefila
		auxfila=1
		nombrefila=100
		#g.node(str(nombrefila),str(auxfila))
		#g.edge("0",str(auxfila))
		#g.graph_attr['rankdir'] = 'TB'
		g.edge("c"+(str(M.dato)),("f"+str(aux.fila)))
		while aux.fila!=M.fila:
			print(str(aux.fila)	+" |"),
			auxfila2=auxfila
			auxfila2+=1
		#	g.edge(str(nombrefila),str(auxfila2))
			auxfila+=1
			nombrefila+=1
			#g.graph_attr['rankdir'] = 'TB'
			g.edge(("f"+str(aux.fila)),("f"+str(aux.fila+1)))
			o=aux
			e=aux.siguientecol
			while (o!=e):
				nc=e.col
				nt=nc
				nf=e.fila
				if nf==nca:
					nc=nc-ncc
				for x in xrange(1,nc):
					print("   "),
				print(str(e.dato)+"  "),
				g.edge(("f"+str(aux.fila)),("s"+str(e.dato)))
				g.edge(("c"+str(aux.col)),("s"+str(e.dato)))
				e=e.siguientecol
				nca=nf
				ncc=nt
			print(" ")
			aux=aux.siguientefila
	def graficarMatriz(self):
		g.view()
		return True

	def numerodecolumna(self,joder):
		columna=ord(joder)
		return (columna-64)

	def nave(self,columna,fila,tipo,modo,direccion):

		if tipo==1:#satelite
			self.Adicionar("s",fila,columna)
		elif tipo==2:#nave
			if modo==1:
				pass
			elif modo==2:
				pass
			else:
				pass
		elif tipo==3:#barco
			if direccion==1:#horizonatal
				columna=columna+1
				for x in range(modo):
					self.Adicionar(8,fila,columna)
					columna-=1
			elif direccion==2:#vertical
				fila=fila-1
				for x in range(modo):
					self.Adicionar(8,fila,columna)
					fila+=1
		elif tipo==4:#submarino
			if direccion==1:
				columna=columna+1
				for x in range(modo):
					self.Adicionar(8,fila,columna)
					columna-=1
			elif direccion==2:
				fila=fila-1
				for x in range(modo):
					self.Adicionar(8,fila,columna)
					fila+=1
			else:
				pass
		else:
			pass

	def cubo(self,columna,fila,tipo,modo,direccion):
		#self.m1=MatrizDispersa()#satelite
		#self.m2=MatrizDispersa()#avion
		#self.m3=MatrizDispersa()#barco
		#self.m4=MatrizDispersa()#submarino
		#self.m1.CrearMatriz(10,10)
		#self.m2.CrearMatriz(10,10)
		#self.m3.CrearMatriz(10,10)
		#self.m4.CrearMatriz(10,10)
		#columna=int(self.numerodecolumna(columna))
		#print self.numerodecolumna(columna)
		if direccion==None:
			direccion="0"
		columna=self.numerodecolumna(columna)
		if tipo==1:
			self.m1.Adicionar("s",fila,columna)
			print "satelite"
		elif tipo==2:
			print "avion"
			if modo==1:
				print"modo 1"
				self.m2.Adicionar("A",fila-1,columna)
				self.m2.Adicionar("A",fila,columna+1)
				self.m2.Adicionar("A",fila,columna)
				self.m2.Adicionar("A",fila,columna-1)
				self.m2.Adicionar("A",fila+1,columna)
				self.m2.Adicionar("A",fila+2,columna)
			elif modo==2:
				print "modo2"
				self.m2.Adicionar("A",fila,columna)
				self.m2.Adicionar("A",fila,columna-1)
				self.m2.Adicionar("A",fila+1,columna)
		elif tipo==3:
			print"barco"
			if direccion==1:#horizonatal
				print "horizontal"
				if modo==1 or modo==2:
					columna=columna
				else:
					columna=columna+1
				for x in range(modo):
					self.m3.Adicionar("B",fila,columna)
					columna-=1
			elif direccion==2:#vertical
				print"vertical"
				if modo==2 or modo==1:
					fila=fila
				else:
					fila=fila-1
				for x in range(modo):
					self.m3.Adicionar("B",fila,columna)
					fila+=1
		elif tipo==4:
			print "submarino"
			if direccion==1:#horizonatal
				print "horizontal"
				columna=columna+1
				for x in range(modo):
					self.m4.Adicionar(8,fila,columna)
					columna-=1
			elif direccion==2:#vertical
				print"vertical"
				fila=fila-1
				for x in range(modo):
					self.m4.Adicionar(8,fila,columna)
					fila+=1
		#self.m1.Imprimir(self.m1.m)
		#self.m2.Imprimir(self.m2.m)
		#self.m3.Imprimir(self.m3.m)
		#self.m4.Imprimir(self.m4.m)








