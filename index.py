from flask import Flask,request,render_template
from flask_cors import CORS
import json

from Calculo import calculadora
Ca=calculadora()

app = Flask(__name__) #le digo que este es mi main (guarda el objeto en app)

# Aca realizamos configuracion de cors
CORS(app) #si no se le pone esto no jala para poder hacer la conexion con mi fronted


@app.route('/') #(1)diseño_loggin
def index():
    return 'nothing'



#suma
@app.route('/suma', methods=['POST'])
def usuarios():
    datos=request.json
    return Ca.Sumaa(datos['a'],datos['b'])


#Resta
@app.route('/resta', methods=['POST'])
def resta():
    datos=request.json
    return Ca.Resta(datos['a'],datos['b'])


#division
@app.route('/division', methods=['POST'])
def divi():
    datos=request.json
    return Ca.Divii(datos['a'],datos['b'])


#Multiplicacion
@app.route('/multiplicacion', methods=['POST'])
def multi():
    datos=request.json
    return Ca.Multii(datos['a'],datos['b']) 

#potencia
@app.route('/potencia', methods=['POST'])
def potenciaa():
    datos=request.json
    return Ca.Pote(datos['a'],datos['b'])  

#r
@app.route('/raiz', methods=['POST'])
def raiz():
    datos=request.json
    return Ca.raizz(datos['a'],datos['b']) 


#muestra datos
@app.route('/verm') #obtiene los datos de mi vector
def mostrar():
    return Ca.obtenerUser()      


   




   
if __name__=='__main__':  #se ejecutara desde cualquier momento en un servidor
    app.run(debug=True, port="5000")