#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import archivo
import alfabeto

def cifraVigenere(archEnt,clave,archSal): 
	doc=archEnt
	palabra=""
	k=""
	f = archivo.abrirArchivo(doc)
	h = archivo.abrirArchivo(clave)
	if f=='' or h=='':
		if(f==''):
			print 'No se encontro el archivo '+doc
		else: 
			print 'No se encontro el archivo '+clave
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
		#imprimirTexto(palabra)
		try:
			while(i<lg):	
				if(j<lk):
					if(palabra[i]=='\xc3' and k[i]=='\xc3'):
						##print i
						dato= alf[((alf.index(palabra[i]+palabra[i+1])+alf.index(k[j]+k[j+1]))%la)]
						i=i+1
						j=j+1
						c=c+dato
					elif(palabra[i]=='\xc3' or palabra[i]=='\xc2'): 
						dato= alf[((alf.index(palabra[i]+palabra[i+1])+alf.index(k[j]))%la)]
						i=i+1
						c=c+dato
					elif(k[j]=='\xc3' or k[j]=='\xc2'):
						dato= alf[((alf.index(palabra[i])+alf.index(k[j]+k[j+1]))%la)]
						j=j+1
						c=c+dato
					else:
						dato= alf[((alf.index(palabra[i])+alf.index(k[j]))%la)]
						c=c+dato
				else:
					if((palabra[i]=='\xc3' or palabra[i]=='\xc2') and (palabra[j-lk]=='\xc3' or palabra[j-lk]=='\xc2')):
						#print palabra[i],palabra[i+1],palabra[i]+palabra[i+1],palabra[j-lk]
						dato= alf[((alf.index(palabra[i]+palabra[i+1])+alf.index(palabra[j-lk]+palabra[j-lk+1]))%la)]
						i=i+1
						j=j+1
						c=c+dato
					elif(palabra[i]=='\xc3' or palabra[i]=='\xc2'):
						#print palabra[i],palabra[i+1],palabra[i]+palabra[i+1],palabra[j-lk]
						dato=alf[((alf.index(palabra[i]+palabra[i+1])+alf.index(palabra[j-lk]))%la)]
						i=i+1
						c=c+dato
					elif(palabra[j-lk]=='\xc3' or palabra[j-lk]=='\xc2'):
						#print palabra[j-lk],palabra[j-lk+1],palabra[j-lk]+palabra[j-lk+1]
						dato= alf[((alf.index(palabra[i])+alf.index(palabra[j-lk]+palabra[j-lk+1]))%la)]
						j=j+1
						c=c+dato
					else:
						dato=alf[((alf.index(palabra[i])+alf.index(palabra[j-lk]))%la)]
						c=c+dato
				i=i+1
				j=j+1
		except ValueError:
			print "El simbolo '",palabra[i],"'-'",palabra[i+1],"'=",palabra[i]+palabra[i+1],"no se encuentra en el alfabeto"
			print "Si desea agregar el simbolo consulte la ayuda"
			if(palabra[i]=="\xc3"):
				print palabra[i]
			sys.exit()
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
	k=""
	f = archivo.abrirArchivo(doc)
	h = archivo.abrirArchivo(clave)
	if f=='' or h=='':
		if(f==''):
			print 'No se encontro el archivo '+doc
		else: 
			print 'No se encontro el archivo '+clave
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
				if((palabra[i]=='\xc3' and palabra[i]=='\xc2') and (k[i]=='\xc2' or k[i]=='\xc3')):
					##print i
					dato= alf[((alf.index(palabra[i]+palabra[i+1])-alf.index(k[j]+k[j+1]))%la)]
					i=i+1
					j=j+1
					m=m+dato
				elif(palabra[i]=='\xc3' or palabra[i]=='\xc2'): 
					dato= alf[((alf.index(palabra[i]+palabra[i+1])+alf.index(k[j]))%la)]
					i=i+1
					m=m+dato
				elif(k[j]=='\xc3' or k[j]=='\xc2'):
					dato= alf[((alf.index(palabra[i])-alf.index(k[j]+k[j+1]))%la)]
					j=j+1
					m=m+dato
				else:
					dato= alf[((alf.index(palabra[i])-alf.index(k[j]))%la)]
					m=m+dato
				#dato=alf[((alf.index(palabra[i])-alf.index(k[i]))%la)]
				#m=m+dato
			else:
				if((palabra[i]=='\xc3' or palabra[i]=='\xc2') and (m[j-lk]=='\xc3' or m[j-lk]=='\xc2')):
					dato= alf[((alf.index(palabra[i]+palabra[i+1])-alf.index(m[j-lk]+m[j-lk+1]))%la)]
					i=i+1
					j=j+1
					m=m+dato
				elif(palabra[i]=='\xc3' or palabra[i]=='\xc2'):
					#print palabra[i],"+",palabra[i+1],"=",palabra[i]+palabra[i+1]
					dato=alf[((alf.index(palabra[i]+palabra[i+1])-alf.index(m[j-lk]))%la)]
					i=i+1
					m=m+dato
				elif(m[j-lk]=='\xc3' or m[j-lk]=='\xc2'):
					dato= alf[((alf.index(palabra[i])-alf.index(m[j-lk]+m[j-lk+1]))%la)]
					j=j+1
					m=m+dato
				else:
					dato=alf[((alf.index(palabra[i])-alf.index(m[j-lk]))%la)]
					m=m+dato
				#dato=alf[((alf.index(palabra[i])-alf.index(m[i-lk]))%la)]
				#m=m+dato
			i=i+1
			j=j+1
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

	


















