from flask import Flask,request,Response
from ABB import ArbolBB

arbol=ArbolBB()

app = Flask("proyecto1")

@app.route('/insertarArbol',methods=['POST']) 
def h():
    parametroPython = str(request.form['user'])
    parametroPython2 = str(request.form['password'])
    arbol.insertar(parametroPython,parametroPython2)
    print "**************"
    arbol.mostrarEnOrdenABB(arbol.raiz)
    print "**************"
    return "True"

@app.route('/verificarPassword',methods=['POST']) 
def v():
    parametroPython = str(request.form['user'])
    parametroPython2 = str(request.form['password'])
    if arbol.buscar(arbol.raiz,parametroPython)==True:
    	print "Usuario valido"
        return "True"
    else:
    	print "usuario invalido"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')