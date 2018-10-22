def escribirArchivo(nombreArchivo, texto):
	try:
		archivo = open(nombreArchivo,"w")
	except IOError:
		return ''
	else:
		archivo.write(texto)
		return archivo
	
def abrirArchivo(nombreArchivo):
	try:
		archivo = open(nombreArchivo,'r')
	except IOError:
		return ''
	else:
		return archivo
		
def obtenerNombreArchivo():
	nombreArchivo = ''
	nombreArchivo = raw_input("(ejm: nombreArchivo.txt): ")
	return nombreArchivo
