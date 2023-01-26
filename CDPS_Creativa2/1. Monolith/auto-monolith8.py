#!/usr/bin/python


#PRACTICA CREATIVA 2


#CDPS


#Álvaro torroba de Linos


#Andres Emilio Flores Reina


#Luis Travé Reneses




import sys
from subprocess import call 
import os

# Descargamos el repositorio 

call (["git", "clone", "https://github.com/luis-trave/creativa_2"])

#instalamos pip
call(["sudo", "apt-get", "install", "python3-pip"])


# Instalamos dependencias 

call (["pip", "install", "-r" , "practica_creativa2/bookinfo/src/productpage/requirements.txt"])



#Creamos la variable del entorno

os.environ ['GROUP NUMBER']="37" 
num_grupo= str(os.environ.get ('GROUP NUMBER'))



#Cambiamos titulo 
call (["cp", "practicacreativa2/bookinfo/src/productpage/templates/productpageCopy.html",
"practica_ creativa2/bookinfo/src/productpage/templates/productpageCopy.html"])
fCopia = open ("practica_ creativa2/bookinfo/src/productpage/templates/productpageCopy.html", 'r')
fOriginal = open ("practica_ creativa2/bookinfo/src/productpage/templates/productpageCopy.html", 'w')
for line in fCopia:
        if "{% block title %} Simple Bookstore App{& endblock %}" in line:
             fOriginal.write("{% block title %} Simple Bookstore App - GRUPO " + num_grupo + "{% endblock %}") 
        else: fOriginal.write(line)
fOriginal.close()
fCopia.close()
call(["rm", "practica creativa2/bookinfo/src/productpage/templates/productpageCopy.html"])



# Arrancamos aplicacion

call (["python3", "practica creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"])
