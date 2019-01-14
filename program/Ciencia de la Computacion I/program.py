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
        field = field[4:]
        fields.append(field)
    fields.pop(0)
    for i in range(0,len(fields)):
        fields[i] = [int(j) for j in fields[i]]
    notasFile.close()
    return fields

def getCriterios():
    criteriosFile = open(CRITERIOS_FILE_PATH, 'r')
    criterios = {}
    for line in criteriosFile:
        tokens = line.split(' ') #ID, Nombre o descripcion
        tokens[-1] = tokens[-1].rstrip('\n')
        criterios[tokens[0]] = tokens[1]
    criteriosFile.close()
    return criterios

def getNiveles():
    nivelesFile = open(NIVELES_ESTUDIANTE_FILE_PATH, 'r')
    nivelesEstudiantes = {}
    for line in nivelesFile:
        tokens = line.split(' ') #ID, minNota, maxNota
        tokens[-1] = tokens[-1].rstrip('\n')
        nivelesEstudiantes[tokens[0]] = [int(tokens[1]), int(tokens[2])]
    nivelesFile.close()
    return nivelesEstudiantes    


def getNotasXcriterio():
    notasXcriterioFile = open(NOTAS_X_CRITERIOS_FILE_PATH, 'r')
    _notasXcriterio = {}
    notasXcriterio = {}
    for line in notasXcriterioFile:
        tokens = line.split(' ') #ID, criterios
        tokens[-1] = tokens[-1].rstrip('\n')
        criterios = tokens[1].split(',')
        _notasXcriterio[tokens[0]] = criterios
    for key, value in _notasXcriterio.iteritems():
        key = int(key)
        for v in value:
            if not v in notasXcriterio:
                notasXcriterio[v] = []
            notasXcriterio[v].append(key) 
    notasXcriterioFile.close()
    return notasXcriterio

def verifyNota(nivelesEstudiante, nota):
    for key, rangos in nivelesEstudiante.iteritems():
        if(nota <= rangos[1]):
            return key

if len(sys.argv) < 2:
    print "Faltan argumentos <notas.csv>"
    sys.exit()


notasFilePath = sys.argv[1]
notas = getNotas(notasFilePath)
criterios = getCriterios()
nivelesEstudiante = getNiveles()
notasXcriterio = getNotasXcriterio()


resumenFinal = {}
for criterio, notasIds in notasXcriterio.iteritems():
    niveles_reporte = {}
    for key, value in nivelesEstudiante.iteritems():
        niveles_reporte[key] = [0,0]
    notasTemp = []

     #nota[nId] for nota in notas for nId in notasIds

    for i in range(0, len(notasIds)):
        nId = notasIds[i]
        for j in range(0, len(notas)):
            nota = notas[j]
            if i == 0:
                notasTemp.append(0)
            notasTemp[j] += nota[nId]
    
    notasTemp = [float(i) / float(len(notasIds)) for i in notasTemp]
    for nota in notasTemp:
        niveles_reporte[verifyNota(nivelesEstudiante, nota)][0] += 1
    for key, value in niveles_reporte.iteritems():
        niveles_reporte[key][1] = value[0] * float(100) / float(len(notas))

    print niveles_reporte #Nivel, [frecuencia, porcentaje]
        
        
            


        

        






