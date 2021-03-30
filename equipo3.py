from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math
import os
import urllib.request
from enum import Enum

#Función para descargar imagenes en su carpeta correspondiente
def downloadSamples(listOfImages, sampleType):
    if not os.path.exists('{}/{}'.format(sampleType,searchWord)):
        os.makedirs('{}/{}'.format(sampleType,searchWord))
    
    for srcImageIndex in range(len(listOfImages)):
        print("Descargas: {} / {}".format(srcImageIndex+1,len(listOfImages)))
        image_url = listOfImages[srcImageIndex] #src de imagén
        save_name = '{}/{}/{}{}.jpg'.format(sampleType,searchWord,searchWord,srcImageIndex) #Nombre local al guardar
        urllib.request.urlretrieve(image_url, save_name)

driver = webdriver.Chrome() #Chrome Driver / En algunas implementaciones con Windows es necesario agregar un path entre los parentesis

#####################################################################
searchWord= "cat" #Imagenes a buscar

lastPageToSearch = 3 #Última página a buscar
#####################################################################

SampleType = Enum('Sample', 'train test') #Enum para diferenciar entre test y train

totalSources = [] #Lista donde se alamacenan el total de src de imagenes

getSRC = lambda x: x.get_attribute("src") #Función lambda para obtener el src de los elementos img

for currentPage in range(1,lastPageToSearch + 1):

    #Cargar la página con su respectiva paginación
    driver.get("https://www.shutterstock.com/search/{}?page={}".format(searchWord,currentPage))
    assert "No results found." not in driver.page_source

    #Se necesita que la página haga scroll hasta abajo ya que la página us alazy loading y solo carga los elementos al momento de que aparecen en pantalla
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(5) #5 segundos de espera

    #Busqueda de elementos con imagenes
    imageElements = driver.find_elements_by_xpath("//div[@class='z_h_b900b']/a/img")
    
    time.sleep(5) #5 segundos de espera
    
    #Lista con los src de las imagenes
    imageSources = list(map(getSRC, imageElements))
    assert "No images found." not in driver.page_source
    totalSources.extend(imageSources)

#Número total de imagenes recolectadas
totalImagesCollected = len(totalSources)

#Parición 80 a 20
pivot = math.floor(totalImagesCollected * .8)

#Declaración de conjuntos
trainSample = totalSources[:pivot]
testSample = totalSources[pivot:]

#Descarga de imagenes
downloadSamples(trainSample,SampleType.train.name)
downloadSamples(testSample,SampleType.test.name)

#Cerrar el navegador
driver.close()