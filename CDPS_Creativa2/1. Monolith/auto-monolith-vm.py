#!/usr/bin/python


#PRACTICA CREATIVA 2


#CDPS 2021


#Alfredo Garrachón Ruiz


#Alejandro Mariñas Cuesta


#Sergio Jiménez Berrón



import os, sys, subprocess, json

from subprocess import call



#MAIN FUNCTIONS


def start ():

	#Instalar pip
		
	call(["apt-get", "update"])

	call(["apt-get", "install", "-y", "python3-pip"])

	
	#Instalar las dependencias	
	
	call(["pip3", "install", "-r", "/home/productpage/requirements.txt"])

	
	#Lanzar el servicio en el puerto 9080
	call(["python3", "/home/productpage/productpage_monolith.py", "9080"])


#CONSOLE INPUTS


arguments = sys.argv


if len(arguments) >= 2 :

	if arguments[1] == "start":
		start()

else:
	print("Not enough arguments")




