#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import ayuda
import validaciones

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
	if(arg[1]=="-sc"):
		validaciones.validacionCesar(arg)
	elif(arg[1]=="-sa"):
		validaciones.validacionAfin(arg)
	elif(arg[1]=="-sva"):
		validaciones.validacionVigenere(arg)
	else:
		print "EL ALGORIMO QUE DIGITO NO ES UNA OPCION VALIDA"

