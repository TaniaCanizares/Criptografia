#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys
import archivo
import alfabeto

def cifraVigenere(archEnt,clave,archSal, codificacion): 
	doc=archEnt
	palabra=""
	k=""
	f = archivo.abrirArchivo(doc)
	h = archivo.abrirArchivo(clave)
	if f=='' or h=='':
		if(f==''):
			print ('No se encontro el archivo '+doc)
		else: 
			print ('No se encontro el archivo '+clave)
	else:
		for pal in f.readlines():
			palabra=palabra+pal
		f.close()
		for cla in h.readlines():
			k=k+cla
		h.close()
		lk=len(k)
		i=0
		j=0
		c=""
		lg=len(palabra)
		alf=alfabeto.getAlfabeto()
		la=alfabeto.tamAlfabeto()
		flag = 1
		#imprimirTexto(palabra)
		#try:
		while(i<lg):	
			if(j<lk):
				try:
					dato= alf[((alf.index(palabra[i])+alf.index(k[j]))%la)]
				except:
					flag = -1
				if(flag==-1):
					print("El caracter ",palabra[i]," no se encuentra en el alfabeto, revise la ayuda en el menú principal para añadirlo") 
					break
				else:
					c=c+dato
			else:

				#print "",palabra[i]
				dato=alf[((alf.index(palabra[i])+alf.index(palabra[j-lk]))%la)]
				c=c+dato
			i=i+1
			j=j+1
		if(flag!=-1):
			n = archSal
			fichero = archivo.escribirArchivo(n, c)
			if fichero=='':
				print ('Ocurrio un error al intentar escribir en ', n)
			else:
				fichero.close()
				print ("\n*********************************************************************")
				print ("  SE GENERO EL ARCHIVO ", n," CON EL MENSAJE CIFRADO")
				print ("*********************************************************************\n\n")
		else:
			print ("La ejecución se detuvo")

#-------------------------------------------------
def descVigenere(archEnt,clave,archSal, codificacion):
	doc=archEnt
	palabra=""
	k=""
	f = archivo.abrirArchivo(doc)
	h = archivo.abrirArchivo(clave)
	if f=='' or h=='':
		if(f==''):
			print ('No se encontro el archivo '+doc)
		else: 
			print ('No se encontro el archivo '+clave)
	else:
		for pal in f.readlines():
			palabra=palabra+pal
		f.close()
		lg=len(palabra)
		for cla in h.readlines():
			k=k+cla
		h.close()
		lk=len(k)
		i=0
		j=0
		m=""
		alf=alfabeto.getAlfabeto()
		la=alfabeto.tamAlfabeto()
		while(i<lg):
			if(j<lk):
				dato= alf[((alf.index(palabra[i])-alf.index(k[j]))%la)]
				m=m+dato
			else:
				dato=alf[((alf.index(palabra[i])-alf.index(m[j-lk]))%la)]
				m=m+dato
			i=i+1
			j=j+1
		n = archSal
		fichero = archivo.escribirArchivo(n,m)
		if fichero=='':
			print ('Ocurrio un error al intentar escribir en ', n)
		else:
			fichero.close()
			print ("\n*********************************************************************")
			print ("SE GENERO EL ARCHIVO ",n," CON EL MENSAJE EN CLARO")
			print ("*********************************************************************\n\n\n")

def imprimirTexto(texto):
	i=0	
	print ("-------------------------------------------")
	while(i<200):
		print (texto[i])
		i=i+1

	


















