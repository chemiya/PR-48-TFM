#!/usr/bin/python
# -*- coding: utf-8 -*-
# import os.path

from os import path
import locale
import csv
import csv_tools
import requests
from datetime import datetime
import data_collect as dc

locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')
SUFFIX = '.csv'
class Excel:
    pass

class estadisticas_acumuladas_equipo:
    equipo = ""
    goles_acumulados = 0
    cambios_acumulados = 0
    cambios_portero_acumulados = 0
    cambios_defensa_acumulados = 0
    cambios_centrocampista_acumulados = 0
    cambios_delantero_acumulados = 0
    suma_tiempo_cambio_acumulado = 0
    lesion_acumulados = 0
    amarilla_acumulados = 0
    roja_acumulados = 0
    goleador_jornada_anterior = ''

    alineacion_jornada_anterior = []

class Cambio_Minuto_Posiciones:
    minuto= ''
    posicion_sale = ''
    posicion_entra = ''


def createExcelObject(league,season,ruta):
    season = str(season)
    print(league + '_' + season)
    s = requests.session()
    #coge los datos de los equipos de la liga
    teams_dict = dc.getTeamsFromLeague(league,season,s)
    teams = teams_dict.keys()
    jornadas = (len(teams)*2)-2
    primera_ejecucion = 1

    #coge los datos de un equipo
    teams_info_dict = dc.getAllTeamsInfo(league,season,teams_dict,s)

    #Diccionario con todas las plantillas de cada equipo de la temporada
    datos_acumulados = dict()
    plantilla = dict()
    for team in teams:
        o = estadisticas_acumuladas_equipo()
        o.equipo = team
        datos_acumulados[team]=o

        #coge datos de la plantilla
        plantilla[team] = dc.getPlantilla(team,season,s)

    #coge los partidos
    partidos = dc.getPartidos(league,season,'1',s)
    
    #Diccionario para almacenar la alineacion de la jornada anterior 
    alineacion_jornada_anterior=dict()
    clasificacion_jornada_anterior = []
    
    #Lista donde se almacenan las estadisiticas resultantes
    data = []
    for jornada in range(1,jornadas+1):

        clasificacion = dc.getClasificacion(league,season,'1',jornada,s)

        partidos_jornada = [j for j in partidos if (j.jornada == str(jornada))]
        
        for clasificacion_equipo in clasificacion:

            output_object = Excel()

            #Datos comunes 
            setattr(output_object,'01-Liga',league)
            setattr(output_object,'02-Temporada',season)
            setattr(output_object,'03-Jornada',jornada)

            #Datos obtenidos de la clase Clasificacion
            setattr(output_object,'04-tiempo',1000 + ((int(season) - 2015 )* jornadas) + jornada)
            setattr(output_object,'05-Equipo',teams_dict[clasificacion_equipo.nombre])
            setattr(output_object,'06-Posicion',clasificacion_equipo.posicion)
            setattr(output_object,'07-Puntos',clasificacion_equipo.puntos)
            setattr(output_object,'08-Goles a Favor',clasificacion_equipo.gfavor)
            setattr(output_object,'09-Goles en Contra',clasificacion_equipo.gcontra)

            #Datos obtenidos de la clase Equipo 
            #TODO puede estar bien sacar la petición fuera para que se haga a la vez
            #equipo_object = dc.getTeamInfo(clasificacion_equipo.nombre,season)
            setattr(output_object,'51-Entrenador',teams_info_dict[clasificacion_equipo.nombre].entrenador)

            local_visitante = ''
            rival = ''
            partido_object = object
            for partido in partidos_jornada:
                if(partido.local == clasificacion_equipo.nombre):
                    partido_object = partido
                    rival = partido.visitante
                    local_visitante ='local'
                    break
                elif(partido.visitante == clasificacion_equipo.nombre):
                    partido_object = partido
                    rival = partido.local
                    local_visitante ='visitante'
                    break
        
            #Datos obtenidos de la clase partido 
            setattr(output_object,'10-Local/Visitante',local_visitante)
            setattr(output_object,'11-Resultado',partido_object.resultado)

            #Calculo puntos en partido
            resultado_lista = partido_object.resultado.split('-')
            puntos_partido = 0
            if(local_visitante == 'local'):
                if resultado_lista[0] > resultado_lista[-1]:
                    puntos_partido = 3
                if resultado_lista[0] < resultado_lista[-1]:
                    puntos_partido = 0
                if resultado_lista[0] == resultado_lista[-1]:
                    puntos_partido = 1
            else:
                if resultado_lista[0] > resultado_lista[-1]:
                    puntos_partido = 0
                if resultado_lista[0] < resultado_lista[-1]:
                    puntos_partido = 3
                if resultado_lista[0] == resultado_lista[-1]:
                    puntos_partido = 1

            setattr(output_object,'50-Puntos obtenidos',puntos_partido)

            
            goles_partido = ''
            if(local_visitante == 'local'):
                goles_partido = partido_object.resultado.split('-')[0]
            else:
                goles_partido = partido_object.resultado.split('-')[1]
            
            setattr(output_object,'12-Goles en Partido',goles_partido.strip(' '))
            
            #Datos obtenidos de la clase Alineacion 
            try:
                alineacion_local,alineacion_visitante = dc.getAlineacion(partido_object.local,partido_object.visitante,season,s)
            except Exception as x:
                print("ERROR AT: Jornada " + str(jornada) + " Partido " + partido.local + "-" + partido.visitante )
                continue
            
            #TODO arreglar esta chapuza
            if alineacion_local is None:
                continue

            if(local_visitante == 'local'):
                alineacion_object = alineacion_local
                #alineacion_object_rival = alineacion_visitante
            else:
                alineacion_object = alineacion_visitante
                #alineacion_object_rival = alineacion_local

            #Calculos cambios 
            cambios_partido = 0
            cambios_portero = 0
            cambios_defensa = 0
            cambios_centrocampista = 0
            cambios_delantero = 0

            dato_dictomico_cambio_lesion = 0
            dato_dictomico_cambio_amarilla = 0 
            dato_dictomico_cambio_roja = 0
            
            lista_cambios = []

            #Filtrado de la alineacion
            alineacion_cambios = [j for j in alineacion_object if (j.cambio != "" and j.estado == "Titular")]
            alineacion_cambios_suplentes = [j for j in alineacion_object if (j.cambio != "" and j.estado == "Suplente")]

            lista_plantilla = plantilla[clasificacion_equipo.nombre]

            for jugador in alineacion_cambios:
                
                jugador_plantilla = next((x for x in lista_plantilla if x.nombre == jugador.jugador), None)
                cambio_object = Cambio_Minuto_Posiciones()
                cambio_object.minuto = jugador.cambio

                if jugador_plantilla is not None:
                    if(jugador_plantilla.posicion == "Portero"):
                        cambio_object.posicion_sale = 'Portero'
                        cambios_portero = cambios_portero + 1
                    elif(jugador_plantilla.posicion == "Defensa"):
                        cambio_object.posicion_sale = 'Defensa'
                        cambios_defensa = cambios_defensa + 1
                    elif(jugador_plantilla.posicion == "Centrocampista"):
                        cambio_object.posicion_sale = 'Centrocampista'
                        cambios_centrocampista = cambios_centrocampista + 1
                    elif(jugador_plantilla.posicion == "Delantero"):
                        cambio_object.posicion_sale = 'Delantero'
                        cambios_delantero = cambios_delantero + 1

                if (str(jugador.lesion) != '0'):
                    dato_dictomico_cambio_lesion = 1
                if (jugador.amarilla != '0'):
                    dato_dictomico_cambio_amarilla = 1
                if (jugador.roja != '0'):
                    dato_dictomico_cambio_roja = 1

                lista_cambios.append(cambio_object)

            for jugador_suplente in alineacion_cambios_suplentes:
                jugador_plantilla_suplente = next((x for x in lista_plantilla if x.nombre == jugador_suplente.jugador), None)
                cambio = next((x for x in lista_cambios if x.minuto == jugador_suplente.cambio), None)
                #TODO Arreglado el bug de los cambios raros pero echarle un ojo
                if((cambio is not None) and (jugador_plantilla_suplente is not None)):
                    cambio.posicion_entra = jugador_plantilla_suplente.posicion

            cambios_partido = len(alineacion_cambios)

            #Cambios durante el partido
            setattr(output_object,'13-Cambios realizados partido',cambios_partido)

            setattr(output_object,'15-Cambios realizados portero partido',cambios_portero)
            setattr(output_object,'17-Cambios realizados defensa partido',cambios_defensa)
            setattr(output_object,'19-Cambios realizados centrocampista partido',cambios_centrocampista)
            setattr(output_object,'21-Cambios realizados delantero partido',cambios_delantero)

            #Objeto de datos acumulados
            datos_acumulados_object = datos_acumulados[clasificacion_equipo.nombre]

            #Cambios acumulados
            cambios_acumulados = datos_acumulados_object.cambios_acumulados + cambios_partido
            setattr(output_object,'14-Cambios realizados acumulados',cambios_acumulados)

            cambios_acumulados_portero= datos_acumulados_object.cambios_portero_acumulados + cambios_portero
            cambios_acumulados_defensa= datos_acumulados_object.cambios_defensa_acumulados + cambios_defensa
            cambios_acumulados_centrocampista= datos_acumulados_object.cambios_centrocampista_acumulados + cambios_centrocampista
            cambios_acumulados_delantero= datos_acumulados_object.cambios_delantero_acumulados + cambios_delantero
            setattr(output_object,'16-Cambios realizados portero acumulados',cambios_acumulados_portero)
            setattr(output_object,'18-Cambios realizados defensa acumulados',cambios_acumulados_defensa)
            setattr(output_object,'20-Cambios realizados centrocampista acumulados',cambios_acumulados_centrocampista)
            setattr(output_object,'22-Cambios realizados delantero acumulados',cambios_acumulados_delantero)
            
            #Datos dicotomicos cambios
            setattr(output_object,'27-Cambio jugador lesion partido',dato_dictomico_cambio_lesion)
            setattr(output_object,'28-Cambio jugador amarilla partido',dato_dictomico_cambio_amarilla)
            setattr(output_object,'29-Cambio jugador roja partido',dato_dictomico_cambio_roja)


            #TODO probablemente esto sean datos prepartido así que me va a tocar cambiarlo
            posicion_jornada_anterior = ''
            puntos_jornada_anterior = ''

            posicion_rival_jornada_anterior = ''
            puntos_rival_jornada_anterior = ''

            if(jornada >1):
                equipo_jornada_anterion = object
                equipo_rival_jornada_anterior = object
                for clasificacion_equipo_jornada_anterior in clasificacion_jornada_anterior:
                    if (clasificacion_equipo_jornada_anterior.nombre == rival):
                        equipo_rival_jornada_anterior = clasificacion_equipo_jornada_anterior
                        continue
                    if (clasificacion_equipo_jornada_anterior.nombre == clasificacion_equipo.nombre):
                        equipo_jornada_anterion = clasificacion_equipo_jornada_anterior
                        continue   
                
                posicion_jornada_anterior = equipo_jornada_anterion.posicion
                puntos_jornada_anterior = equipo_jornada_anterion.puntos

                posicion_rival_jornada_anterior = equipo_rival_jornada_anterior.posicion
                puntos_rival_jornada_anterior = equipo_rival_jornada_anterior.puntos
                
            #Datos equipo prepartido
            setattr(output_object,'41-Posicion Local prepartido',posicion_jornada_anterior)
            setattr(output_object,'42-Puntos local prepartido',puntos_jornada_anterior)

            #Datos equipo rival prepartido
            setattr(output_object,'43-Rival',teams_dict[rival])
            setattr(output_object,'44-Posicion rival',posicion_rival_jornada_anterior)
            setattr(output_object,'45-Puntos rival',puntos_rival_jornada_anterior)

            #Datos jugadores
            edad_media = 0
            peso_medio = 0
            altura_media = 0

            #TODO lo mismo debería tener en cuenta si alguno de los datos es - para no contarlo en la media en vez de usar len()
            for jugador_plantilla in lista_plantilla:
                if(jugador_plantilla.edad != '' and jugador_plantilla.edad != '-'):
                    edad_media = edad_media + int(jugador_plantilla.edad)
                if(jugador_plantilla.peso != '' and jugador_plantilla.peso != '-'):
                    peso_medio = peso_medio + int(jugador_plantilla.peso)
                if(jugador_plantilla.altura != '' and jugador_plantilla.altura != '-'):
                    altura_media = altura_media + int(jugador_plantilla.altura)

            if (len(lista_plantilla)!=0):
                edad_media = edad_media / len(lista_plantilla)
                peso_medio = peso_medio / len(lista_plantilla)
                altura_media = altura_media / len(lista_plantilla)

            setattr(output_object,'46-Edad media',int(edad_media))
            setattr(output_object,'47-Peso medio',int(peso_medio))
            setattr(output_object,'48-Altura media',int(altura_media))

            #Calculo cambios 
            tiempo_suma_cambio = 0
            cambios_sorted = sorted(lista_cambios, key=lambda x: x.minuto)
            for idx in range(0,3):
                if idx+1 <= len(cambios_sorted):
                    minuto = cambios_sorted[idx].minuto
                    tiempo_suma_cambio = tiempo_suma_cambio + int(minuto)
                    posicion_sale = cambios_sorted[idx].posicion_sale
                    posicion_entra = cambios_sorted[idx].posicion_entra
                else:
                    minuto = 0
                    posicion_sale = ''
                    posicion_entra = ''

                numero_cambio = idx + 1
                setattr(output_object,'52-Minuto cambio ' + str(numero_cambio), minuto)
                #TODO Igual debería de quitar el guion si no hay cambio
                setattr(output_object,'53-Posicion cambio (Sale/Entra) ' + str(numero_cambio),posicion_sale + ' - ' + posicion_entra)

            media_minuto_cambio = 0
            if (len(lista_cambios)!=0):
                media_minuto_cambio = tiempo_suma_cambio / len(lista_cambios)
            setattr(output_object, '23-Media minuto cambio partido',int(media_minuto_cambio))
            
            tiempo_cambio_acumulado = datos_acumulados_object.suma_tiempo_cambio_acumulado + tiempo_suma_cambio
            
            media_minuto_cambio_acumulado = 0
            if (cambios_acumulados != 0):
                media_minuto_cambio_acumulado = tiempo_cambio_acumulado / cambios_acumulados
            setattr(output_object, '24-Media minuto cambio acumulado',int(media_minuto_cambio_acumulado))

            dato_lesiones_partido = 0
            dato_amarilla_partido = 0
            dato_roja_partido = 0
            #TODO lo mismo tengo que poner que solo sean jugadores titulares
            for jugador in alineacion_object:
                if(str(jugador.lesion)!= '0'):
                    dato_lesiones_partido = dato_lesiones_partido + 1
                if(jugador.roja != '0'):
                    dato_roja_partido = dato_roja_partido + 1
                if(jugador.amarilla != '0'):
                    dato_amarilla_partido = dato_amarilla_partido + int(jugador.amarilla)
                
            setattr(output_object, '35-Lesiones en partido',dato_lesiones_partido)
            setattr(output_object, '37-Amarillas partido',dato_amarilla_partido)
            setattr(output_object, '39-Rojas partido',dato_roja_partido)
 
            dato_lesiones_acumulados_temporada = datos_acumulados_object.lesion_acumulados + dato_lesiones_partido
            dato_amarilla_acumulados_temporada = datos_acumulados_object.amarilla_acumulados + dato_amarilla_partido
            dato_roja_acumulados_temporada = datos_acumulados_object.roja_acumulados + dato_roja_partido

            setattr(output_object, '36-Lesiones acumuladas',dato_lesiones_acumulados_temporada)
            setattr(output_object, '38-Amarillas acumuladas',dato_amarilla_acumulados_temporada)
            setattr(output_object, '40-Rojas acumuladas',dato_roja_acumulados_temporada)

            #Calculo de maximo goleador y maximo asistente
            maximo_goleador_cambio = 0
            maximo_asistente_cambio = 0

            #TODO usar sort para buscar el maximo goleador y el maximo asistente
            if(int(goles_partido)>0):
                maximo_goleador = max(alineacion_object, key=lambda jugador: jugador.gol)

                if(maximo_goleador.cambio != ''):
                    maximo_goleador_cambio = 1

                maximo_asistente = max(alineacion_object, key=lambda jugador: jugador.asistencia)

                if(maximo_asistente.cambio != ''):
                    maximo_asistente_cambio = 1

            setattr(output_object, '25-Cambio jugador más asistencias partido',maximo_asistente_cambio)
            setattr(output_object, '26-Cambio jugador más goles partido',maximo_goleador_cambio)

            numero_titulares_cambiados = 0

            dato_dictomico_goleador_jornada_anterior = 0
            dato_dictomico_lesion_jornada_anterior = 0
            dato_dictomico_amarilla_jornada_anterior = 0 
            dato_dictomico_roja_jornada_anterior = 0
            
            #TODO Algo no funciona aqui
            if(jornada > 1):
                titulares_jornada_anterior = [j for j in alineacion_jornada_anterior[clasificacion_equipo.nombre] if (j.estado == "Titular")]
                titulares_jornada_actual = [j for j in alineacion_object if (j.estado == "Titular")]
                
                for jugador in titulares_jornada_anterior:
                    for jugador2 in titulares_jornada_actual:
                        if(jugador.jugador == jugador2.jugador):
                            titulares_jornada_anterior.remove(jugador)
                            titulares_jornada_actual.remove(jugador2)
                            break
                
                goleador_jornada_anterior = datos_acumulados_object.goleador_jornada_anterior
                numero_titulares_cambiados = len(titulares_jornada_actual)
                for jugador in titulares_jornada_actual:
                    if(jugador.jugador == goleador_jornada_anterior):
                        dato_dictomico_goleador_jornada_anterior = 1
                    if(str(jugador.lesion)!= '0'):
                        dato_dictomico_lesion_jornada_anterior = 1
                    if(jugador.amarilla != '0'):
                        dato_dictomico_amarilla_jornada_anterior = 1
                    if(jugador.roja != '0'):
                        dato_dictomico_roja_jornada_anterior = 1
            
            setattr(output_object,'30-Titulares cambiados respecto jornada anterior',numero_titulares_cambiados)

            setattr(output_object,'31-Cambio goleador jornada anterior',dato_dictomico_goleador_jornada_anterior)
            setattr(output_object,'32-Cambio amarilla jornada anterior',dato_dictomico_amarilla_jornada_anterior)
            setattr(output_object,'33-Cambio roja jornada anterior',dato_dictomico_roja_jornada_anterior)
            setattr(output_object,'34-Cambio lesion jornada anterior',dato_dictomico_lesion_jornada_anterior)

            #Jornada intermedia
            jornada_intermedia = 0

            if (jornada > 1):
                todos_los_partidos = dc.getAllMatchesByTeam(clasificacion_equipo.nombre,season,s)
                todos_los_partidos_sorted = sorted(todos_los_partidos, key=lambda x: x.fecha)
                fecha_partido = datetime.strptime(partido.fecha,'%d %b %y')
                for idx,partido in enumerate(todos_los_partidos_sorted):
                    if(partido.fecha == fecha_partido):
                        if(todos_los_partidos_sorted[idx-1].liga == league):
                            jornada_intermedia = 0
                            break
                        else:
                            jornada_intermedia = 1
                            break
            
            setattr(output_object,'49-Jornada intermedia',jornada_intermedia)


            #find_partido
            #para cada equipo buscar que partido juega en esa jornada en la lista de partidos 
            #una vez tengo equipo local y visitante puedo buscar ka akineacior para esa jornada

            #Actualiza los datos acumulados para la proxima jornada 
            datos_acumulados_object.goles_acumulados = clasificacion_equipo.gfavor
            datos_acumulados_object.cambios_acumulados = cambios_acumulados
            datos_acumulados_object.cambios_portero_acumulados = cambios_acumulados_portero
            datos_acumulados_object.cambios_defensa_acumulados = cambios_acumulados_defensa
            datos_acumulados_object.cambios_centrocampista_acumulados = cambios_acumulados_centrocampista
            datos_acumulados_object.cambios_delantero_acumulados = cambios_acumulados_delantero
            datos_acumulados_object.suma_tiempo_cambio_acumulado = tiempo_cambio_acumulado
            datos_acumulados_object.lesion_acumulados = dato_lesiones_acumulados_temporada
            datos_acumulados_object.amarilla_acumulados = dato_amarilla_acumulados_temporada
            datos_acumulados_object.roja_acumulados = dato_roja_acumulados_temporada
            datos_acumulados_object.goleador_jornada_anterior = maximo_goleador.jugador
            
            alineacion_jornada_anterior[clasificacion_equipo.nombre] = alineacion_object
            
            #CSV writing
            
            
            base_filename = league + '_' + season
            fileName = path.join(ruta, base_filename + SUFFIX)

            if(primera_ejecucion==1):
                primera_ejecucion=0
                csv_tools.writeHeader(output_object,fileName)
            
            csv_tools.appendLineToExistingFile(output_object,fileName)
        
        clasificacion_jornada_anterior = clasificacion

    return data




        
