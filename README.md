# Actividad Integradora 2

## Propósito del Proyecto
El producto elaborado en esta actividad tiene la finalidad de recopilar imágenes de la base de datos en línea ShutterStock, bajo un término de búsqueda especificado por quien ejecute el programa. La ventaja de la base de datos ShutterStock es que esta tiene una gran cantidad de imágenes que están etiquetadas según sus contenidos.

Este programa será de utilidad para el análisis de imágenes utilizando algún método de Machine Learning ya que, a través de este programa, se busca obtener rápida y fácilmente un gran set de imágenes para entrenar y probar modelos.

## Requisitos para Ejecutar el Programa

### Python
Para ejecutar este programa, es necesario contar con el lenguaje Python instalado en el sistema.

### Selenium
Lo siguiente es tener en el ambiente de desarrollo la herramiente Selenium. Esta se puede instalar a través de los manejadores de paquetes Anaconda o Pip.

Así mismo, es necesario tener instalado el driver de Selenium para el navegador de Chrome, ya que a través de este se hace el scraping.

## Funcionamiento del Programa
Al ejecutar el código, el programa pedirá al usuario la palabra que será el criterio de búsqueda. Después de escribirla y dar Enter, el programa hará la búsqueda de imágenes y estas se descargarán en dos nuevas carpetas creadas en el folder donde se ejecutó el programa. Estas carpetas serán **./train/[palabra]** y **./test/[palabra]**, donde **[palabra]** es el término de búsqueda. Cabe mencionar que el 80% de las imágenes recopiladas serán guardadas en la carpeta train y el resto en la carpeta test. 