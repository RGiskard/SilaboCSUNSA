import sys

DF = "/"
_CONFIG_DIR_PATH = "conf"
_CRITERIOS_FILE_NAME = "criterios"
_NOTAS_X_CRITERIOS_FILE_NAME = "notasXcriterios"
_NIVELES_ESTUDIANTE_FILE_NAME = "niveles_estudiante"

CRITERIOS_FILE_PATH = _CONFIG_DIR_PATH + DF + _CRITERIOS_FILE_NAME
NOTAS_X_CRITERIOS_FILE_PATH = _CONFIG_DIR_PATH + DF + _NOTAS_X_CRITERIOS_FILE_NAME
NIVELES_ESTUDIANTE_FILE_PATH = _CONFIG_DIR_PATH + DF + _NIVELES_ESTUDIANTE_FILE_NAME


def getNotas(notasFilePath):
    notasFile = open(notasFilePath, 'r')
    fields = []
    for line in notasFile:
        field = line.split(',') #ID, DNI, APELLIDO, NOMBRE, NOTA1, 2, 3, 4, 5 ,6
        field[-1] = field[-1].rstrip('\n')
        fields.append(field)
    fields.pop(0)
    notasFile.close()
    return fields



if len(sys.argv) < 2:
    print "Faltan argumentos <notas.csv>"
    sys.exit()


notasFilePath = sys.argv[1]
notas = getNotas(notasFilePath)
print notas



