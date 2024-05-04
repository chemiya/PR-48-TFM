

from bs4 import BeautifulSoup
import requests
import pandas as pd
URL_BASE="https://www.resultados-futbol.com/"

equipos = pd.read_csv('csv/equipos.csv')
dataframe_jugadores=pd.DataFrame(columns=['id_jugador','nombre', 'posicion','id_equipo'])
id_jugador=0


#recorremos equipos
for index, row in equipos.iterrows():
    equipo = row['nombre']
    temporada = row['temporada']
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
            

dataframe_jugadores.to_csv('csv/jugadores.csv',encoding='utf-8', index=False) 



           