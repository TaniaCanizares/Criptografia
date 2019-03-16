#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys

def ayudaPrincipal():
	print (" --------------------------------------------------------------------------------------")
	print ("|                                                                                     |")
	print ("| \tALGORITMOS CRIPTOGRAFICOS                                                     |")
	print ("|										      |")
	print ("| sintaxis: python3 principal.py <algoritmo>					      |")
	print ("|										      |")
	print ("| <algoritmo>:									      |")
	print ("|\t-sc    Algoritmo de sustitución monoalfabética Julio Cesar		      |")
	print ("|\t-sa    Algoritmo de sustitución monoalfabética afin			      |")
	print ("|\t-sva   Algoritmo de sustitución polialfabética Vigenere Autoclave	      |")
	print ("|\t-mr   Algoritmo de transposicion Mascara Rotativa	                      |")
	print ("|\t-caf   Algoritmo de criptoanálisis por Frecuencia	                      |")
	print ("|										      |")
	print ("| consultar ayuda de un algoritmo en específico: 				      |")
	print ("|                                   sintaxis: python3 principal.py <algoritmo>	      |")
	print ("|										      |")
	print ("|										      |")
	print ("| Ayuda con el alfabeto:  			    				      |")
	print ("|\tsintaxis: python3 principal.py Alfabeto <tipoAyuda>	       		      |")
	print ("|										      |")
	print ("| <tipoAyuda>:									      |")
	print ("|\t-m    Mostrar alfabeto		     				              |")
	print ("|\t-a <simbolo>    agregar	simbolo al alfabeto    			              |")
	print ("|\t-t    Tamaño del alfabeto	      					      |")
	print ("|										      |")
	print ("|_____________________________________________________________________________________|")
	print ("| Elaborado por: Tania Cañizares (ctania@unicauca.edu.co)                             |")
	print ("| 		 Jonathan Ibarra (estivenp@unicauca.edu.co)                           |")
	print ("| Electiva:      Introducción a la Criptografía                         	      |")
	print ("| Docente:       Siler Amador Donado (samador@unicauca.edu.co)                        |")
	print ("|         									      |")
	print ("|                             UNIVERSIDAD DEL CAUCA                                   |")
	print ("|                   		  Febrero 2019                                        |")
	print (" --------------------------------------------------------------------------------------")

def ayudaVigenere():
	print (" ---------------------------------------------------------------------------------------------------")
	print ("|                                                                                                   |")
	print ("| \tALGORITMO VIGENERE AUTOCLAVE                     			                    |")
	print ("|	           								                    |")
	print ("| sintaxis: python3 principal.py -sva <modo> <archivoEntrada> <Archivoclave>                        |")
	print ("|								   		                    |")
	print ("| <modo>:									                    |")
	print ("|\t-c    para cifrar el archivo					                            |")
	print ("|\t-d    para decifrar el archivo    	  						    |")
	print ("| 										     		    |")
	print ("| <archivoEntrada>: Nombre del archivo de entrada a cifrar o descifrar ej: quijote.txt	 	    |")
	print ("|										                    |")
	print ("| <Archivoclave>: El archivo que contiene la clave para cifrar o descifrar el mensaje 		    |")
	print ("|										     		    |")
	print ("| NOTA: El archivo de salida tendra el mismo nombre que el archivo de entrada 	 		    |")
	print ("|	agregando al final la extencion '.cif'(cifrar) o '.dec'(descifrar)  			    |")
	print ("|	ej: quijote.txt.cif o quijote.txt.dec  					                    |")
	print ("|										     		    |")
	print ("| Codificación y decodificación (opcional):   	    	 				            |")
	print ("|\tsintaxis: python3 principal.py -sva <modo><archivoEntrada><Archivoclave> -c64 		    |")
	print ("|										                    |")
	print ("| Ejemplos:    			  						                    |")
	print ("|\tcifrar: python3 principal.py -sva -c quijote.txt Archivo_Clave.txt          		    |")
	print ("|\tdescifrar: python3 principal.py -sva -d quijote.txt.cif Archivo_Clave.txt	            |")
	print ("|\tcifrar codificando: python3 principal.py -sva -c quijote.txt Archivo_Clave.txt -c64         |")
	print ("|\tdescifrar decodificando: python3 principal.py -sva -d quijote.txt.cif Archivo_Clave.txt -c64|")
	print ("|										      		    |")
	print (" ---------------------------------------------------------------------------------------------------")

def ayudaCesar():
	print (" -------------------------------------------------------------------------------------")
	print ("|                                                                                     |")
	print ("| \tALGORITMO JULIO CÉSAR		                                              |")
	print ("|										      |")
	print ("| sintaxis: python3 principal.py -sc <modo> <archivoEntrada> <clave>                  |")
	print ("|										      |")
	print ("| <modo>:									      |")
	print ("|\t-c    para cifrar el archivo			             		      |")
	print ("|\t-d    para decifrar el archivo                  			      |")
	print ("| 										      |")
	print ("| <archivoEntrada>: Nombre del archivo de entrada a cifrar o descifrar ej: quijote.txt|")
	print ("|										      |")
	print ("| <clave>: es un número que corresponde al desplazamiento del alfabeto                |")
	print ("|										      |")
	print ("| Codificación y decodificación (opcional): 	 	                              |")
	print ("|\tsintaxis: python3 principal.py -sc <modo> <archivoEntrada> <clave> -c64       |")
	print ("|										      |")
	print ("| Ejemplos:    					 				      |")
	print ("|\tcifrar: python3 principal.py -sc -c quijote.txt 4                             |")
	print ("|\tdescifrar: python3 principal.py -sc -d quijote.txt.cif 4                      |")
	print ("|\tcifrar codificando: python3 principal.py -sc -c quijote.txt 4 -c64            |")
	print ("|\tdescifrar decodificando: python3 principal.py -sc -d quijote.txt.cif 4 -c64   |")
	print ("|         									      |")
	print (" -------------------------------------------------------------------------------------")

def ayudaAfin():
	print (" --------------------------------------------------------------------------------------")
	print ("|                                                                                      |")
	print ("| \tALGORITMO AFÍN		                                                       |")
	print ("|										       |")
	print ("| sintaxis: python3 principal.py -sa <modo> <archivoEntrada> <a> <b>                   |")
	print ("|										       |")
	print ("| <modo>:									       |")
	print ("|\t-c    para cifrar el archivo			             		       |")
	print ("|\t-d    para decifrar el archivo                  			       |")
	print ("| 										       |")
	print ("| <archivoEntrada>: Nombre del archivo de entrada a cifrar o descifrar ej: quijote.txt |")
	print ("|										       |")
	print ("| a y b deben estar en el siguiente rango 0<(a,b)<n-1  con n= Tamaño del alfabeto      |")
	print ("|										       |")
	print ("| <a>: es un número que sea co-primo con n (mcd(a,n)=1)      n=Tamaño del alfabeto     |")
	print ("|										       |")
	print ("| <b>: es un número que corresponde al desplazamiento del alfabeto(clave)              |")
	print ("|										       |")
	print ("| Codificación y decodificación (opcional): 	 	                               |")
	print ("|\tsintaxis: python3 principal.py -sa <modo> <archivoEntrada> <a> <b> -c64        |")
	print ("|										       |")
	print ("| Ejemplos:    					 				       |")
	print ("|\tcifrar: python3 principal.py -sa -c quijote.txt 17 5                           |")
	print ("|\tdescifrar: python3 principal.py -sa -d quijote.txt.cif 17 5                    |")
	print ("|\tcifrar codificando: python3 principal.py -sa -c quijote.txt 17 5 -c64          |")
	print ("|\tdescifrar decodificando: python3 principal.py -sa -d quijote.txt.cif 17 5 -c64 |")
	print ("|         									       |")
	print (" --------------------------------------------------------------------------------------")

def ayudaFrecuencia():
	print (" -----------------------------------------------------------------------------------------")
	print ("|                                                                                         |")
	print ("| \tCRIPTOANÁLISIS POR FRECUENCIA		                                          |")
	print ("|										          |")
	print ("| sintaxis: python3 principal.py -caf <archivoCifrado>                                    |")
	print ("|			  				 		 	          |")
	print ("| <archivoCifrado>: Nombre del archivo de entrada que desea descifrar ej: quijote.txt.cif |")
	print ("|										          |")
	print ("| Ejemplo:    					 				          |")
	print ("|\tdescifrar: python3 principal.py -caf quijote.txt.cif                              |")
	print ("|         									          |")
	print (" -----------------------------------------------------------------------------------------")

def ayudaMascara():
	print (" --------------------------------------------------------------------------------------------")
	print ("|                                                                             	             |")
	print ("| \tALGORITMO MÁSCARA ROTATIVA	                                                     |")
	print ("|										             |")
	print ("| sintaxis: python3 principal.py -mr <modo> <archivoEntrada> <Mascara>                       |")
	print ("|										             |")
	print ("| <modo>:									             |")
	print ("|\t-c    para cifrar el archivo			             		             |")
	print ("|\t-d    para decifrar el archivo                  			             |")
	print ("| 										             |")
	print ("| <archivoEntrada>: Nombre del archivo de entrada a cifrar o descifrar ej: quijote.txt       |")
	print ("|										             |")
	print ("| <Mascara>: Corresponde a la Clave. Revisar la documentacion 			             |")
	print ("|										             |")
	print ("| Codificación y decodificación (opcional): 	 	                                     |")
	print ("|\tsintaxis: python3 principal.py -mr <modo> <archivoEntrada> <Mascara> -c64            |")
	print ("|										             |")
	print ("| Ejemplos:    					 				             |")
	print ("|\tcifrar: python3 principal.py -mr -c quijote.txt mascara.txt                          |")
	print ("|\tdescifrar: python3 principal.py -mr -d quijote.txt.cif mascara.txt                   |")
	print ("|\tcifrar codificando: python3 principal.py -mr -c quijote.txt mascara.txt -c64         |")
	print ("|\tdescifrar decodificando: python3 principal.py -mr -d quijote.txt.cif mascara.txt -c64|")
	print ("|         									             |")
	print (" --------------------------------------------------------------------------------------------")
