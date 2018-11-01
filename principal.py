#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import ayuda
import validaciones
import alfabeto

numArg=len(sys.argv)
arg=sys.argv


if(numArg==1):
	ayuda.ayudaPrincipal()
elif(numArg==2):
	if(arg[1]=="-sc"):
		ayuda.ayudaCesar()
	elif(arg[1]=="-sa"):
		ayuda.ayudaAfin()
	elif(arg[1]=="-sva"):
		ayuda.ayudaVigenere()
	else:
		print "EL ALGORIMO QUE DIGITO NO ES UNA OPCION VALIDA"
else:	
	if(arg[1]=="Alfabeto"):
		if(arg[2]=="-m"):
			alfabeto.imprimir()
		elif(arg[2]=="-a"):
			if(numArg==4):
				simbolo=arg[3]
				if(len(simbolo)==1 and alfabeto.existe(simbolo)==False):
					alfabeto.agregarSimbolo(simbolo)
				elif(len(simbolo)==2):
					if(simbolo[0]=='\xc3' or simbolo[0]=='\xc2'):
						if(alfabeto.existe(simbolo)==False):
							alfabeto.agregarSimbolo(simbolo)
					else:
						print 'Digite un solo simbolo '
				else:
					print 'Digite un solo simbolo'
			else:
				print 'Numero de argumentos incorrectos. Verifique la ayuda'
		elif(arg[2]=="-t"):
			print alfabeto.tamAlfabeto()
	elif(arg[1]=="-sc"):
		validaciones.validacionCesar(arg)
	elif(arg[1]=="-sa"):
		validaciones.validacionAfin(arg)
	elif(arg[1]=="-sva"):
		validaciones.validacionVigenere(arg)
	else:
		print "EL COMANDO QUE DIGITO NO ES UNA OPCION VALIDA"

