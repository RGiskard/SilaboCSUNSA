import tabula
import pandas as pd
from subprocess import check_output

'''
name="notas_2018_450_1701209_BA002475"#formato del nombre de los cursos
campos=name.split("_")#campos
notas=campos[4]#parsear para obtener notas
semestre=notas[0]#semestre
grupo=notas[1]#grupo a b 
value=val=int(notas[2:])#string a entero para ordenar por notas
# Read remote pdf into DataFrame
#df2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")
'''
# convert PDF into CSV

#tabula.convert_into("notas.pdf", "output.csv", output_format="csv")
#cereal_df = pd.read_csv("output.csv")
#print(df.head(5))

###concatenar
#df_new = pd.concat([df_a, df_b])

#cabeceras
cabecera=["Nro","Codigo","Alumno","Nota","En Letras","Resolucion"]
# Read pdf into DataFrame
def getFrame(fileNameInput):
	df = tabula.read_pdf(fileNameInput)
	df = df.drop(cabecera[len(cabecera)-1], 1)
	df = df.drop(cabecera[len(cabecera)-2], 1)
	df = df.drop(cabecera[0], 1)
	return df

##problemas con series y dataframe df=df.loc[:,campo]
def getMinimunFrame(fileNameInput,campo):
	df = tabula.read_pdf(fileNameInput)
	index=cabecera.index(campo)
	for i in range(index):
		df = df.drop(cabecera[i], 1)
	for i in range(index+1,len(cabecera)):
		df = df.drop(cabecera[i], 1)
	return df	

def parseName(fileNameInput):
	campos=fileNameInput.split("_")#campos
	return campos


##obtener lista de nombres
fileName="files.txt"
comand="dir /b /a-d>"+fileName
check_output(comand, shell=True)
names = [line.rstrip('\n') for line in open('files.txt')]
##eliminar archivos no utilizados
del names[0]
del names[0]

####Para testear solamente
clave="Nota"
dfInit=getFrame(names[0])
dfNota1=getMinimunFrame(names[1],clave)