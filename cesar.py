#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import archivo
import alfabeto

TAM_ALFABETO = alfabeto.tamAlfabeto()
abc = alfabeto.getAlfabeto()
	
def cifrarCesar(texto, clave, nombreArchivoSalida):
	mensajeCifrado = ""
	i = 0
	#print texto
	while (i < len(texto)):
		if texto[i] == '\xc3' or texto[i] == '\xc2':
			caracter = texto[i] + texto[i + 1]
			i+=1
			mi = alfabeto.getPosicion(caracter)
		else:
			mi = alfabeto.getPosicion(texto[i])
		modulo = (mi+clave)%TAM_ALFABETO
		mensajeCifrado = mensajeCifrado + abc[modulo]
		i+=1			
	f = archivo.escribirArchivo(nombreArchivoSalida, mensajeCifrado)
	if f =='':
		print ('Ocurrio un error al intentar escribir en', nombreArchivoSalida)
	else:
		print ('El mensaje cifrado se guardo correctamente en',nombreArchivoSalida)
		f.close()
	sys.stdin.flush()
	#print mensajeCifrado

def descifrarCesar(criptograma, clave, nombreArchivoSalida):
	mensajeClaro = ""
	i = 0
	while (i < len(criptograma)):
		if criptograma[i] == '\xc3' or criptograma[i] == '\xc2':
			caracter = criptograma[i] + criptograma[i + 1]
			i+=1
			ci = alfabeto.getPosicion(caracter)
		else:
			ci = alfabeto.getPosicion(criptograma[i])
		modulo = (ci-clave)%TAM_ALFABETO
		mensajeClaro = mensajeClaro + abc[modulo]
		i+=1
	f = archivo.escribirArchivo(nombreArchivoSalida, mensajeClaro)
	if f=='':
		print ('Ocurrio un error al intentar escribir en', nombreArchivoSalida)
	else:
		print ('El mensaje descifrado se guardo correctamente en',nombreArchivoSalida)
		f.close()	
	sys.stdin.flush()
	#print mensajeClaro
	
def obtenerEntero(cla):
	clave = 0
	try:
		clave = int(cla)
	except ValueError:
		print ("Ingresa un numero entre 1 y \n",TAM_ALFABETO-1)
		return -1
	else:
		if (clave >= 0 and clave < TAM_ALFABETO):
			return clave
		else:
			print ('Ingresa un numero entre 1 y \n', TAM_ALFABETO-1)
			return -1
		

def cifrarDescifrar():
	accion = 0
	print ('\n1. Cifrar \n2. Descifrar \n3. Regresar')
	try:
		accion = int(input('\nIngresa una opcion: '))
	except NameError:
		print ("Debes ingresar un numero entre 1 y 3")
	else:
		if accion >= 1 and accion <=3:
			return accion
		else:
			print ('Debes ingresar un numero entre 1 y 3')
