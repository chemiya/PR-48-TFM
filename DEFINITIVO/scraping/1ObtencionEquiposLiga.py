from bs4 import BeautifulSoup
import requests
import pandas as pd
URL_BASE="https://www.resultados-futbol.com/"





import Constantes as const
#liga y temporada a analizar
ligas=const.ligas
temporadas=const.temporadas

#dataframe donde se guardaran los equipos
dataframe_equipos=pd.DataFrame(columns=['id_equipo','temporada', 'liga','nombre'])
id_equipo=0


# para cada liga y temporada se extraen los equipos
for liga in ligas:
    for temporada in temporadas:
        print("Procesando: "+liga+'-'+str(temporada))   
        url = URL_BASE + liga + str(temporada)
        response = requests.get(url)
        if response.status_code == 200:
            soup=BeautifulSoup(response.content,'html.parser')
            teamList = soup.find_all('li',class_='shield')

            #cada uno de los equipos encontrados
            for team in teamList:
                clave = team.find('a').attrs['href']
                clave = clave.strip('/')
                dataframe_equipos.loc[len(dataframe_equipos)]=[id_equipo,temporada,liga,clave]
                id_equipo=id_equipo+1

            #guardamos equipos de la liga y temporada
            dataframe_equipos.to_csv('csv/equipos-'+liga+'-'+str(temporada)+'.csv', index=False)    
            # vaciamos
            dataframe_equipos = dataframe_equipos.drop(dataframe_equipos.index) 
                  
    


        
        