from flask import Flask,request,Response
from ABB import ArbolBB
from MatrizDispersa import MatrizDispersa
from ListaDoble import ListaDoblementeEnlazada

arbol=ArbolBB()
listajuegos=ListaDoblementeEnlazada()
usuario1=""
Usuario2=""
app = Flask("proyecto1")

@app.route('/insertarArbol',methods=['POST']) 
def h():
    parametroPython = str(request.form['user'])
    parametroPython2 = str(request.form['password'])
    parametroPython3 = str(request.form['estado'])
    if arbol.buscar(arbol.raiz,parametroPython)!=True:
    	arbol.insertar1(parametroPython,parametroPython2,parametroPython3)
    	print "**************"
    	arbol.mostrarEnOrdenABB(arbol.raiz)
    	#arbol.graficarABB()
    	print "**************"
    	return "valido"
    else:
    	print "usuario ya existe"
    	return "False"

@app.route('/insertarArbol1',methods=['POST']) 
def h1():
    parametroPython = str(request.form['user'])
    parametroPython2 = str(request.form['password'])
   # parametroPython3 = str(request.form['estado'])
    if arbol.buscar(arbol.raiz,parametroPython)!=True:
    	arbol.insertar(parametroPython,parametroPython2)
    	print "**************"
    	arbol.mostrarEnOrdenABB(arbol.raiz)
    	print "**************"
    	return "valido"
    else:
    	print "usuario ya existe"
    	return "False"

@app.route('/verificarPassword',methods=['POST']) 
def v():
    parametroPython = str(request.form['user'])
    parametroPython2 = str(request.form['password'])
    auxLista=arbol.buscar1(arbol.raiz,parametroPython)
    if auxLista!=None:
    #	auxLista.lista=ListaDoblementeEnlazada()
    	print "Usuario valido"
        return "prueba"
    else:
    	print "usuario invalido"
    	return "False"

@app.route('/juego',methods=['POST']) 
def j():
    var=str(request.form['user'])
    var2=str(request.form['oponente'])
    var3=str(request.form['realizados'])
    var4=str(request.form['acertados'])
    var5=str(request.form['fallados'])
    var7=str(request.form['gano'])
    var6=str(request.form['danio'])
    auxLista=arbol.buscar1(arbol.raiz,var)
    #if listajuegos.vacia():
    #	listajuegos.agregar_inicio(var,var2,var3,var4,var5,var6,var7)
    #	listajuegos.recorrer_inicio_fin()
    if auxLista!=None:
    	auxLista.lista.agregar_inicio(var,var2,var3,var4,var5,var6,var7)
    	auxLista.lista.recorrer_inicio_fin()
    	#auxLista.lista.Graficar()
    	print "*****************"
    	print arbol.raiz.lista.recorrer_inicio_fin()
    	#auxLista.lista.Graficar()
    	return "valido"
    else:
    	print "el usuario no existe"
    	return "false"
    

@app.route('/juegoActual',methods=['POST']) 
def ja():
	user1=str(request.form['user'])
	user2=str(request.form['user2'])
	ejeX=int(request.form['ejeX'])
	ejeY=int(request.form['ejeY'])
	aux1=arbol.buscar1(arbol.raiz,user1)
	aux2=arbol.buscar1(arbol.raiz,user2)
	usuario1=user1
	Usuario2=user2
	#print str(aux1) + " " +str(aux2)
	#return "true"
	if aux1!=None and aux2!=None:
		#print user1+" joder"
		aux1.matriz.m1=MatrizDispersa()
		aux1.matriz.m2=MatrizDispersa()
		aux1.matriz.m3=MatrizDispersa()
		aux1.matriz.m4=MatrizDispersa()
		aux1.matriz.m1.CrearMatriz(ejeX,ejeY)
		aux1.matriz.m2.CrearMatriz(ejeX,ejeY)
		aux1.matriz.m3.CrearMatriz(ejeX,ejeY)
		aux1.matriz.m4.CrearMatriz(ejeX,ejeY)
		aux1.matriz.m1.Imprimir(aux1.matriz.m1.m)
		aux1.matriz.m2.Imprimir(aux1.matriz.m2.m)
		aux1.matriz.m3.Imprimir(aux1.matriz.m3.m)
		aux1.matriz.m4.Imprimir(aux1.matriz.m4.m)
		print"************segundo usuario**************"
		aux2.matriz.m1=MatrizDispersa()
		aux2.matriz.m2=MatrizDispersa()
		aux2.matriz.m3=MatrizDispersa()
		aux2.matriz.m4=MatrizDispersa()
		aux2.matriz.m1.CrearMatriz(ejeX,ejeY)
		aux2.matriz.m2.CrearMatriz(ejeX,ejeY)
		aux2.matriz.m3.CrearMatriz(ejeX,ejeY)
		aux2.matriz.m4.CrearMatriz(ejeX,ejeY)
		aux2.matriz.m1.Imprimir(aux2.matriz.m1.m)
		aux2.matriz.m2.Imprimir(aux2.matriz.m2.m)
		aux2.matriz.m3.Imprimir(aux2.matriz.m3.m)
		aux2.matriz.m4.Imprimir(aux2.matriz.m4.m)
		return "creada"
	else:
		print "cagada"
		return "false"

@app.route('/cubo',methods=['POST']) 
def cu():
	var1=str(request.form['user'])
	var2=str(request.form['col'])
	var3=str(request.form['fila'])
	var4=str(request.form['tipo'])
	var5=str(request.form['modo'])
	var6=str(request.form['direccion'])
	auxUser=arbol.buscar1(arbol.raiz,var1)
	if auxUser!=None:
		auxUser.matriz.cubo(var2,var3,var4,var5,var6)
		#if var4=="1":
	#		print "ingreso un satelite"
	
	print "sdsfa"
	return "aas"

@app.route('/bu',methods=['POST']) 
def bu():
	var1=str(request.form['user'])
	auxUser=arbol.buscar1(arbol.raiz,var1)
	if auxUser!=None:
		auxUser.lista.Graficar()
	return "hecho"

@app.route('/arbol',methods=['POST']) 
def ar():
	#var1=str(request.form['user'])
	arbol.graficarABB()
	return "true"

@app.route('/matriz',methods=['POST']) 
def ma():
	user1=str(request.form['user'])
	#user2=str(request.form['user2'])
	aux1=arbol.buscar1(arbol.raiz,user1)
	#aux2=arbol.buscar1(arbol.raiz,user2)
	#print str(aux1) + " " +str(aux2)
	#return "true"
	if aux1!=None:
		aux1.matriz.m1.Imprimir(aux1.matriz.m1.m)
		aux1.matriz.m2.Imprimir(aux1.matriz.m2.m)
		aux1.matriz.m3.Imprimir(aux1.matriz.m3.m)
		aux1.matriz.m4.Imprimir(aux1.matriz.m4.m)
		
		return "true"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')