from bs4 import BeautifulSoup
import requests
import pandas as pd
URL_BASE="https://www.resultados-futbol.com/"



from datetime import datetime

def convertir_fecha(texto_fecha):
    
    meses = {"Ene": 1, "Feb": 2, "Mar": 3, "Abr": 4, "May": 5, "Jun": 6,
             "Jul": 7, "Ago": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dic": 12}
    
    dia, mes, anio = texto_fecha.split()
    num_mes = meses[mes]
    anio = "20" + anio
    fecha_obj = datetime(int(anio), num_mes, int(dia))
    return fecha_obj



#liga y temporada a analizar
ligas=['bundesliga']
temporadas=[2022,2023,2024]

#dataframe donde se guardaran los partidos
dataframe_partidos=pd.DataFrame(columns=['id_partido','fecha','temporada', 'liga','jornada','id_equipo_local','id_equipo_visitante','finalizado'])
id_partido=0


# para cada liga y temporada se extraen los partidos
for liga in ligas:
    for temporada in temporadas:
        print("Procesando: "+liga+"-"+str(temporada))
        equipos = pd.read_csv('csv/equipos-'+liga+'-'+str(temporada)+'.csv')



        try:
            # Intentar cargar el CSV
            partidos = pd.read_csv('csv/partidos-'+liga+'-'+str(temporada)+'.csv')
            print("Fichero con partidos ya existe para "+liga+'-'+str(temporada))
            partidos_existen=True
        except FileNotFoundError:
            print("Fichero con partidos no existe para "+liga+'-'+str(temporada))
            partidos_existen=False




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

        #convertimos la fecha a un formato que se pueda ordenar
        dataframe_partidos["fecha"] = dataframe_partidos["fecha"].apply(convertir_fecha)
        #ordenamos
        dataframe_partidos = dataframe_partidos.sort_values(by="fecha")

        if partidos_existen==True:
            # Asegurar que ambos DataFrames tienen el mismo índice
            dataframe_partidos = dataframe_partidos.reset_index(drop=True)
            partidos = partidos.reset_index(drop=True)

            # Comparar las columnas específicas y encontrar las filas diferentes
            diferencias = dataframe_partidos[dataframe_partidos['finalizado'] != partidos['finalizado']]

            if len(diferencias)>0:
                #guardamos los partidos que se han jugado nuevos
                diferencias.to_csv('csv/diferenciasPartidos-'+liga+'-'+str(temporada)+'.csv', index=False) 
                # vaciamos
                diferencias = diferencias.drop(diferencias.index) 

        #guardamos los partidos de una determinada liga y temporada
        dataframe_partidos.to_csv('csv/partidos-'+liga+'-'+str(temporada)+'.csv', index=False) 
        # vaciamos
        dataframe_partidos = dataframe_partidos.drop(dataframe_partidos.index) 

