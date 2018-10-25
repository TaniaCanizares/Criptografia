#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import archivo
import alfabeto

def cifraVigenere(archEnt,clave,archSal): 
	doc=archEnt
	palabra=""
	f = archivo.abrirArchivo(doc)
	if f=='':
		print 'No se encontro el archivo '+doc
	else:
		for pal in f.readlines():
			palabra=palabra+pal
		f.close()
		k=clave
		lk=len(k)
		i=0
		c=""
		lg=len(palabra)
		alf=alfabeto.getAlfabeto()
		la=alfabeto.tamAlfabeto()
		#imprimirTexto(palabra)
		#auxiliar=acomodarTexto(palabra)
		#imprimirTexto(auxiliar)
		while(i<lg):	
			if(i<lk):
				if(palabra[i]!='\xc3'):
					##print i
					dato= alf[((alf.index(palabra[i])+alf.index(k[i]))%la)]
					c=c+dato
				else: 
					dato= alf[((alf.index(palabra[i]+palabra[i+1])+alf.index(k[i]))%la)]
					i=i+1
					c=c+dato
			else:
				if(palabra[i]!='\xc3'):
					dato=alf[((alf.index(palabra[i])+alf.index(palabra[i-lk]))%la)]
					c=c+dato
				else:
					##print palabra[i]+palabra[i+1]
					dato=alf[((alf.index(palabra[i]+palabra[i+1])+alf.index(palabra[i-lk]))%la)]
					i=i+1
					c=c+dato
			i=i+1
		n = archSal
		fichero = archivo.escribirArchivo(n, c)
		if fichero=='':
			print 'Ocurrio un error al intentar escribir en ', n
		else:
			fichero.close()
			print "\n*********************************************************************"
			print "  SE GENERO EL ARCHIVO ", n," CON EL MENSAJE CIFRADO"
			print "*********************************************************************\n\n"

#-------------------------------------------------
def descVigenere(archEnt,clave,archSal):
	doc=archEnt
	palabra=""
	f = archivo.abrirArchivo(doc)
	if f == '':
		print 'No se encontro el archivo '+doc
	else:
		for pal in f.readlines():
			palabra=palabra+pal
		f.close()
		lg=len(palabra)
		k=clave
		lk=len(k)
		i=0
		m=""
		alf=alfabeto.getAlfabeto()
		la=alfabeto.tamAlfabeto()
		while(i<lg):
			if(i<lk):
				dato=alf[((alf.index(palabra[i])-alf.index(k[i]))%la)]
				m=m+dato
			else:
				dato=alf[((alf.index(palabra[i])-alf.index(m[i-lk]))%la)]
				m=m+dato
			i=i+1
		n = archSal
		fichero = archivo.escribirArchivo(n,m)
		if fichero=='':
			print 'Ocurrio un error al intentar escribir en ', n
		else:
			fichero.close()
			print "\n*********************************************************************"
			print "SE GENERO EL ARCHIVO ",n," CON EL MENSAJE EN CLARO"
			print "*********************************************************************\n\n\n"

def imprimirTexto(texto):
	i=0	
	print "-------------------------------------------"
	while(i<200):
		print texto[i]
		i=i+1

def acomodarTexto(texto):
	i=0
	while(i<200):
		if(texto[i]=='\xc3'):
			#texto[i]=str(texto[i+1])
			print texto[i]+texto[i+1]
			texto[i]='h'
		i=i+1
	return texto
	


















