#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import archivo
import alfabeto

TAM_ALFABETO = alfabeto.tamAlfabeto()
abc = alfabeto.getAlfabeto()

def contar(letra, texto):
	contador = 0
    for caracter in texto:
        if caracter == letra:
            contador = contador + 1
    return contador



def guardarFrecuencias(texto):
	i = 0
	listaFrecuencias = []
	while (i< len(abc)):
		n = contar(abc[i],texto)
		if (n == 0):
			i+=1
		listaFrecuencias.append(contar(abc[i],texto))
	
	for elemento in listaFrecuencias:
		print elemento
		
guardarFrecuencias('LAVIDAESUNSUEÑOYLOSSUEÑOSSUEÑOSSON')
		

