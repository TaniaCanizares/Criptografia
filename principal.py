#!/usr/bin/python
# -*- coding: utf8 -*-
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
	elif(arg[1]=="-mr"):
		ayuda.ayudaMascara()
	elif(arg[1]=="-caf"):
		ayuda.ayudaFrecuencia()
	else:
		print ("EL ALGORIMO QUE DIGITÓ NO ES UNA OPCION VÁLIDA")
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
						print ('Digite un solo símbolo ')
			else:
				print ('Número de argumentos incorrectos. Verifique la ayuda')
		elif(arg[2]=="-t"):
			print (alfabeto.tamAlfabeto())
	elif(arg[1]=="-sc"):
		validaciones.validacionCesar(arg)
	elif(arg[1]=="-sa"):
		validaciones.validacionAfin(arg)
	elif(arg[1]=="-sva"):
		validaciones.validacionVigenere(arg)
	elif(arg[1]=="-mr"):
		validaciones.validacionMascara(arg)
	elif(arg[1]=="-caf"):
		validaciones.validacionFrecuencia(arg)
	else:
		print ("EL COMANDO QUE DIGITÓ NO ES UNA OPCION VÁLIDA")

