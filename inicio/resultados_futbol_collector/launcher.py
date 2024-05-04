#!/usr/bin/python
# -*- coding: utf-8 -*-


#Host: http://t4t.infor.uva.es
#Usuario: usuario
#Pass: tfm2024




import os, sys
import os.path
from os import path
import multiprocessing
from itertools import repeat
import csv_tools
import excel_generator 

#leagues = ['bundesliga','premier','primera','serie_a']
leagues = ['bundesliga','premier','primera','serie_a']
seasons = range(2016,2021)

NUMBER_OF_PROCESSES = 5


#crea carpetas para cada liga
def generateEnvironment(ruta):
    if (not path.exists(ruta)):
        os.mkdir(ruta)
    for league in leagues:
        nueva_ruta = os.path.join(ruta,league)

        if (not path.exists(nueva_ruta)):
            os.mkdir(nueva_ruta)

def generateFiles(ruta):
    for league in leagues:
        file_path = os.path.join(ruta,league)
        for season in seasons:
            excel_generator.createExcelObject(league,str(season),file_path)

def generateFilesParallel(ruta):
    runInParallel(league,seasons,file_path)


#crea excel con los datos de una liga en una temporada
def generateFilesSingleSeason(league,season,ruta):
    file_path = os.path.join(ruta,league)
    excel_generator.createExcelObject(league,str(season),file_path)

def main():
    current_path = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(current_path,'results')
    generateEnvironment(ruta)
    
    #generateFiles(ruta)
    generateFilesSingleSeason('premier',2017,ruta)

    #concatenateFiles(ruta)

def concatenateFiles(ruta):
    directorios = [new_dir for new_dir in os.listdir(ruta) if os.path.isdir(os.path.join(ruta,new_dir))]

    for directorio in directorios:
        directorio_actual = os.path.join(ruta,directorio)
        file_list = [os.path.join(directorio_actual,new_dir) for new_dir in os.listdir(directorio_actual) if not os.path.isdir(os.path.join(directorio_actual,new_dir))]
        file_name = os.path.join(directorio_actual,directorio + '.csv')
        print('working on: ' + directorio + '.csv ...')
        csv_tools.combineCsvList(file_list, file_name)
        
def runInParallel(league, season, path):
    with multiprocessing.Pool(processes=NUMBER_OF_PROCESSES) as pool:
        pool.starmap(excel_generator.createExcelObject,zip(repeat(league),season,repeat(path)))

  
  


if __name__ == "__main__":
    main()