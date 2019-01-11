import tabula
import pandas as pd
from subprocess import check_output
# Read pdf into DataFrame
df = tabula.read_pdf("notas.pdf")
df = df.drop('Resolucion', 1)
name="notas_2018_450_1701209_BA002475"#formato del nombre de los cursos
campos=name.split("_")#campos
notas=campos[4]#parsear para obtener notas
semestre=notas[0]#semestre
grupo=notas[1]#grupo a b 
value=val=int(notas[2:])#string a entero para ordenar por notas
# Read remote pdf into DataFrame
#df2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")

# convert PDF into CSV

#tabula.convert_into("notas.pdf", "output.csv", output_format="csv")
#cereal_df = pd.read_csv("output.csv")
#print(df.head(5))


check_output("dir /b /a-d>files.txt", shell=True)