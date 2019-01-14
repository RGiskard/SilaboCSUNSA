# coding=utf-8

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DF = "/"
_CONFIG_DIR_PATH = "conf"
_CRITERIOS_FILE_NAME = "criterios"
_NOTAS_X_CRITERIOS_FILE_NAME = "notasXcriterios"
_NIVELES_ESTUDIANTE_FILE_NAME = "niveles_estudiante"

CRITERIOS_LABEL = 'criterios'
Y_LABEL = "Alumnos"
CHART_TITLE = "Resumen"


CRITERIOS_FILE_PATH = _CONFIG_DIR_PATH + DF + _CRITERIOS_FILE_NAME
NOTAS_X_CRITERIOS_FILE_PATH = _CONFIG_DIR_PATH + DF + _NOTAS_X_CRITERIOS_FILE_NAME
NIVELES_ESTUDIANTE_FILE_PATH = _CONFIG_DIR_PATH + DF + _NIVELES_ESTUDIANTE_FILE_NAME


COLORS = ['#EE3224', '#F78F1E', '#FFC222']


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
    labels = []
    for line in nivelesFile:
        tokens = line.split(' ') #ID, minNota, maxNota
        tokens[-1] = tokens[-1].rstrip('\n')
        nivelesEstudiantes[tokens[0]] = [int(tokens[1]), int(tokens[2])]
        labels.append(tokens[0])
    nivelesFile.close()
    return nivelesEstudiantes, labels


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
nivelesEstudiante, labelsNiveles = getNiveles()
notasXcriterio = getNotasXcriterio()


resumenFinal = {}
for criterio, notasIds in notasXcriterio.iteritems():
    niveles_reporte = {}
    for key, value in nivelesEstudiante.iteritems():
        niveles_reporte[key] = [0,0]
    notasTemp = []

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

    resumenFinal[criterio] = niveles_reporte  #Nivel, [frecuencia, porcentaje]


raw_data_for_ploting = {}
raw_data_for_ploting[CRITERIOS_LABEL] = [criterio for criterio, notasIds in notasXcriterio.iteritems()]
raw_data_for_ploting[CRITERIOS_LABEL].sort()

for nivel in nivelesEstudiante:
    raw_data_for_ploting[nivel] = []
for criterio in raw_data_for_ploting[CRITERIOS_LABEL]:    
     for nivel, values in resumenFinal[criterio].iteritems():
         raw_data_for_ploting[nivel].append(values[0])
         
labelsNiveles.insert(0, CRITERIOS_LABEL)

df = pd.DataFrame(raw_data_for_ploting, columns = labelsNiveles)
pos = list(range(len(df[labelsNiveles[1]]))) 
width = 0.25

ig, ax = plt.subplots(figsize=(10,5))

for i in range(1,len(labelsNiveles)):
    label = labelsNiveles[i]
    plt.bar([p + width * (i - 1) for p in pos],
            df[label], 
            width, 
            alpha=0.5, 
            color=COLORS[i-1], 
            label=df[CRITERIOS_LABEL][i - 1]) 

ax.set_ylabel(Y_LABEL)

ax.set_title(CHART_TITLE)

ax.set_xticks([p + 1.5 * width for p in pos])

ax.set_xticklabels(df[CRITERIOS_LABEL])

plt.xlim(min(pos)-width, max(pos)+width*4)

height = []
for i in range (1,len(labelsNiveles)):
    label = labelsNiveles[i]
    if len(height) == 0:
        height = df[label]
    else:
        height += df[label]

plt.ylim([0, max(height)] )

plt.legend(labelsNiveles[1:], loc='upper left')
plt.grid()
plt.show()



            


        

        






