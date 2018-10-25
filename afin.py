# -*- coding: latin-1 -*-
import os, sys
import archivo
import alfabeto

TAM_ALFABETO = alfabeto.tamAlfabeto()
abc = alfabeto.getAlfabeto()

def cifrarAfin(texto, a, b, nombreArchivoSalida):
	mensajeCifrado = ""
	i = 0
	while (i < len(texto)):
		if texto[i] == '\xc3' or texto[i] == '\xc2':
			caracter = texto[i] + texto[i + 1]
			i+=1
			mi = alfabeto.getPosicion(caracter)
		else:
			mi = alfabeto.getPosicion(texto[i])
		modulo = (a*mi+b)%TAM_ALFABETO
		mensajeCifrado = mensajeCifrado + abc[modulo]
		i+=1
	f = archivo.escribirArchivo(nombreArchivoSalida, mensajeCifrado)
	if f=='':
		print 'Ocurrio un error al intentar escribir en', nombreArchivoSalida
	else:
		print 'Se guardo correctamente el mensaje cifrado en', nombreArchivoSalida
		f.close()
	sys.stdin.flush()
	#print mensajeCifrado

def descifrarAfin(texto, a, b, nombreArchivoSalida):
	d,x,y = extMcd(a, TAM_ALFABETO)
	mensajeClaro = ""
	i = 0
	while (i < len(texto)):
		if texto[i] == '\xc3' or texto[i] == '\xc2':
			caracter = texto[i] + texto[i + 1]
			i+=1
			ci = alfabeto.getPosicion(caracter)
		else:
			ci = alfabeto.getPosicion(texto[i])
		modulo = (x*(ci-b))%TAM_ALFABETO
		mensajeClaro = mensajeClaro + abc[modulo]
		i+=1
	f = archivo.escribirArchivo(nombreArchivoSalida, mensajeClaro)
	if f=='':
		print 'Ocurrio un error al intentar escribir en', nombreArchivoSalida
	else:
		print 'Se guardo correctamente el mensaje descifrado en',nombreArchivoSalida
		f.close()
	sys.stdin.flush()
	#print mensajeClaro
	
def verificarCoprimo(a):
	d,x,y = extMcd(a,TAM_ALFABETO)
	if d == 1:
		return True
	else:
		return False
	
def extMcd(a,b):
	if b == 0:
		return a,1,0
	x2 = 1
	x1 = 0
	y2 = 0
	y1 = 1
	while b != 0:
		q = a//b
		r = a - q*b
		x = x2 - q*x1
		y = y2 - q*y1
		a = b
		b = r
		x2 = x1
		x1 = x
		y2 = y1
		y1 = y
	if a < 0:
		return map(int, (-a, -x2, -y2))
	return map(int, (a, x2, y2))
	
def obtenerA(valor):
	a = 0
	try:
		a = int(valor)
	except ValueError:
		print "Ingresa un numero entre 1 y ",TAM_ALFABETO-1," para 'a'\n"
		return -1
	else:
		if (a >= 0 and a < TAM_ALFABETO):
			return a
		else:
			print 'Ingresa un numero entre 1 y ',TAM_ALFABETO-1," para 'a'\n"
			return -1

def obtenerB(valor):
	a = 0
	try:
		a = int(valor)
	except ValueError:
		print "Ingresa un numero entre 1 y ",TAM_ALFABETO-1," para 'b'\n"
		return -1
	else:
		if (a >= 0 and a < TAM_ALFABETO):
			return a
		else:
			print 'Ingresa un numero entre 1 y ', TAM_ALFABETO-1," para 'b'\n"
			return -1
