from bs4 import BeautifulSoup
import requests
import pandas as pd
URL_BASE="https://www.resultados-futbol.com/"

partidos = pd.read_csv('csv/partidos.csv')
equipos = pd.read_csv('csv/equipos.csv')

#ligas=['bundesliga','premier','primera','serie_a']
#temporadas=[2020,2021,2022,2023]

dataframe_datos_partidos_jugados=pd.DataFrame(columns=['id_datos_partido_jugado', 'id_partido','resultado_local','resultado_visitante','cambios_local','cambios_visitante','amarillas_local','amarillas_visitante','rojas_local','rojas_visitante','corners_local','corners_visitante','posesion_local','posesion_visitante','total_tiros_local','total_tiros_visitante'])
id_dato_partido_jugado=0

tamano_partidos=len(partidos)
indicador_resumen=0

#recorremos partidos
for index, row in partidos.iterrows():
    print("Procesando:"+str(indicador_resumen)+"/"+str(tamano_partidos))
    indicador_resumen=indicador_resumen+1

    id_equipo_local = row['id_equipo_local']
    id_equipo_visitante = row['id_equipo_visitante']
    id_partido = row['id_partido']
    temporada = row['temporada']
    finalizado = row['finalizado']


    #si esta finalizado
    if finalizado==1:
        #buscamos nombre del local
        resultado = equipos.loc[(equipos['id_equipo'] == id_equipo_local) & 
                            (equipos['temporada'] == temporada) ]            
        if not resultado.empty:
            local = resultado['nombre'].values[0]
        else:
            print(f"No se encontró el equipo {id_equipo_local} en la temporada {temporada}")

        #buscamos nombre del visistante
        resultado = equipos.loc[(equipos['id_equipo'] == id_equipo_visitante) & 
                            (equipos['temporada'] == temporada) ]             
        if not resultado.empty:
            visitante = resultado['nombre'].values[0]
        else:
            print(f"No se encontró el equipo {id_equipo_visitante} en la temporada {temporada}")



        #abrimos url detalle partido
        url = URL_BASE + "partido/" + local + '/' + visitante + '/' + str(temporada)
        response = requests.get(url)
        if response.status_code == 200:
            soup=BeautifulSoup(response.content,'html.parser')
            jornada=soup.find('div',class_='jornada')
            jornada=jornada.string

            #obtenemos datos amarillas y rojas
            amarillas_equipos=soup.find_all('span',class_="am")
            amarillas_local=amarillas_equipos[0].string
            amarillas_visitante=amarillas_equipos[1].string
            rojas_equipos=soup.find_all('span',class_="ro")
            rojas_local=rojas_equipos[0].string
            rojas_visitante=rojas_equipos[1].string
            datos_tabla=soup.find_all('tr',class_="barstyle bar4")
            contador_tr=0


            local_salen=soup.find_all('span',class_="left event_6")
            visitante_salen=soup.find_all('span',class_="right event_6")

            cambios_local=len(local_salen)
            cambios_visitante=len(visitante_salen)

            #procesamos datos tabla
            for dato_tabla in datos_tabla:
                tds = dato_tabla.find_all('td')
                primer_td = tds[0].text.strip()
                segundo_td = tds[1].text.strip()
                tercer_td = tds[2].text.strip()
                if segundo_td=='Goles':
                    resultado_local=primer_td
                    resultado_visitante=tercer_td
                elif segundo_td=='Posesión del balón':
                    posesion_local=primer_td[:-1]
                    posesion_visitante=tercer_td[:-1]
                elif segundo_td=='Total tiros':
                    total_tiros_local=primer_td
                    total_tiros_visitante=tercer_td
                elif segundo_td=='Saques de esquina':
                    corners_local=primer_td
                    corners_visitante=tercer_td
                contador_tr=contador_tr+1
            

            dataframe_datos_partidos_jugados.loc[len(dataframe_datos_partidos_jugados)]=[
                    id_dato_partido_jugado,id_partido,resultado_local,resultado_visitante,cambios_local,cambios_visitante,amarillas_local,amarillas_visitante,rojas_local,rojas_visitante,corners_local,corners_visitante,posesion_local,posesion_visitante,total_tiros_local,total_tiros_visitante
                ]
            id_dato_partido_jugado=id_dato_partido_jugado+1
    else:
        break

dataframe_datos_partidos_jugados.to_csv('csv/datosPartidosJugados.csv', index=False)            