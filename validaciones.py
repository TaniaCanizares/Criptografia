#!/usr/bin/python
# -*- coding: latin-1 -*-
import ayuda
import vigenere
import archivo
import cesar
import afin
import frecuencia
import MascaraRotativa
from time import time


def validacionVigenere(argumentos):
	if(len(argumentos)!=5):
		print "\nEl numero de parametros es incorrecto"
		print "Revisar la ayuda del algoritmo de vigenere: python principal.py -sva\n"
	else:
		if(argumentos[2]=="-c"):
			start_time = time()
			vigenere.cifraVigenere(argumentos[3],argumentos[4],argumentos[3]+".cif")
			elapsed_time = time() - start_time
			print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
		elif(argumentos[2]=="-d"):
			sal=argumentos[3].replace("cif","dec")
			start_time = time()
			vigenere.descVigenere(argumentos[3],argumentos[4],sal)
			elapsed_time = time() - start_time
			print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
		else: 
			print "\nEl modo ",argumentos[2]," es incorrecto"
			print "Revisar la ayuda del algoritmo de vigenere: python principal.py -sva\n"

def validacionCesar(argumentos):
	texto = ""
	if(len(argumentos)!=5):
		print "\nEl numero de parametros es incorrecto"
		print "Revisar la ayuda del algoritmo de cesar: python principal.py -sc\n"
	else:
		if(argumentos[2]=="-c"):
			f = archivo.abrirArchivo(argumentos[3])
			if f=='':
				print 'No se encontro el archivo '+argumentos[3]
			else:
				for pal in f.readlines():
					texto=texto+pal
				f.close()
				clave = cesar.obtenerEntero(argumentos[4])
				if(clave != -1):
					start_time = time()
					cesar.cifrarCesar(texto, clave, argumentos[3]+".cif")
					elapsed_time = time() - start_time
					print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
		elif(argumentos[2]=="-d"):
			f = archivo.abrirArchivo(argumentos[3])
			if f=='':
				print 'No se encontro el archivo '+argumentos[3]
			else:
				for pal in f.readlines():
					texto=texto+pal
				f.close()
				clave = cesar.obtenerEntero(argumentos[4])
				nomArchivoDec = argumentos[3].replace('.cif', '.dec')
				if(clave != -1):
					start_time = time()
					cesar.descifrarCesar(texto, clave, nomArchivoDec)
					elapsed_time = time() - start_time
					print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
		else: 
			print "\nEl modo ",argumentos[2]," es incorrecto"
			print "Revisar la ayuda del algoritmo de cesar: python principal.py -sc\n"

def validacionAfin(argumentos):
	texto = ""
	if(len(argumentos)!=6):
		print "\nEl numero de parametros es incorrecto"
		print "Revisar la ayuda del algoritmo de afin: python principal.py -sa\n"
	else:
		if(argumentos[2]=="-c"):
			f = archivo.abrirArchivo(argumentos[3])
			if f=='':
				print 'No se encontro el archivo '+argumentos[3]
			else:
				for pal in f.readlines():
					texto=texto+pal
				f.close()
				a = afin.obtenerA(argumentos[4])
				if (a != -1):
					if (afin.verificarCoprimo(a) != True):	
						print 'El nuemero a es invalido'
						print 'El numero debe ser primo con el tamano del alfabeto' 
					else:
						b = afin.obtenerB(argumentos[5])
						if(b != -1):
							start_time = time()
							afin.cifrarAfin(texto, a, b, argumentos[3]+".cif")
							elapsed_time = time() - start_time
							print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
		elif(argumentos[2]=="-d"):
			f = archivo.abrirArchivo(argumentos[3])
			if f=='':
				print 'No se encontro el archivo '+argumentos[3]
			else:
				for pal in f.readlines():
					texto=texto+pal
				f.close()
				a = afin.obtenerA(argumentos[4])
				if (a != -1):
					if (afin.verificarCoprimo(a) != True):	
						print 'El nuemero a es invalido'
						print 'El numero debe ser primo con el tamano del alfabeto' 					
					else:					
						b = afin.obtenerB(argumentos[5])
						nomArchivoDec = argumentos[3].replace('.cif', '.dec')
						if(b != -1):
							start_time = time()
							afin.descifrarAfin(texto, a, b, nomArchivoDec)
							elapsed_time = time() - start_time
							print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
		else: 
			print "\nEl modo ",argumentos[2]," es incorrecto"
			print "Revisar la ayuda del algoritmo de afin: python principal.py -sa\n"

def validacionFrecuencia(argumentos):
	if(len(argumentos)!=3):
		print "\nEl numero de parametros es incorrecto"
		print "Revisar la ayuda del algoritmo de criptoanalisis por frecuencia: python principal.py -caf\n"
	else:
		f = archivo.abrirArchivo(argumentos[2])
		if f=='':
			print 'No se encontro el archivo '+argumentos[2]
		else:
			texto = ""
			nomArchivoDec = argumentos[2].replace('.cif', '.dec')
			for pal in f.readlines():
				texto=texto+pal
			f.close()
			start_time = time()
			frecuencia.analisisFrecuencia(texto, nomArchivoDec)
			elapsed_time = time() - start_time
			print("Tiempo transcurrido: %.10f segundos." % elapsed_time)

def validacionMascara(argumentos):
	if(len(argumentos)!=5):
		print "\nEl numero de parametros es incorrecto"
		print "Revisar la ayuda del algoritmo de Mascara Rotativa: python principal.py -mr\n"
	else:
		if(argumentos[2]=="-c"):
			start_time = time()
			MascaraRotativa.cifradoMR(argumentos[3],argumentos[4])
			elapsed_time = time() - start_time
			print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
		elif(argumentos[2]=="-d"):
			start_time = time()
			MascaraRotativa.descifradoMR(argumentos[3],argumentos[4])
			elapsed_time = time() - start_time
			print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
		else: 
			print "\nEl modo ",argumentos[2]," es incorrecto"
			print "Revisar la ayuda del algoritmo de Mascara Rotativa: python principal.py -mr\n"
