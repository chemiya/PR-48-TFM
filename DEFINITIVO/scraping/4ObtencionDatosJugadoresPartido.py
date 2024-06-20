from bs4 import BeautifulSoup
import requests
import pandas as pd
URL_BASE="https://www.resultados-futbol.com/"








# dataframe donde se guardan los datos de los jugadores en los partidos de una liga y temporada
dataframe_datos_jugadores_partidos=pd.DataFrame(columns=['id_dato_jugador_partido','id_jugador', 'id_partido','titular','amarilla','roja','lesion','cambio','asistencias','goles','sustituido_por'])
# dataframe para guardar los nuevos jugadores detectados en la liga y temporada
dataframe_nuevos_jugadores=pd.DataFrame(columns=['id_jugador','nombre', 'posicion','id_equipo'])

id_dato_jugador=0
contador=0
indicador_resumen=0


import Constantes as const
#liga y temporada a analizar
ligas=const.ligas
temporadas=const.temporadas


# para cada liga y temporada se extraen los datos de los jugadores en los partidos de esa liga y temporada
for liga in ligas:
    for temporada in temporadas:
        print("Procesando: "+liga+"-"+str(temporada))
        partidos = pd.read_csv('csv/partidos-'+liga+'-'+str(temporada)+'.csv')
        equipos = pd.read_csv('csv/equipos-'+liga+'-'+str(temporada)+'.csv')
        jugadores = pd.read_csv('csv/jugadores-'+liga+'-'+str(temporada)+'.csv')
        id_jugador_nuevo=len(jugadores)
        tamano_partidos=len(partidos)


        try:
            # Intentar cargar el CSV
            partidos = pd.read_csv('csv/diferenciasPartidos-'+liga+'-'+str(temporada)+'.csv')
            print("Solo se actualizan partidos nuevos "+liga+'-'+str(temporada))
            partidos_existen=True
        except FileNotFoundError:
            partidos = pd.read_csv('csv/partidos-'+liga+'-'+str(temporada)+'.csv')
            print("No existen nuevos y se actualizan todos "+liga+'-'+str(temporada))
            partidos_existen=False

        

        #para cada uno de los partidos
        for index, row in partidos.iterrows():
            print("Procesando:"+str(indicador_resumen))
            indicador_resumen=indicador_resumen+1

            id_equipo_local = row['id_equipo_local']
            id_equipo_visitante = row['id_equipo_visitante']
            id_partido = row['id_partido']
            temporada = row['temporada']
            finalizado = row['finalizado']
            contador=contador+1


            #buscar datos de los finalizados 
            if finalizado==1:







                #encontramos nombre del equipo local
                resultado = equipos.loc[(equipos['id_equipo'] == id_equipo_local) & 
                                    (equipos['temporada'] == temporada) ]         
                if not resultado.empty:
                    local = resultado['nombre'].values[0]









                #encontramos nombre visitante
                resultado = equipos.loc[(equipos['id_equipo'] == id_equipo_visitante) & 
                                    (equipos['temporada'] == temporada) ]               
                if not resultado.empty:
                    visitante = resultado['nombre'].values[0]









                #abrimos url detalle del partido
                url = URL_BASE + "partido/" + local + '/' + visitante + '/' + str(temporada)
                response = requests.get(url)
                if response.status_code == 200:
                    alineacion_local = []
                    alineacion_visitante =[]
                    soup=BeautifulSoup(response.content,'html.parser')
                    jornada=soup.find('div',class_='jornada')
                    jornada=jornada.string









                    #lesiones, asistencias y cambios local
                    local_lesion=soup.find_all('span',class_="left event_4")
                    local_asistencias=soup.find_all('span',class_="left event_5")
                    local_salen=soup.find_all('span',class_="left event_6")
                    local_entran=soup.find_all('span',class_="left event_7")

                    lesiones_local=[]
                    for a in local_lesion:
                        nombre=a.find('a')
                        lesiones_local.append(nombre.string)

                    asistencia_local=[]
                    for a in local_asistencias:
                        nombre=a.find('a')
                        asistencia_local.append(nombre.string)

                    cambios_local={}
                    for salida, entrada in zip(local_salen, local_entran):
                        nombre_sale=salida.find('a').string
                        nombre_entra=entrada.find('a').string
                        cambios_local[nombre_sale]=nombre_entra
                        


                    







                    #lesiones, asistencias y cambios visitante
                    visitante_lesion=soup.find_all('span',class_="right event_4")
                    visitante_asistencia=soup.find_all('span',class_="right event_5")
                    visitante_salen=soup.find_all('span',class_="right event_6")
                    visitante_entran=soup.find_all('span',class_="right event_7")

                    lesiones_visitante=[]
                    for a in visitante_lesion:
                        nombre=a.find('a')
                        lesiones_visitante.append(nombre.string)

                    asistencia_visitante=[]
                    for a in visitante_asistencia:
                        nombre=a.find('a')
                        asistencia_visitante.append(nombre.string)

                    cambios_visitante={}
                    for salida, entrada in zip(visitante_salen, visitante_entran):
                        nombre_sale=salida.find('a').string
                        nombre_entra=entrada.find('a').string
                        cambios_visitante[nombre_sale]=nombre_entra
                    
                    






                    #datos sobre jugadores del local
                    try:
                        equipo_local=soup.find('div',class_='team team1')
                        equipo_local=equipo_local.find_all('li',class_='')
                    except:
                        raise
                    i=0
                    #recorro jugadores
                    for jugador in equipo_local:
                        if i<11:
                            titular=1
                        else:
                            titular=0
                        i=i+1


                        #comprobar si esta registrado
                        nombreH5=jugador.find('h5',class_='align-player')
                        nombre=nombreH5.string
                        sustituido_por="-1"
                        if nombreH5:
                            elemento_a = nombreH5.find('a')
                            if elemento_a and 'href' in elemento_a.attrs:
                                href = elemento_a['href']



                                #lo buscamos en csv jugadores
                                resultado = jugadores.loc[(jugadores['nombre'] == nombre) & 
                                    (jugadores['id_equipo'] == id_equipo_local) ]     
                                if not resultado.empty:
                                    id_jugador = resultado['id_jugador'].values[0]
                                else:


                                    #lo buscamos en dataframe nuevos
                                    resultado = dataframe_nuevos_jugadores.loc[(dataframe_nuevos_jugadores['nombre'] == nombre) & 
                                    (dataframe_nuevos_jugadores['id_equipo'] == id_equipo_local) ]     
                                    if not resultado.empty:
                                        id_jugador = resultado['id_jugador'].values[0]
                                    else:



                                        #abirmos url y lo guardamos en dataframe
                                        if "resultados-futbol" in href:
                                            url=href
                                        else:
                                            url = URL_BASE + href                               
                                        response1 = requests.get(url)                              
                                        if response1.status_code == 200:
                                            soup1=BeautifulSoup(response1.content,'html.parser') 
                                            tabla=soup1.find_all('div',class_='contentitem') 
                                            if len(tabla)>0:
                                                texto_tabla=tabla[1] 
                                                elementos=soup1.find_all('dd')
                                                valores_elementos=[]
                                                for dd in elementos:
                                                    valores_elementos.append(dd.text)
                                                if "Portero" in valores_elementos:
                                                    posicion="Portero"
                                                elif "Defensa" in valores_elementos:
                                                    posicion="Defensa"
                                                elif"Centrocampista" in valores_elementos:
                                                    posicion="Centrocampista"
                                                elif "Delantero" in valores_elementos:
                                                    posicion="Delantero"


                                                #print("Se guarda en el dataframe de nuevos jugadores "+nombre) 
                                                dataframe_nuevos_jugadores.loc[len(dataframe_nuevos_jugadores)]=[id_jugador_nuevo,nombre,posicion,id_equipo_local]
                                                id_jugador_nuevo=id_jugador_nuevo+1
                                            else:
                                                print("CUIDADO PARA------------------")
                                                print(url)






                        
                        #comprobar amarilla
                        eventos=jugador.find('div',class_='align-events')
                        if None is eventos:
                            continue
                        if eventos.find('span',class_='flaticon-live-5'):
                            amarilla="1"
                        else:
                            amarilla="0"








                        #comprobar goles
                        if eventos.find('span',class_='flaticon-goal'):
                            gol=eventos.find('span',class_='flaticon-goal')
                            if gol.find('b',class_=''):
                                gol=gol.find('b',class_='')
                                gol=gol.string
                            else:
                                gol="1"
                        else:
                            gol="0"





                        #comprobar por quien se sustituye
                        if eventos.find('span',class_='flaticon-up12'):
                            cambio=eventos.find('span',class_='flaticon-up12')
                            cambio=cambio.string
                            if nombre in cambios_local:
                                sustituido_por = cambios_local[nombre]




                                # se busca el id con el nombre en csv
                                resultado = jugadores.loc[(jugadores['nombre'] == sustituido_por) & 
                                    (jugadores['id_equipo'] == id_equipo_local) ]     
                                if not resultado.empty:
                                    sustituido_por = resultado['id_jugador'].values[0]
                                else:
                                    #si no se busca en nuevos_jugadores
                                    resultado = dataframe_nuevos_jugadores.loc[(dataframe_nuevos_jugadores['nombre'] == sustituido_por) & 
                                    (dataframe_nuevos_jugadores['id_equipo'] == id_equipo_local) ] 
                                    if not resultado.empty:
                                        sustituido_por = resultado['id_jugador'].values[0]
                                                    
                        else:
                            cambio="-1"








                        #comrpobar roja
                        if eventos.find('span',class_='flaticon-live-3'):
                            roja="1"
                        else:
                            roja="0"
                        if eventos.find('span',class_='flaticon-live-4'):
                            roja="1"
                            amarilla="2"
                        




                        #comprobar lesion
                        lesion='0'
                        for a in lesiones_local:
                            if a == nombre:
                                lesion='1'





                        #comprobar asistencia 
                        asistencia=0
                        for a in asistencia_local:
                            if a == nombre:
                                asistencia=asistencia+1




                        #comrpobar cambio
                        jugador=nombre
                        if cambio!="":
                            if cambio[1]=="'":
                                cambio=cambio[:1]
                            else:
                                cambio=cambio[:2]    
                        equipo=local





                        #buscamos id del jugador en csv jugadores
                        resultado = jugadores.loc[(jugadores['nombre'] == nombre) & 
                                    (jugadores['id_equipo'] == id_equipo_local) ] 
                        if not resultado.empty:
                            id_jugador = resultado['id_jugador'].values[0]
                        else:
                            #si no lo buscamos en los nuevos
                            resultado = dataframe_nuevos_jugadores.loc[(dataframe_nuevos_jugadores['nombre'] == nombre) & 
                                    (dataframe_nuevos_jugadores['id_equipo'] == id_equipo_local) ] 
                            if not resultado.empty:
                                id_jugador = resultado['id_jugador'].values[0]

                        dataframe_datos_jugadores_partidos.loc[len(dataframe_datos_jugadores_partidos)]=[id_dato_jugador,id_jugador,id_partido,titular,amarilla,roja,lesion,cambio,asistencia,gol,sustituido_por]
                        id_dato_jugador=id_dato_jugador+1








                    #datos sobre jugadores del visitante
                    equipo_visitante=soup.find('div',class_='team team2')
                    equipo_visitante=equipo_visitante.find_all('li',class_='')
                    i=0

                    #recorremos jugadores
                    for jugador in equipo_visitante:
                        if i<11:
                            titular=1
                        else:
                            titular=0 
                        i=i+1

                        nombreH5=jugador.find('h5',class_='align-player')
                        nombre=nombreH5.string
                        sustituido_por="-1"
                        if nombreH5:
                            elemento_a = nombreH5.find('a')
                            if elemento_a and 'href' in elemento_a.attrs:
                                href = elemento_a['href']
                                resultado = jugadores.loc[(jugadores['nombre'] == nombre) & 
                                    (jugadores['id_equipo'] == id_equipo_visitante) ]     
                                if not resultado.empty:
                                    id_jugador = resultado['id_jugador'].values[0]
                                else:
                                    resultado = dataframe_nuevos_jugadores.loc[(dataframe_nuevos_jugadores['nombre'] == nombre) & 
                                    (dataframe_nuevos_jugadores['id_equipo'] == id_equipo_visitante) ]     
                                    if not resultado.empty:
                                        id_jugador = resultado['id_jugador'].values[0]
                                    else:
                                        #print("jugador del visitante ni en dataframe ni csv")
                                        url = URL_BASE + href
                                        response2 = requests.get(url)
                                        if response2.status_code == 200:
                                            soup2=BeautifulSoup(response2.content,'html.parser') 
                                            tabla=soup2.find_all('div',class_='contentitem') 
                                            if len(tabla)>0:
                                                texto_tabla=tabla[1] 
                                                elementos=soup2.find_all('dd')
                                                valores_elementos=[]
                                                for dd in elementos:
                                                    valores_elementos.append(dd.text)
                                                if "Portero" in valores_elementos:
                                                    posicion="Portero"
                                                elif "Defensa" in valores_elementos:
                                                    posicion="Defensa"
                                                elif"Centrocampista" in valores_elementos:
                                                    posicion="Centrocampista"
                                                elif "Delantero" in valores_elementos:
                                                    posicion="Delantero"
                                                        
                                                dataframe_nuevos_jugadores.loc[len(dataframe_nuevos_jugadores)]=[id_jugador_nuevo,nombre,posicion,id_equipo_visitante]
                                                id_jugador_nuevo=id_jugador_nuevo+1
                                            else:
                                                print("CUIDADO PARA------------------")
                                                print(url)



                        #amarillas
                        eventos=jugador.find('div',class_='align-events')
                        if None is eventos:
                            continue
                        if eventos.find('span',class_='flaticon-live-5'):
                            amarilla="1"
                        else:
                            amarilla="0"

                        #goles
                        if eventos.find('span',class_='flaticon-goal'):
                            gol=eventos.find('span',class_='flaticon-goal')
                            if gol.find('b',class_=''):
                                gol=gol.find('b',class_='')
                                gol=gol.string
                            else:
                                gol="1"
                        else:
                            gol="0"

                        #sustituido
                        if eventos.find('span',class_='flaticon-up12'):
                            cambio=eventos.find('span',class_='flaticon-up12')
                            cambio=cambio.string
                            if nombre in cambios_visitante:
                                sustituido_por = cambios_visitante[nombre]
                                #buscamos id de quien lo sustituye
                                resultado = jugadores.loc[(jugadores['nombre'] == sustituido_por) & 
                                    (jugadores['id_equipo'] == id_equipo_visitante) ]     
                                if not resultado.empty:
                                    sustituido_por = resultado['id_jugador'].values[0]
                                else:
                                    resultado = dataframe_nuevos_jugadores.loc[(dataframe_nuevos_jugadores['nombre'] == sustituido_por) & 
                                    (dataframe_nuevos_jugadores['id_equipo'] == id_equipo_visitante) ]     
                                    if not resultado.empty:
                                        sustituido_por = resultado['id_jugador'].values[0]
                        else:
                            cambio="-1"

                        #rojas
                        if eventos.find('span',class_='flaticon-live-3'):
                            roja="1"
                        else:
                            roja="0"
                        if eventos.find('span',class_='flaticon-live-4'):
                            roja="1"
                            amarilla="2"

                        #lesion
                        lesion=0
                        for a in lesiones_visitante:
                            if a == nombre:
                                lesion=1

                        #asistencias
                        asistencia=0
                        for a in asistencia_visitante:
                            if a == nombre:
                                asistencia=asistencia+1

                        #cambio
                        jugador=nombre
                        if cambio!="":
                            if cambio[1]=="'":
                                cambio=cambio[:1]
                            else:
                                cambio=cambio[:2]
                        equipo=visitante

                        #buscamos id del jugador
                        resultado = jugadores.loc[(jugadores['nombre'] == nombre) & 
                                    (jugadores['id_equipo'] == id_equipo_visitante) ]  
                        if not resultado.empty:
                            id_jugador = resultado['id_jugador'].values[0]
                        else:
                            resultado = dataframe_nuevos_jugadores.loc[(dataframe_nuevos_jugadores['nombre'] == nombre) & 
                                    (dataframe_nuevos_jugadores['id_equipo'] == id_equipo_visitante) ]  
                            if not resultado.empty:
                                id_jugador = resultado['id_jugador'].values[0]

                        dataframe_datos_jugadores_partidos.loc[len(dataframe_datos_jugadores_partidos)]=[id_dato_jugador,id_jugador,id_partido,titular,amarilla,roja,lesion,cambio,asistencia,gol,sustituido_por]
                        id_dato_jugador=id_dato_jugador+1
            else:
                break



        #dataframe_nuevos_jugadores.to_csv('csv/nuevos.csv', index=False)

        # convertimos si el que sustituye esta con nombre a id
        for i, valor in enumerate(dataframe_datos_jugadores_partidos['sustituido_por']):
            try:
                num = pd.to_numeric(valor)
            except:
                resultado = dataframe_nuevos_jugadores.loc[(dataframe_nuevos_jugadores['nombre'] == valor)  ]  
                if not resultado.empty:
                    id_jugador = resultado['id_jugador'].values[0]
                    dataframe_datos_jugadores_partidos.at[i, 'sustituido_por'] = id_jugador


        if partidos_existen==False:
            # guardamos los datos de los jugadores en los partidos de una liga y temporada
            dataframe_datos_jugadores_partidos.to_csv('csv/datosJugadoresPartidos-'+liga+'-'+str(temporada)+'.csv', index=False)   
            # vaciamos
            dataframe_datos_jugadores_partidos = dataframe_datos_jugadores_partidos.drop(dataframe_datos_jugadores_partidos.index) 
            
        else:
            # guardamos los datos de los jugadores en los partidos de una liga y temporada
            dataframe_datos_jugadores_partidos.to_csv('csv/datosJugadoresPartidos-'+liga+'-'+str(temporada)+'.csv',mode='a', index=False)   
            # vaciamos
            dataframe_datos_jugadores_partidos = dataframe_datos_jugadores_partidos.drop(dataframe_datos_jugadores_partidos.index) 




        # guardamos los nuevos jugadores detectados
        dataframe_nuevos_jugadores.to_csv('csv/jugadores-'+liga+'-'+str(temporada)+'.csv', mode='a', header=False, index=False)   
        # vaciamos 
        dataframe_nuevos_jugadores = dataframe_nuevos_jugadores.drop(dataframe_nuevos_jugadores.index)      