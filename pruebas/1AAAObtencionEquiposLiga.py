from bs4 import BeautifulSoup
import requests
import pandas as pd
URL_BASE="https://www.resultados-futbol.com/"







#equipos de la liga-----------------------------------------------------------
ligas=['primera']
temporadas=[2024]

dataframe_equipos=pd.DataFrame(columns=['id_equipo','temporada', 'liga','nombre'])
id_equipo=0



for liga in ligas:
    for temporada in temporadas:
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



dataframe_equipos.to_csv('csv/equipos.csv', index=False)              
    


        
        