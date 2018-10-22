#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import archivo
import alfabeto

TAM_ALFABETO = alfabeto.tamAlfabeto()
abc = alfabeto.getAlfabeto()
	
def cifrarCesar(texto, clave, nombreArchivoSalida):
	mensajeCifrado = ""
	for caracter in texto: 
		mi = alfabeto.getPosicion(caracter)
		if (mi!=-1):
			modulo = (mi+clave)%TAM_ALFABETO
			mensajeCifrado = mensajeCifrado + abc[modulo]
		else:
			continue
	f = archivo.escribirArchivo(nombreArchivoSalida, mensajeCifrado)
	if f =='':
		print 'Ocurrio un error al intentar escribir en', nombreArchivoSalida
	else:
		print 'El mensaje cifrado se guardo correctamente en',nombreArchivoSalida
		f.close()
	sys.stdin.flush()
	#print mensajeCifrado

def descifrarCesar(criptograma, clave, nombreArchivoSalida):
	mensajeClaro = ""
	for caracter in criptograma:
		ci = alfabeto.getPosicion(caracter)
		if (ci!=-1):
			modulo = (ci-clave)%TAM_ALFABETO
			mensajeClaro = mensajeClaro + abc[modulo]
		else:
			continue
	f = archivo.escribirArchivo(nombreArchivoSalida, mensajeClaro)
	if f=='':
		print 'Ocurrio un error al intentar escribir en', nombreArchivoSalida
	else:
		print 'El mensaje descifrado se guardo correctamente en',nombreArchivoSalida
		f.close()	
	sys.stdin.flush()
	#print mensajeClaro
	
def obtenerEntero(cla):
	clave = 0
	try:
		clave = int(cla)
	except ValueError:
		print "Ingresa un numero entre 1 y \n",TAM_ALFABETO-1
		return -1
	else:
		if (clave >= 0 and clave < TAM_ALFABETO):
			return clave
		else:
			print 'Ingresa un numero entre 1 y \n', TAM_ALFABETO-1
			return -1
		

def cifrarDescifrar():
	accion = 0
	print '\n1. Cifrar \n2. Descifrar \n3. Regresar'
	try:
		accion = int(input('\nIngresa una opcion: '))
	except NameError:
		print "Debes ingresar un numero entre 1 y 3"
	else:
		if accion >= 1 and accion <=3:
			return accion
		else:
			print 'Debes ingresar un numero entre 1 y 3'
