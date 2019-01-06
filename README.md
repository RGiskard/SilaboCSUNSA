# Plantilla de Silabo CSUNSA

## Plantilla DUFA
Contenido:
```
dufa.tex
silabus.sty
```

![Color](https://github.com/RGiskard/SilaboCSUNSA/blob/master/imgReadme/dufa/informacionAcademica.png)

```latex
\setPeriodoAcademico{2018-B}
\setNombreAsignatura{Base de Datos I}
\setNombreProfesor{Edward  Hinojosa Cárdenas}
\setGradoProfesorAbreviado{Dr.}

\academicaTable
{Ciencia de la Computación} %Escuela Profesional
{1004244} %Código de la asignatura
{4} %Número del semestre
{Semestral} %Características
{17 Semanas} %Duración
{1} %Número de horas teóricas
{0} %Número de horas prácticas
{0} %Número de horas seminarios
{2}  %Número de horas laboratorio
{2} %Número de horas Teórico-práctico
{4} %Número de créditos
{Sistemas Operativos,Introducción a Ciencia de la Computación} % Prerrequisitos (separados por comas)

```

![Color](https://github.com/RGiskard/SilaboCSUNSA/blob/master/imgReadme/dufa/informacionAdministrativa.png)

```latex
\administrativaTable
{Doctor} %Grado académico del profesor
{Ingeniería de Sistemas e Informática} %Departamento académico
{6} %Número de horas totales
{2} %Número de horas - lunes
{-} %Número de horas - martes
{2} %Número de horas - miercoles
{2} %Número de horas - jueves
{-} %Número de horas - viernes
{101} %Aula de clase - lunes
{-} %Aula de clase - martes
{101} %Aula de clase - miercoles
{101} %Aula de clase - jueves
{-} %Aula de clase - viernes
```

![Color](https://github.com/RGiskard/SilaboCSUNSA/blob/master/imgReadme/dufa/fundamentacion.png)

```latex
\begin{fundamentacion}
El curso de Base de Datos I tiene como propósito desarrollar en el estudiante la capacidad de implementar una base de datos empleando adecuadamente los fundamentos de normalización, el modelo entidad-relación y el diseño lógico, basado en los requerimientos de información de una organización.
\end{fundamentacion}
```


![Color](https://github.com/RGiskard/SilaboCSUNSA/blob/master/imgReadme/dufa/sumilla.png)

```latex
\begin{sumilla}
\item uno
\item dos
\end{sumilla}
```


![Color](https://github.com/RGiskard/SilaboCSUNSA/blob/master/imgReadme/dufa/competenciasAsignaturas.png)

```latex
\begin{competenciasAsignatura}
\item this is item a
\item another item
\item assdsadsa
\end{competenciasAsignatura}
```


![Color](https://github.com/RGiskard/SilaboCSUNSA/blob/master/imgReadme/dufa/contenidos.png)

```latex
\begin{contenidos}
\nextUnidad{Identificación de requerimientos}
\nextCapitulo{Introducción a las Bases de Datos}
\nextTema{Clase Inaugural}
\nextTema{Introducción a las bases de datos}
\nextTema{Identificacion de BD}

\nextUnidad{Diseño de la base de datos}
\nextCapitulo{Modelamiento de Información}
\nextTema{Arquitectura}
\nextTema{Tipos}
\nextTema{Diseño Logico}

\nextUnidad{Construcción de bases de datos}
\nextCapitulo{Construcción de bases de datos}
\nextTema{Sentencias DDL}
\nextTema{Sentencias DML}
\nextTema{Normalización}

\end{contenidos}

```


![Color](https://github.com/RGiskard/SilaboCSUNSA/blob/master/imgReadme/dufa/estrategiasEnseñanza.png)

```latex
\begin{estrategia. ContenidossEnsenanza}
    \begin{metodos}
        Método expositivo en las clases teóricas \\
        Método de elaboración conjunta en los seminarios taller y en la elaboración del proyecto de investigación.
    \end{metodos}
    \begin{medios}
        Pizarra acrílica, plumones, cañón multimedia, material de laboratorio, videos, software.
    \end{medios}
    \begin{formasOrganizacion}
        %Se pone los que se necesiten
        \newItemFO{Clases Teóricas}{Desarrollo de los conceptos teóricos}
        \newItemFO{Seminarios}{Algo...}
        \newItemFO{Prácticas}{Algo...}
        \newItemFO{Laboratorio}{Aplicación de los conceptos vistos es clases teóricas.}
        \newItemFO{Otros}{Algo...}
    \end{formasOrganizacion}
    \begin{programacion}
        \newItemFO{Investigación Formativa}{Implementación de Sistema Computacional Web usando una base de datos relacional normalizada}
        \newItemFO{Responsabilidad Social}{Generar videos para la enseñanza de implementación de bases de datos y que sean disponibilizados de la población}
    \end{programacion}
    \begin{segumientoAprendizaje}
        Aquí va el seguimiento del aprendizaje
    \end{segumientoAprendizaje}
\end{estrategiasEnsenanza}
```


![Color](https://github.com/RGiskard/SilaboCSUNSA/blob/master/imgReadme/dufa/cronogramaAcademico.png)

```latex
\begin{cronogramaAcademico}
    \newItemCA{Tema1}{Edward Hinojosa Cárdenas}{10}  %Tema/Evaluación - Docente - Porcentaje acumulado
    \newItemCA{Tema2}{Edward Hinojosa Cárdenas}{16}
    \newItemCA{Tema3}{Edward Hinojosa Cárdenas}{20}
    \newItemCA{Tema4}{Edward Hinojosa Cárdenas}{25}
    \newItemCA{Tema5}{Edward Hinojosa Cárdenas}{33}
    \newItemCA{Tema6}{Edward Hinojosa Cárdenas}{37}
    \newItemCA{Tema7}{Edward Hinojosa Cárdenas}{40}
    \newItemCA{Tema8}{Edward Hinojosa Cárdenas}{45}
    \newItemCA{Tema9}{Edward Hinojosa Cárdenas}{50}
    \newItemCA{Tema10}{Edward Hinojosa Cárdenas}{53}
    \newItemCA{Tema11}{Edward Hinojosa Cárdenas}{58}
    \newItemCA{Tema12}{Edward Hinojosa Cárdenas}{64}
    \newItemCA{Tema13}{Edward Hinojosa Cárdenas}{69}
    \newItemCA{Tema14}{Edward Hinojosa Cárdenas}{76}
    \newItemCA{Tema15}{Edward Hinojosa Cárdenas}{84}
    \newItemCA{Tema16}{Edward Hinojosa Cárdenas}{93}
    \newItemCA{Tema17}{Edward Hinojosa Cárdenas}{100}
\end{cronogramaAcademico}

```

![Color](https://github.com/RGiskard/SilaboCSUNSA/blob/master/imgReadme/dufa/estrategiasEvaluacion.png)

```latex
\begin{estrategiasEvaluacion}
    \begin{evaluacionContinua}
        Práctica y Laboratorios en cada clase sobre los temas realizados, tanto para el primer parcial (EC1), segundo parcial (EC2) y tercer parcial (EC3).
    \end{evaluacionContinua}
    \begin{evaluacionPeriodica}
        \newItemEP{Primer Examen}{ponderación}
        \newItemEP{Segundo Examen}{ponderación}
        \newItemEP{Tercer Examen}{}
    \end{evaluacionPeriodica}
    \begin{cronogramaEvaluacion}
        \newItemCE{11/5/2019}{11/5/2019}{11/5/2019}{30\%}
        \newItemCE{11/8/2019}{11/8/2019}{11/8/2019}{30\%}
        \newItemCE{11/12/2019}{11/12/2019}{11/12/2019}{40\%}
    \end{cronogramaEvaluacion}
    \begin{tipoEvaluacion}
        Tipo de evaluación
    \end{tipoEvaluacion}
    \begin{instrumentosEvaluacion}
        Instrumentos de evaluación
    \end{instrumentosEvaluacion}
\end{estrategiasEvaluacion}

```

![Color](https://github.com/RGiskard/SilaboCSUNSA/blob/master/imgReadme/dufa/RequisitosAprobacion.png)

```latex
\begin{requisitosAprobacion}
\item El alumno tendrá derecho a observar o en su defecto a ratificar las notas consignadas en sus evaluaciones, después de ser entregadas las mismas por parte del profesor, salvo el vencimiento de plazos para culminación del semestre académico, luego del mismo, no se admitirán reclamaciones,
alumno que no se haga presente en el día establecido, perderá su derecho a reclamo.
\item Para aprobar ...
\end{requisitosAprobacion}

```

![Color](https://github.com/RGiskard/SilaboCSUNSA/blob/master/imgReadme/dufa/bibliografia.png)
```latex
\begin{bibliografia}
\item Korth, H. Saenz, F. Silberschatz. A. Sudarshan, S. Database System Concepts (6th ed.).
2013
\item Kroenke D. Auer D. Database Processing: Fundamentals, Design and Implementation
(14th ed.). 2015.
\end{bibliografia}

```
### FECHA Y FIRMA

![Color](https://github.com/RGiskard/SilaboCSUNSA/blob/master/imgReadme/dufa/fechaFirma.png)

```latex

\fecha

\firma

```


# Plantilla ICACIT
```
icacit.tex
icacit.sty
```

