class NodoMatrizDispersa(object):
	"""docstring for NodoMatrizDispersa"""
	def __init__(self,dato,fila,col):
		self.dato=dato
		self.fila=fila
		self.col=col
		self.siguientefila=None
		self.siguientecol=None

		