

from bs4 import BeautifulSoup
import requests
import pandas as pd
import glob
import os

URL_BASE="https://www.resultados-futbol.com/"



#dataframe donde se guardaran los jugadores
dataframe_jugadores=pd.DataFrame(columns=['id_jugador','nombre', 'posicion','id_equipo'])
id_jugador=0

#liga y temporada a analizar
ligas=['premier']
temporadas=[2022,2023,2024]


# para cada liga y temporada, se extraen los jugadores de cada equipo
for liga in ligas:
    for temporada in temporadas:
        print("Procesando: "+liga+'-'+str(temporada))    
        equipos = pd.read_csv('csv/equipos-'+liga+'-'+str(temporada)+'.csv')

        #recorremos equipos
        for index, row in equipos.iterrows():
            equipo = row['nombre']
            id_equipo = row['id_equipo']

            url = URL_BASE + 'plantilla/' + equipo + '/' + str(temporada)
            response = requests.get(url)
            if response.status_code == 200:
                soup=BeautifulSoup(response.content,'html.parser')
                results=soup.find(class_='sdata_table')


                if results is None:
                    print("Nada")
                tabla=results.find('tbody')
                if tabla is None:
                    print("Nada")
                filas=tabla.find_all('tr')
                if filas is None:
                    print("Nada")
                posicion=""


                #recorrer cada uno de los jugadores
                for i in filas:
                    s=i.find('th').string
                    if s in ("Portero","Defensa","Centrocampista","Delantero"):
                        posicion=s
                        continue

                    #insertar el jugador
                    nombre=i.find(class_='sdata_player_name')
                    nombre=nombre.find('span').string
                    dataframe_jugadores.loc[len(dataframe_jugadores)]=[id_jugador,nombre,posicion,id_equipo]
                    id_jugador=id_jugador+1


        #guardamos los jugadores de cada equipo para esa liga y temporada
        dataframe_jugadores.to_csv('csv/jugadores-'+liga+'-'+str(temporada)+'.csv',encoding='utf-8', index=False) 
        # vaciamos
        dataframe_jugadores = dataframe_jugadores.drop(dataframe_jugadores.index) 
        



           