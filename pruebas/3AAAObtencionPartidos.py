from bs4 import BeautifulSoup
import requests
import pandas as pd
URL_BASE="https://www.resultados-futbol.com/"


try:
    partidos = pd.read_csv('csv/partidos.csv')
    print("Ya existen partidos registrados, por lo tanto se actualizan valores")
    cargar_todos=False
except FileNotFoundError:
    print("No existen partidos registrados.")
    cargar_todos=True



equipos = pd.read_csv('csv/equipos.csv')
#ligas=['bundesliga','premier','primera','serie_a']
#temporadas=[2020,2021,2022,2023]
ligas=['primera']
temporadas=[2024]
dataframe_partidos=pd.DataFrame(columns=['id_partido','fecha','temporada', 'liga','jornada','id_equipo_local','id_equipo_visitante','finalizado'])
id_partido=0


if cargar_todos==True:
    for liga in ligas:
        for temporada in temporadas:
            url = URL_BASE + liga + str(temporada) + '/grupo' + str(1) + '/calendario'
            response = requests.get(url)
            if response.status_code == 200:
                soup=BeautifulSoup(response.content,'html.parser')
                results=soup.find('div',class_="b2col-container col-calendar-content")
                jornadas=results.find_all('div',id='col-resultados')


                #recorremos jornadas
                for jornada in jornadas:
                    jor=jornada.find('div',class_='boxtop')
                    jor=str(jor.find('span',class_='titlebox').string)
                    jor=jor.split(' ')
                    jor=jor[1]
                    datos=jornada.find_all('tr')


                    #analizamos cada uno de los datos del partido de la jornada
                    for i in datos:
                        fecha=i.find('td',class_='fecha')
                        local=i.find('td',class_='equipo1')
                        visitante=i.find('td',class_='equipo2')
                        local = local.find('a').attrs['href'].split('/')[1]
                        visitante = visitante.find('a').attrs['href'].split('/')[1]
                        resultado=i.find('td',class_='rstd')
                        resultado=resultado.find('a',class_='url')
                        jornada = jor
                        fecha=fecha.string



                        #comprobar si el partido ha finalizado
                        if resultado is None:
                            resultado="Aplazado"
                        else:
                            resultado=resultado.string
                            if "x" in resultado or ":" in resultado:
                                finalizado=0
                            else:
                                finalizado=1



                        #encontrar id del equipo local
                        resultado = equipos.loc[(equipos['nombre'] == local) & 
                            (equipos['temporada'] == temporada) & 
                            (equipos['liga'] == liga)]
                        if not resultado.empty:
                            id_equipo_local = resultado['id_equipo'].values[0]
                        else:
                            print(f"No se encontró el equipo {local} en la temporada {temporada} y liga {liga}")



                        #encontrar id del equipo visitante
                        resultado = equipos.loc[(equipos['nombre'] == visitante) & 
                            (equipos['temporada'] == temporada) & 
                            (equipos['liga'] == liga)]
                        if not resultado.empty:
                            id_equipo_visitante = resultado['id_equipo'].values[0]
                        else:
                            print(f"No se encontró el equipo {visitante} en la temporada {temporada} y liga {liga}")

                        
                        dataframe_partidos.loc[len(dataframe_partidos)]=[id_partido,fecha, temporada,liga,jornada,id_equipo_local,id_equipo_visitante,finalizado]
                        id_partido=id_partido+1

dataframe_partidos.to_csv('csv/partidos.csv', index=False) 