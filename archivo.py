def escribirArchivo(nombreArchivo, texto):
	try:
		archivo = open(nombreArchivo,"w",encoding="ISO-8859-1")
	except IOError:
		return ''
	else:
		archivo.write(texto)
		return archivo

def escribirAlfabeto(nombreArchivo, texto):
	try:
		archivo = open(nombreArchivo,"a",encoding="ISO-8859-1")
	except IOError:
		return ''
	else:
		archivo.write(texto)
		return archivo
	
def abrirArchivo(nombreArchivo):
	try:
		archivo = open(nombreArchivo,'r',encoding="ISO-8859-1")
	except IOError:
		return ''
	else:
		return archivo
		
def obtenerNombreArchivo():
	nombreArchivo = ''
	nombreArchivo = raw_input("(ejm: nombreArchivo.txt): ")
	return nombreArchivo
