
import pandas as pd
fecha='04 May 24'


#funciones
def evaluar_resultado(row):
    if row['resultado_local'] > row['resultado_visitante']:
        return '1'
    elif row['resultado_local'] == row['resultado_visitante']:
        return 'X'
    else:
        return '2'
def calculos(numerador,denominador):
    porcentaje=((numerador)/(denominador))*100
    porcentaje=round(porcentaje,2)
    return porcentaje
                    
def calculosSin100(numerador,denominador):
    porcentaje=((numerador)/(denominador))
    porcentaje=round(porcentaje,2)
    return porcentaje


#cargamos csv
partidos = pd.read_csv('csv/partidos.csv')
jugadores = pd.read_csv('csv/jugadores.csv')
datos_partidos_jugados = pd.read_csv('csv/datosPartidosJugados.csv')
datos_jugadores_partidos = pd.read_csv('csv/datosJugadoresPartidos.csv')


#filtramos partidos en la fecha que queremos
partidos_fecha = partidos.loc[(partidos['fecha'] == fecha)  ]
partidos_fecha = partidos_fecha.loc[(partidos['id_equipo_local'] == 5)  ]




#acumuladores------------------------------------------
#local ganador-
contador_local_ganados=[0,0,0,0]
porcentaje_local_ganados=[0,0,0,0,0]

contador_local_empatados=[0,0,0,0]
porcentaje_local_empatados=[0,0,0,0,0]

contador_local_perdidos=[0,0,0,0]
porcentaje_local_perdidos=[0,0,0,0,0]




#visitante ganador-
contador_visitante_ganados=[0,0,0,0]
porcentaje_visitante_ganados=[0,0,0,0,0]

contador_visitante_empatados=[0,0,0,0]
porcentaje_visitante_empatados=[0,0,0,0,0]

contador_visitante_perdidos=[0,0,0,0]
porcentaje_visitante_perdidos=[0,0,0,0,0]



#local goles-
contador_local_mas15=[0,0,0,0]
porcentaje_local_mas15=[0,0,0,0,0]

contador_local_mas25=[0,0,0,0]
porcentaje_local_mas25=[0,0,0,0,0]

contador_local_mas35=[0,0,0,0]
porcentaje_local_mas35=[0,0,0,0,0]

contador_local_mas45=[0,0,0,0]
porcentaje_local_mas45=[0,0,0,0,0]



#visitante goles-
contador_visitante_mas15=[0,0,0,0]
porcentaje_visitante_mas15=[0,0,0,0,0]

contador_visitante_mas25=[0,0,0,0]
porcentaje_visitante_mas25=[0,0,0,0,0]

contador_visitante_mas35=[0,0,0,0]
porcentaje_visitante_mas35=[0,0,0,0,0]

contador_visitante_mas45=[0,0,0,0]
porcentaje_visitante_mas45=[0,0,0,0,0]



#local goles marcados-
contador_local_mas05_marcados=[0,0,0,0]
porcentaje_local_mas05_marcados=[0,0,0,0,0]

contador_local_mas15_marcados=[0,0,0,0]
porcentaje_local_mas15_marcados=[0,0,0,0,0]

contador_local_mas25_marcados=[0,0,0,0]
porcentaje_local_mas25_marcados=[0,0,0,0,0]



#local goles encajados-
contador_local_mas05_encajados=[0,0,0,0]
porcentaje_local_mas05_encajados=[0,0,0,0,0]

contador_local_mas15_encajados=[0,0,0,0]
porcentaje_local_mas15_encajados=[0,0,0,0,0]

contador_local_mas25_encajados=[0,0,0,0]
porcentaje_local_mas25_encajados=[0,0,0,0,0]



#visitante goles marcados-
contador_visitante_mas05_marcados=[0,0,0,0]
porcentaje_visitante_mas05_marcados=[0,0,0,0,0]

contador_visitante_mas15_marcados=[0,0,0,0]
porcentaje_visitante_mas15_marcados=[0,0,0,0,0]

contador_visitante_mas25_marcados=[0,0,0,0]
porcentaje_visitante_mas25_marcados=[0,0,0,0,0]



#visitante goles encajados-
contador_visitante_mas05_encajados=[0,0,0,0]
porcentaje_visitante_mas05_encajados=[0,0,0,0,0]

contador_visitante_mas15_encajados=[0,0,0,0]
porcentaje_visitante_mas15_encajados=[0,0,0,0,0]

contador_visitante_mas25_encajados=[0,0,0,0]
porcentaje_visitante_mas25_encajados=[0,0,0,0,0]


#local y visitante acumulador goles totales-
contador_local_goles_totales=[0,0,0,0]
proporcion_local_goles_totales=[0,0,0,0,0]

contador_visitante_goles_totales=[0,0,0,0]
proporcion_visitante_goles_totales=[0,0,0,0,0]




#local acumulador goles marcados y encajados-
contador_local_goles_marcados=[0,0,0,0]
proporcion_local_goles_marcados=[0,0,0,0,0]

contador_local_goles_encajados=[0,0,0,0]
proporcion_local_goles_encajados=[0,0,0,0,0]



#visitante acumulador goles marcados y encajados-
contador_visitante_goles_marcados=[0,0,0,0]
proporcion_visitante_goles_marcados=[0,0,0,0,0]

contador_visitante_goles_encajados=[0,0,0,0]
proporcion_visitante_goles_encajados=[0,0,0,0,0]


#local acumulador puntos-
contador_local_puntos=[0,0,0,0]
proporcion_local_puntos=[0,0,0,0,0]


#visitante acumulador puntos-
contador_visitante_puntos=[0,0,0,0]
proporcion_visitante_puntos=[0,0,0,0,0]


#local y visitante partidos-
contador_local_partidos=[0,0]
contador_visitante_partidos=[0,0]


#local y visitante amarillas-
contador_local_amarillas=[0,0,0,0]
proporcion_local_amarillas=[0,0,0,0,0]

contador_visitante_amarillas=[0,0,0,0]
proporcion_visitante_amarillas=[0,0,0,0,0]


#local y visitante rojas-
contador_local_rojas=[0,0,0,0]
proporcion_local_rojas=[0,0,0,0,0]

contador_visitante_rojas=[0,0,0,0]
proporcion_visitante_rojas=[0,0,0,0,0]


#local y visitante corners a favor
contador_local_corners_afavor=[0,0,0,0]
proporcion_local_corners_afavor=[0,0,0,0,0]

contador_visitante_corners_afavor=[0,0,0,0]
proporcion_visitante_corners_afavor=[0,0,0,0,0]


#local y visitante corners en contra
contador_local_corners_encontra=[0,0,0,0]
proporcion_local_corners_encontra=[0,0,0,0,0]

contador_visitante_corners_encontra=[0,0,0,0]
proporcion_visitante_corners_encontra=[0,0,0,0,0]


#local y visitante cambios realizados-
contador_local_cambios=[0,0,0,0]
proporcion_local_cambios=[0,0,0,0,0]

contador_visitante_cambios=[0,0,0,0]
proporcion_visitante_cambios=[0,0,0,0,0]


#local y visitante posesion-
contador_local_posesion=[0,0,0,0]
proporcion_local_posesion=[0,0,0,0,0]

contador_visitante_posesion=[0,0,0,0]
proporcion_visitante_posesion=[0,0,0,0,0]


#local y visitante total tiros-
contador_local_total_tiros=[0,0,0,0]
proporcion_local_total_tiros=[0,0,0,0,0]

contador_visitante_total_tiros=[0,0,0,0]
proporcion_visitante_total_tiros=[0,0,0,0,0]


#local y visitante contador cambios lesionados
contador_local_cambios_lesionados=[0,0,0,0]
proporcion_local_cambios_lesionados=[0,0,0,0,0]
contador_visitante_cambios_lesionados=[0,0,0,0]
proporcion_visitante_cambios_lesionados=[0,0,0,0,0]

#local y visitante contador cambios amarillas
contador_local_cambios_amarillas=[0,0,0,0]
proporcion_local_cambios_amarillas=[0,0,0,0,0]
contador_visitante_cambios_amarillas=[0,0,0,0]
proporcion_visitante_cambios_amarillas=[0,0,0,0,0]

#local y visitante contador cambios goleadores
contador_local_cambios_goleadores=[0,0,0,0]
proporcion_local_cambios_goleadores=[0,0,0,0,0]
contador_visitante_cambios_goleadores=[0,0,0,0]
proporcion_visitante_cambios_goleadores=[0,0,0,0,0]

#local y visitante contador cambios asistentes
contador_local_cambios_asistentes=[0,0,0,0]
proporcion_local_cambios_asistentes=[0,0,0,0,0]
contador_visitante_cambios_asistentes=[0,0,0,0]
proporcion_visitante_cambios_asistentes=[0,0,0,0,0]

#media minutos local y visitante cambios
media_local_cambio_minutos=[0,0,0,0]
media_visitante_cambio_minutos=[0,0,0,0]

#media local y visitante cambios respecto ultima alineacion
media_local_cambios_ultima_alineacion=[0,0,0,0]
media_visitante_cambios_ultima_alineacion=[0,0,0,0]

#local y visitante contador cambios delanteros a defensas-
contador_local_cambios_delanteros_a_defensas=[0,0,0,0]
proporcion_local_cambios_delanteros_a_defensas=[0,0,0,0,0]
contador_visitante_cambios_delanteros_a_defensas=[0,0,0,0]
proporcion_visitante_cambios_delanteros_a_defensas=[0,0,0,0,0]

#local y visitante contador cambios delanteros a centrocampistas-
contador_local_cambios_delanteros_a_centrocampistas=[0,0,0,0]
proporcion_local_cambios_delanteros_a_centrocampistas=[0,0,0,0,0]
contador_visitante_cambios_delanteros_a_centrocampistas=[0,0,0,0]
proporcion_visitante_cambios_delanteros_a_centrocampistas=[0,0,0,0,0]

#local y visitante contador cambios defensas a delanteros-
contador_local_cambios_defensas_a_delanteros=[0,0,0,0]
proporcion_local_cambios_defensas_a_delanteros=[0,0,0,0,0]
contador_visitante_cambios_defensas_a_delanteros=[0,0,0,0]
proporcion_visitante_cambios_defensas_a_delanteros=[0,0,0,0,0]

#local y visitante contador cambios defensas a centrocampistas-
contador_local_cambios_defensas_a_centrocampistas=[0,0,0,0]
proporcion_local_cambios_defensas_a_centrocampistas=[0,0,0,0,0]
contador_visitante_cambios_defensas_a_centrocampistas=[0,0,0,0]
proporcion_visitante_cambios_defensas_a_centrocampistas=[0,0,0,0,0]

#local y visitante contador cambios centrocampistas a delanteros-
contador_local_cambios_centrocampistas_a_delanteros=[0,0,0,0]
proporcion_local_cambios_centrocampistas_a_delanteros=[0,0,0,0,0]
contador_visitante_cambios_centrocampistas_a_delanteros=[0,0,0,0]
proporcion_visitante_cambios_centrocampistas_a_delanteros=[0,0,0,0,0]

#local y visitante contador cambios centrocampistas a defensas-
contador_local_cambios_centrocampistas_a_defensas=[0,0,0,0]
proporcion_local_cambios_centrocampistas_a_defensas=[0,0,0,0,0]
contador_visitante_cambios_centrocampistas_a_defensas=[0,0,0,0]
proporcion_visitante_cambios_centrocampistas_a_defensas=[0,0,0,0,0]

#local y visitante contador cambios antes del descanso-
contador_local_cambios_antes_descanso=[0,0,0,0]
proporcion_local_cambios_antes_descanso=[0,0,0,0,0]
contador_visitante_cambios_antes_descanso=[0,0,0,0]
proporcion_visitante_cambios_antes_descanso=[0,0,0,0,0]

#local y visitante contador cambios 45-60-
contador_local_cambios_45_60=[0,0,0,0]
proporcion_local_cambios_45_60=[0,0,0,0,0]
contador_visitante_cambios_45_60=[0,0,0,0]
proporcion_visitante_cambios_45_60=[0,0,0,0,0]

#local y visitante contador cambios 61-75-
contador_local_cambios_61_75=[0,0,0,0]
proporcion_local_cambios_61_75=[0,0,0,0,0]
contador_visitante_cambios_61_75=[0,0,0,0]
proporcion_visitante_cambios_61_75=[0,0,0,0,0]

#local y visitante contador cambios 76-final-
contador_local_cambios_76_final=[0,0,0,0]
proporcion_local_cambios_76_final=[0,0,0,0,0]
contador_visitante_cambios_76_final=[0,0,0,0]
proporcion_visitante_cambios_76_final=[0,0,0,0,0]

#local y visitante contador alineacion defensa
contador_local_cambios_alineacion_defensa=[0,0,0,0]
proporcion_local_cambios_alineacion_defensa=[0,0,0,0,0]
contador_visitante_cambios_alineacion_defensa=[0,0,0,0]
proporcion_visitante_cambios_alineacion_defensa=[0,0,0,0,0]

#local y visitante contador alineacion centrocampista
contador_local_cambios_alineacion_centrocampista=[0,0,0,0]
proporcion_local_cambios_alineacion_centrocampista=[0,0,0,0,0]
contador_visitante_cambios_alineacion_centrocampista=[0,0,0,0]
proporcion_visitante_cambios_alineacion_centrocampista=[0,0,0,0,0]

#local y visitante contador alineacion delantero
contador_local_cambios_alineacion_delantero=[0,0,0,0]
proporcion_local_cambios_alineacion_delantero=[0,0,0,0,0]
contador_visitante_cambios_alineacion_delantero=[0,0,0,0]
proporcion_visitante_cambios_alineacion_delantero=[0,0,0,0,0]

#dataframe para meter los datos
id_indicadores_equipo_prepartido=0
dataframe_indicadores_equipos_prepartido=pd.DataFrame(columns=[
    'id_indicadores_equipo_prepartido',
'id_partido',
'porcentaje local ganados en sitio',
'porcentaje local ganados en general',
'porcentaje local empatados en sitio',
'porcentaje local empatados en general',
'porcentaje local perdidos en sitio',
'porcentaje local perdidos en general',
'porcentaje visitante ganados en sitio',
'porcentaje visitante ganados en general',
'porcentaje visitante empatados en sitio',
'porcentaje visitante empatados en general',
'porcentaje visitante perdidos en sitio',
'porcentaje visitante perdidos en general',
'proporcion local puntos en sitio',
'proporcion local puntos en general',
'proporcion visitante puntos en sitio',
'proporcion visitante puntos en general',
'porcentaje local mas 1,5 en sitio',
'porcentaje local mas 1,5 en general',
'porcentaje visitante mas 1,5 en sitio',
'porcentaje visitante mas 1,5 en general',
'porcentaje local mas 2,5 en sitio',
'porcentaje local mas 2,5 en general',
'porcentaje visitante mas 2,5 en sitio',
'porcentaje visitante mas 2,5 en general',
'porcentaje local mas 3,5 en sitio',
'porcentaje local mas 3,5 en general',
'porcentaje visitante mas 3,5 en sitio',
'porcentaje visitante mas 3,5 en general',
'porcentaje local mas 4,5 en sitio',
'porcentaje local mas 4,5 en general',
'porcentaje visitante mas 4,5 en sitio',
'porcentaje visitante mas 4,5 en general',
'proporcion local goles totales en sitio',
'proporcion local goles totales en general',
'proporcion local goles marcados en sitio',
'proporcion local goles marcados en general',
'proporcion local goles encajados en sitio',
'proporcion local goles encajados en general',
'proporcion visitante goles totales en sitio',
'proporcion visitante goles totales en general',
'proporcion visitante goles marcados en sitio',
'proporcion visitante goles marcados en general',
'proporcion visitante goles encajados en sitio',
'proporcion visitante goles encajados en general',
'porcentaje local mas 0,5 marcados en sitio',
'porcentaje local mas 0,5 marcados en general',
'porcentaje local mas 1,5 marcados en sitio',
'porcentaje local mas 1,5 marcados en general',
'porcentaje local mas 2,5 marcados en sitio',
'porcentaje local mas 2,5 marcados en general',
'porcentaje local mas 0,5 encajados en sitio',
'porcentaje local mas 0,5 encajados en general',
'porcentaje local mas 1,5 encajados en sitio',
'porcentaje local mas 1,5 encajados en general',
'porcentaje local mas 2,5 encajados en sitio',
'porcentaje local mas 2,5 encajados en general',
'porcentaje visitante mas 0,5 marcados en sitio',
'porcentaje visitante mas 0,5 marcados en general',
'porcentaje visitante mas 1,5 marcados en sitio',
'porcentaje visitante mas 1,5 marcados en general',
'porcentaje visitante mas 2,5 marcados en sitio',
'porcentaje visitante mas 2,5 marcados en general',
'porcentaje visitante mas 0,5 encajados en sitio',
'porcentaje visitante mas 0,5 encajados en general',
'porcentaje visitante mas 1,5 encajados en sitio',
'porcentaje visitante mas 1,5 encajados en general',
'porcentaje visitante mas 2,5 encajados en sitio',
'porcentaje visitante mas 2,5 encajados en general',
'proporcion local amarillas en sitio',
'proporcion local amarillas en general',
'proporcion visitante amarillas en sitio',
'proporcion visitante amarillas en general',
'proporcion local rojas en sitio',
'proporcion local rojas en general',
'proporcion visitante rojas en sitio',
'proporcion visitante rojas en general',
'proporcion local cambios en sitio',
'proporcion local cambios en general',
'proporcion visitante cambios en sitio',
'proporcion visitante cambios en general',
'proporcion local posesion en sitio',
'proporcion local posesion en general',
'proporcion visitante posesion en sitio',
'proporcion visitante posesion en general',
'proporcion local total tiros en sitio',
'proporcion local total tiros en general',
'proporcion visitante total tiros en sitio',
'proporcion visitante total tiros en general',
'proporcion local corners a favor en sitio',
'proporcion local corners a favor en general',
'proporcion visitante corners a favor en sitio',
'proporcion visitante corners a favor en general',
'proporcion local corners en contra en sitio',
'proporcion local corners en contra en general',
'proporcion visitante corners en contra en sitio',
'proporcion visitante corners en contra en general',
'proporcion local cambios lesionados sitio',
'proporcion local cambios lesionados en general',
'proporcion visitante cambios lesionados en sitio',
'proporcion visitante cambios lesionados en general',
'proporcion local cambios amarillas sitio',
'proporcion local cambios amarillas en general',
'proporcion visitante cambios amarillas en sitio',
'proporcion visitante cambios amarillas en general',
'proporcion local cambios goleadores sitio',
'proporcion local cambios goleadores en general',
'proporcion visitante cambios goleadores en sitio',
'proporcion visitante cambios goleadores en general',
'proporcion local cambios asistentes sitio',
'proporcion local cambios asistentes en general',
'proporcion visitante cambios asistentes en sitio',
'proporcion visitante cambios asistentes en general',
'media local cambios minutos sitio',
'media local cambios minutos en general',
'media visitante cambios minutos sitio',
'media visitante cambios minutos en general',
'proporcion local cambios delanteros a centrocampistas sitio',
'proporcion local cambios delanteros a centrocampistas en general',
'proporcion visitante cambios delanteros a centrocampistas en sitio',
'proporcion visitante cambios delanteros a centrocampistas en general',
'proporcion local cambios delanteros a defensas sitio',
'proporcion local cambios delanteros a defensas en general',
'proporcion visitante cambios delanteros a defensas en sitio',
'proporcion visitante cambios delanteros a defensas en general',
'proporcion local cambios centrocampistas a delanteros sitio',
'proporcion local cambios centrocampistas a delanteros en general',
'proporcion visitante cambios centrocampistas a delanteros en sitio',
'proporcion visitante cambios centrocampistas a delanteros en general',
'proporcion local cambios centrocampistas a defensas sitio',
'proporcion local cambios centrocampistas a defensas en general',
'proporcion visitante cambios centrocampistas a defensas en sitio',
'proporcion visitante cambios centrocampistas a defensas en general',
'proporcion local cambios defensas a delanteros sitio',
'proporcion local cambios defensas a delanteros en general',
'proporcion visitante cambios defensas a delanteros en sitio',
'proporcion visitante cambios defensas a delanteros en general',
'proporcion local cambios defensas a centrocampistas sitio',
'proporcion local cambios defensas a centrocampistas en general',
'proporcion visitante cambios defensas a centrocampistas en sitio',
'proporcion visitante cambios defensas a centrocampistas en general',
'proporcion local cambios antes descanso sitio',
'proporcion local cambios antes descanso en general',
'proporcion visitante cambios antes descanso en sitio',
'proporcion visitante cambios antes descanso en general',
'proporcion local cambios 45 a 60 sitio',
'proporcion local cambios 45 a 60 en general',
'proporcion visitante cambios 45 a 60 en sitio',
'proporcion visitante cambios 45 a 60 en general',
'proporcion local cambios 61 a 75 sitio',
'proporcion local cambios 61 a 75 en general',
'proporcion visitante cambios 61 a 75 en sitio',
'proporcion visitante cambios 61 a 75 en general',
'proporcion local cambios 76 a final sitio',
'proporcion local cambios 76 a final en general',
'proporcion visitante cambios 76 a final en sitio',
'proporcion visitante cambios 76 a final en general',
'proporcion local cambios alineacion defensa sitio',
'proporcion local cambios alineacion defensa en general',
'proporcion visitante cambios alineacion defensa en sitio',
'proporcion visitante cambios alineacion defensa en general',
'proporcion local cambios alineacion centrocampista sitio',
'proporcion local cambios alineacion centrocampista en general',
'proporcion visitante cambios alineacion centrocampista en sitio',
'proporcion visitante cambios alineacion centrocampista en general',
'proporcion local cambios alineacion delantero sitio',
'proporcion local cambios alineacion delantero en general',
'proporcion visitante cambios alineacion delantero en sitio',
'proporcion visitante cambios alineacion delantero en general'


])







#recorremos los partidos de hoy
for index, row in partidos_fecha.iterrows():
        id_equipo_local = row['id_equipo_local']
        id_equipo_visitante = row['id_equipo_visitante']
        id_partido = row['id_partido']







 

        #partidos del local como local
        partidos_local=partidos.loc[(partidos['id_equipo_local'] == id_equipo_local)  ]
        id_partidos_local = partidos_local['id_partido']
        
        datos_partidos_jugados_local_como_local = datos_partidos_jugados[datos_partidos_jugados['id_partido'].isin(id_partidos_local)]

        datos_partidos_jugados_local_como_local = pd.merge(datos_partidos_jugados_local_como_local, partidos_local[['id_partido', 'jornada']], on='id_partido', how='left')

        contador_local_partidos[0]=len(datos_partidos_jugados_local_como_local)








        #obtener datos de los jugadores en los partidos del local como local
        datos_jugadores_partidos_filtrados_local_como_local=datos_jugadores_partidos.loc[datos_jugadores_partidos['id_partido'].isin(id_partidos_local)  ]
        datos_jugadores_partidos_filtrados_local_como_local.to_csv('csv/localLocal.csv', index=False) 











        #partidos visitante como visitante
        partidos_visitante=partidos.loc[(partidos['id_equipo_visitante'] == id_equipo_visitante)  ]
        id_partidos_visitante = partidos_visitante['id_partido']

        datos_partidos_jugados_visitante_como_visitante = datos_partidos_jugados[datos_partidos_jugados['id_partido'].isin(id_partidos_visitante)]

        datos_partidos_jugados_visitante_como_visitante = pd.merge(datos_partidos_jugados_visitante_como_visitante, partidos_visitante[['id_partido', 'jornada']], on='id_partido', how='left')   

        contador_visitante_partidos[0]=len(datos_partidos_jugados_visitante_como_visitante)







        #obtener datos de los jugadores en los partidos del visitante como visitante
        datos_jugadores_partidos_filtrados_visitante_como_visitante=datos_jugadores_partidos.loc[datos_jugadores_partidos['id_partido'].isin(id_partidos_visitante)  ]
        datos_jugadores_partidos_filtrados_visitante_como_visitante.to_csv('csv/visitanteVisitante.csv', index=False)








        #partidos local como visitante 
        partidos_local=partidos.loc[(partidos['id_equipo_visitante'] == id_equipo_local)  ]
        id_partidos_local = partidos_local['id_partido']
        
        datos_partidos_jugados_local_como_visitante = datos_partidos_jugados[datos_partidos_jugados['id_partido'].isin(id_partidos_local)]

        datos_partidos_jugados_local_como_visitante = pd.merge(datos_partidos_jugados_local_como_visitante, partidos_local[['id_partido', 'jornada']], on='id_partido', how='left')     
        







        #obtener datos de los jugadores en los partidos del local como visitante
        datos_jugadores_partidos_filtrados_local_como_visitante=datos_jugadores_partidos.loc[datos_jugadores_partidos['id_partido'].isin(id_partidos_local)  ]
        datos_jugadores_partidos_filtrados_local_como_visitante.to_csv('csv/localVisitante.csv', index=False)







        #partidos visitante como local
        partidos_visitante=partidos.loc[(partidos['id_equipo_local'] == id_equipo_visitante)  ]
        id_partidos_visitante = partidos_visitante['id_partido']

        datos_partidos_jugados_visitante_como_local = datos_partidos_jugados[datos_partidos_jugados['id_partido'].isin(id_partidos_visitante)]

        datos_partidos_jugados_visitante_como_local = pd.merge(datos_partidos_jugados_visitante_como_local, partidos_visitante[['id_partido', 'jornada']], on='id_partido', how='left') 







        #obtener datos de los jugadores en los partidos del visitante como local
        datos_jugadores_partidos_filtrados_visitante_como_local=datos_jugadores_partidos.loc[datos_jugadores_partidos['id_partido'].isin(id_partidos_visitante)  ]
        datos_jugadores_partidos_filtrados_visitante_como_local.to_csv('csv/visitanteLocal.csv', index=False)





        #partidos totales del local
        datos_partidos_jugados_local_total = pd.concat([datos_partidos_jugados_local_como_local, datos_partidos_jugados_local_como_visitante])

        datos_partidos_jugados_local_total = datos_partidos_jugados_local_total.sort_values(by='jornada')

        contador_local_partidos[1]=len(datos_partidos_jugados_local_total)

        datos_partidos_jugados_local_total.to_csv('csv/localTotal.csv', index=False)






        #partidos totales del visitante
        datos_partidos_jugados_visitante_total = pd.concat([datos_partidos_jugados_visitante_como_local, datos_partidos_jugados_visitante_como_visitante])

        datos_partidos_jugados_visitante_total = datos_partidos_jugados_visitante_total.sort_values(by='jornada')

        contador_visitante_partidos[1]=len(datos_partidos_jugados_visitante_total)

        datos_partidos_jugados_visitante_total.to_csv('csv/visitanteTotal.csv', index=False)






    







        

        #añadir columnas ganador y goles
        datos_partidos_jugados_local_como_local['total_goles'] = datos_partidos_jugados_local_como_local['resultado_local'] + datos_partidos_jugados_local_como_local['resultado_visitante'] 

        datos_partidos_jugados_local_como_local['resultado_partido'] = datos_partidos_jugados_local_como_local.apply(evaluar_resultado, axis=1)

        datos_partidos_jugados_local_como_visitante['total_goles'] = datos_partidos_jugados_local_como_visitante['resultado_local'] + datos_partidos_jugados_local_como_visitante['resultado_visitante'] 

        datos_partidos_jugados_local_como_visitante['resultado_partido'] = datos_partidos_jugados_local_como_visitante.apply(evaluar_resultado, axis=1)    

        datos_partidos_jugados_local_total['total_goles'] = datos_partidos_jugados_local_total['resultado_local'] + datos_partidos_jugados_local_total['resultado_visitante'] 

        datos_partidos_jugados_local_total['resultado_partido'] = datos_partidos_jugados_local_total.apply(evaluar_resultado, axis=1)

        datos_partidos_jugados_visitante_como_local['total_goles'] = datos_partidos_jugados_visitante_como_local['resultado_local'] + datos_partidos_jugados_visitante_como_local['resultado_visitante'] 

        datos_partidos_jugados_visitante_como_local['resultado_partido'] = datos_partidos_jugados_visitante_como_local.apply(evaluar_resultado, axis=1)

        datos_partidos_jugados_visitante_como_visitante['total_goles'] = datos_partidos_jugados_visitante_como_visitante['resultado_local'] + datos_partidos_jugados_visitante_como_visitante['resultado_visitante'] 

        datos_partidos_jugados_visitante_como_visitante['resultado_partido'] = datos_partidos_jugados_visitante_como_visitante.apply(evaluar_resultado, axis=1)    

        datos_partidos_jugados_visitante_total['total_goles'] = datos_partidos_jugados_visitante_total['resultado_local'] + datos_partidos_jugados_visitante_total['resultado_visitante'] 

        datos_partidos_jugados_visitante_total['resultado_partido'] = datos_partidos_jugados_visitante_total.apply(evaluar_resultado, axis=1)








        #cuenta eventos---------------------------------------



        #goles local
        contador_local_mas15[0] = (datos_partidos_jugados_local_como_local['total_goles'] > 1).sum()
        porcentaje_local_mas15[0]=calculos(contador_local_mas15[0],contador_local_partidos[0])

        contador_local_mas15[1] = (datos_partidos_jugados_local_total['total_goles'] > 1).sum()
        porcentaje_local_mas15[1]=calculos(contador_local_mas15[1],contador_local_partidos[1])

        contador_local_mas25[0] = (datos_partidos_jugados_local_como_local['total_goles'] > 2).sum()
        porcentaje_local_mas25[0]=calculos(contador_local_mas25[0],contador_local_partidos[0])

        contador_local_mas25[1] = (datos_partidos_jugados_local_total['total_goles'] > 2).sum()
        porcentaje_local_mas25[1]=calculos(contador_local_mas25[1],contador_local_partidos[1])

        contador_local_mas35[0] = (datos_partidos_jugados_local_como_local['total_goles'] > 3).sum()
        porcentaje_local_mas35[0]=calculos(contador_local_mas35[0],contador_local_partidos[0])

        contador_local_mas35[1] = (datos_partidos_jugados_local_total['total_goles'] > 3).sum()
        porcentaje_local_mas35[1]=calculos(contador_local_mas35[1],contador_local_partidos[1])

        contador_local_mas45[0] = (datos_partidos_jugados_local_como_local['total_goles'] > 4).sum()
        porcentaje_local_mas45[0]=calculos(contador_local_mas45[0],contador_local_partidos[0])

        contador_local_mas45[1] = (datos_partidos_jugados_local_total['total_goles'] > 4).sum()
        porcentaje_local_mas45[1]=calculos(contador_local_mas45[1],contador_local_partidos[1])








        #goles visitante
        contador_visitante_mas15[0] = (datos_partidos_jugados_visitante_como_visitante['total_goles'] > 1).sum()
        porcentaje_visitante_mas15[0]=calculos(contador_visitante_mas15[0],contador_visitante_partidos[0])

        contador_visitante_mas15[1] = (datos_partidos_jugados_visitante_total['total_goles'] > 1).sum()
        porcentaje_visitante_mas15[1]=calculos(contador_visitante_mas15[1],contador_visitante_partidos[1])

        contador_visitante_mas25[0] = (datos_partidos_jugados_visitante_como_visitante['total_goles'] > 2).sum()
        porcentaje_visitante_mas25[0]=calculos(contador_visitante_mas25[0],contador_visitante_partidos[0])

        contador_visitante_mas25[1] = (datos_partidos_jugados_visitante_total['total_goles'] > 2).sum()
        porcentaje_visitante_mas25[1]=calculos(contador_visitante_mas25[1],contador_visitante_partidos[1])

        contador_visitante_mas35[0] = (datos_partidos_jugados_visitante_como_visitante['total_goles'] > 3).sum()
        porcentaje_visitante_mas35[0]=calculos(contador_visitante_mas35[0],contador_visitante_partidos[0])

        contador_visitante_mas35[1] = (datos_partidos_jugados_visitante_total['total_goles'] > 3).sum()
        porcentaje_visitante_mas35[1]=calculos(contador_visitante_mas35[1],contador_visitante_partidos[1])

        contador_visitante_mas45[0] = (datos_partidos_jugados_visitante_como_visitante['total_goles'] > 4).sum()
        porcentaje_visitante_mas45[0]=calculos(contador_visitante_mas45[0],contador_visitante_partidos[0])

        contador_visitante_mas45[1] = (datos_partidos_jugados_visitante_total['total_goles'] > 4).sum()
        porcentaje_visitante_mas45[1]=calculos(contador_visitante_mas45[1],contador_visitante_partidos[1])








        #local ganador
        contador_local_ganados[0]= (datos_partidos_jugados_local_como_local['resultado_partido'] =='1').sum()
        porcentaje_local_ganados[0]=calculos(contador_local_ganados[0],contador_local_partidos[0])

        contador_local_empatados[0]= (datos_partidos_jugados_local_como_local['resultado_partido'] =='X').sum()
        porcentaje_local_empatados[0]=calculos(contador_local_empatados[0],contador_local_partidos[0])

        contador_local_perdidos[0]= (datos_partidos_jugados_local_como_local['resultado_partido'] =='2').sum()
        porcentaje_local_perdidos[0]=calculos(contador_local_perdidos[0],contador_local_partidos[0])

        contador_local_ganados[1]= (datos_partidos_jugados_local_como_visitante['resultado_partido'] =='2').sum()+contador_local_ganados[0]
        porcentaje_local_ganados[1]=calculos(contador_local_ganados[1],contador_local_partidos[1])

        contador_local_empatados[1]= (datos_partidos_jugados_local_como_visitante['resultado_partido'] =='X').sum()+contador_local_empatados[0]
        porcentaje_local_empatados[1]=calculos(contador_local_empatados[1],contador_local_partidos[1])

        contador_local_perdidos[1]= (datos_partidos_jugados_local_como_visitante['resultado_partido'] =='1').sum()+contador_local_perdidos[0]
        porcentaje_local_perdidos[1]=calculos(contador_local_perdidos[1],contador_local_partidos[1])








        #acumulador puntos local
        contador_local_puntos[0]=contador_local_ganados[0]*3+contador_local_empatados[0]
        contador_local_puntos[1]=3*contador_local_ganados[1]+contador_local_empatados[1]
        proporcion_local_puntos[0]=calculosSin100(contador_local_puntos[0],contador_local_partidos[0])
        proporcion_local_puntos[1]=calculosSin100(contador_local_puntos[1],contador_local_partidos[1])




        






        #visitante ganador
        contador_visitante_ganados[0]= (datos_partidos_jugados_visitante_como_visitante['resultado_partido'] =='2').sum()
        porcentaje_visitante_ganados[0]=calculos(contador_visitante_ganados[0],contador_visitante_partidos[0])

        contador_visitante_empatados[0]= (datos_partidos_jugados_visitante_como_visitante['resultado_partido'] =='X').sum()
        porcentaje_visitante_empatados[0]=calculos(contador_visitante_empatados[0],contador_visitante_partidos[0])

        contador_visitante_perdidos[0]= (datos_partidos_jugados_visitante_como_visitante['resultado_partido'] =='1').sum()
        porcentaje_visitante_perdidos[0]=calculos(contador_visitante_perdidos[0],contador_visitante_partidos[0])

        contador_visitante_ganados[1]= (datos_partidos_jugados_visitante_como_local['resultado_partido'] =='1').sum()+contador_visitante_ganados[0]
        porcentaje_visitante_ganados[1]=calculos(contador_visitante_ganados[1],contador_visitante_partidos[1])

        contador_visitante_empatados[1]= (datos_partidos_jugados_visitante_como_local['resultado_partido'] =='X').sum()+contador_visitante_empatados[0]
        porcentaje_visitante_empatados[1]=calculos(contador_visitante_empatados[1],contador_visitante_partidos[1])

        contador_visitante_perdidos[1]= (datos_partidos_jugados_visitante_como_local['resultado_partido'] =='2').sum()+contador_visitante_perdidos[0]
        porcentaje_visitante_perdidos[1]=calculos(contador_visitante_perdidos[1],contador_visitante_partidos[1])








        #acumulador puntos visitante
        contador_visitante_puntos[0]=contador_visitante_ganados[0]*3+contador_visitante_empatados[0]
        contador_visitante_puntos[1]=contador_visitante_ganados[1]*3+contador_visitante_empatados[1]
        proporcion_visitante_puntos[0]=calculosSin100(contador_visitante_puntos[0],contador_visitante_partidos[0])
        proporcion_visitante_puntos[1]=calculosSin100(contador_visitante_puntos[1],contador_visitante_partidos[1])






        #local goles marcados
        contador_local_mas05_marcados[0]= (datos_partidos_jugados_local_como_local['resultado_local'] >0).sum()
        porcentaje_local_mas05_marcados[0]=calculos(contador_local_mas05_marcados[0],contador_local_partidos[0])

        contador_local_mas05_marcados[1]= (datos_partidos_jugados_local_como_visitante['resultado_visitante'] >0).sum()+contador_local_mas05_marcados[0]
        porcentaje_local_mas05_marcados[1]=calculos(contador_local_mas05_marcados[1],contador_local_partidos[1])

        contador_local_mas15_marcados[0]= (datos_partidos_jugados_local_como_local['resultado_local'] >1).sum()
        porcentaje_local_mas15_marcados[0]=calculos(contador_local_mas15_marcados[0],contador_local_partidos[0])

        contador_local_mas15_marcados[1]= (datos_partidos_jugados_local_como_visitante['resultado_visitante'] >1).sum()+contador_local_mas15_marcados[0]
        porcentaje_local_mas15_marcados[1]=calculos(contador_local_mas15_marcados[1],contador_local_partidos[1])

        contador_local_mas25_marcados[0]= (datos_partidos_jugados_local_como_local['resultado_local'] >2).sum()
        porcentaje_local_mas25_marcados[0]=calculos(contador_local_mas25_marcados[0],contador_local_partidos[0])

        contador_local_mas25_marcados[1]= (datos_partidos_jugados_local_como_visitante['resultado_visitante'] >2).sum()+contador_local_mas25_marcados[0]
        porcentaje_local_mas25_marcados[1]=calculos(contador_local_mas25_marcados[1],contador_local_partidos[1])












        #local goles encajados
        contador_local_mas05_encajados[0]= (datos_partidos_jugados_local_como_local['resultado_visitante'] >0).sum()
        porcentaje_local_mas05_encajados[0]=calculos(contador_local_mas05_encajados[0],contador_local_partidos[0])

        contador_local_mas05_encajados[1]= (datos_partidos_jugados_local_como_visitante['resultado_local'] >0).sum()+contador_local_mas05_encajados[0]
        porcentaje_local_mas05_encajados[1]=calculos(contador_local_mas05_encajados[1],contador_local_partidos[1])

        contador_local_mas15_encajados[0]= (datos_partidos_jugados_local_como_local['resultado_visitante'] >1).sum()
        porcentaje_local_mas15_encajados[0]=calculos(contador_local_mas15_encajados[0],contador_local_partidos[0])

        contador_local_mas15_encajados[1]= (datos_partidos_jugados_local_como_visitante['resultado_local'] >1).sum()+contador_local_mas15_encajados[0]
        porcentaje_local_mas15_encajados[1]=calculos(contador_local_mas15_encajados[1],contador_local_partidos[1])

        contador_local_mas25_encajados[0]= (datos_partidos_jugados_local_como_local['resultado_visitante'] >2).sum()
        porcentaje_local_mas25_encajados[0]=calculos(contador_local_mas25_encajados[0],contador_local_partidos[0])

        contador_local_mas25_encajados[1]= (datos_partidos_jugados_local_como_visitante['resultado_local'] >2).sum()+contador_local_mas25_encajados[0]
        porcentaje_local_mas25_encajados[1]=calculos(contador_local_mas25_encajados[1],contador_local_partidos[1])









        #visitante goles marcados
        contador_visitante_mas05_marcados[0]= (datos_partidos_jugados_visitante_como_visitante['resultado_visitante'] >0).sum()
        porcentaje_visitante_mas05_marcados[0]=calculos(contador_visitante_mas05_marcados[0],contador_visitante_partidos[0])

        contador_visitante_mas05_marcados[1]= (datos_partidos_jugados_visitante_como_local['resultado_local'] >0).sum()+contador_visitante_mas05_marcados[0]
        porcentaje_visitante_mas05_marcados[1]=calculos(contador_visitante_mas05_marcados[1],contador_visitante_partidos[1])

        contador_visitante_mas15_marcados[0]= (datos_partidos_jugados_visitante_como_visitante['resultado_visitante'] >1).sum()
        porcentaje_visitante_mas15_marcados[0]=calculos(contador_visitante_mas15_marcados[0],contador_visitante_partidos[0])

        contador_visitante_mas15_marcados[1]= (datos_partidos_jugados_visitante_como_local['resultado_local'] >1).sum()+contador_visitante_mas15_marcados[0]
        porcentaje_visitante_mas15_marcados[1]=calculos(contador_visitante_mas15_marcados[1],contador_visitante_partidos[1])

        contador_visitante_mas25_marcados[0]= (datos_partidos_jugados_visitante_como_visitante['resultado_visitante'] >2).sum()
        porcentaje_visitante_mas25_marcados[0]=calculos(contador_visitante_mas25_marcados[0],contador_visitante_partidos[0])

        contador_visitante_mas25_marcados[1]= (datos_partidos_jugados_visitante_como_local['resultado_local'] >2).sum()+contador_visitante_mas25_marcados[0]
        porcentaje_visitante_mas25_marcados[1]=calculos(contador_visitante_mas25_marcados[1],contador_visitante_partidos[1])













        #visitante goles encajados
        contador_visitante_mas05_encajados[0]= (datos_partidos_jugados_visitante_como_visitante['resultado_local'] >0).sum()
        porcentaje_visitante_mas05_encajados[0]=calculos(contador_visitante_mas05_encajados[0],contador_visitante_partidos[0])

        contador_visitante_mas05_encajados[1]= (datos_partidos_jugados_visitante_como_local['resultado_visitante'] >0).sum()+contador_visitante_mas05_encajados[0]
        porcentaje_visitante_mas05_encajados[1]=calculos(contador_visitante_mas05_encajados[1],contador_visitante_partidos[1])

        contador_visitante_mas15_encajados[0]= (datos_partidos_jugados_visitante_como_visitante['resultado_local'] >1).sum()
        porcentaje_visitante_mas15_encajados[0]=calculos(contador_visitante_mas15_encajados[0],contador_visitante_partidos[0])

        contador_visitante_mas15_encajados[1]= (datos_partidos_jugados_visitante_como_local['resultado_visitante'] >1).sum()+contador_visitante_mas15_encajados[0]
        porcentaje_visitante_mas15_encajados[1]=calculos(contador_visitante_mas15_encajados[1],contador_visitante_partidos[1])

        contador_visitante_mas25_encajados[0]= (datos_partidos_jugados_visitante_como_visitante['resultado_local'] >2).sum()
        porcentaje_visitante_mas25_encajados[0]=calculos(contador_visitante_mas25_encajados[0],contador_visitante_partidos[0])

        contador_visitante_mas25_encajados[1]= (datos_partidos_jugados_visitante_como_local['resultado_visitante'] >2).sum()+contador_visitante_mas25_encajados[0]
        porcentaje_visitante_mas25_encajados[1]=calculos(contador_visitante_mas25_encajados[1],contador_visitante_partidos[1])










        #local acumulador goles marcados
        contador_local_goles_marcados[0]=datos_partidos_jugados_local_como_local['resultado_local'].sum()
        proporcion_local_goles_marcados[0]=calculosSin100(contador_local_goles_marcados[0],contador_local_partidos[0])

        contador_local_goles_marcados[1]=datos_partidos_jugados_local_como_visitante['resultado_visitante'].sum()+contador_local_goles_marcados[0]
        proporcion_local_goles_marcados[1]=calculosSin100(contador_local_goles_marcados[1],contador_local_partidos[1])




        #local acumulador goles totales
        contador_local_goles_totales[0]=datos_partidos_jugados_local_como_local['total_goles'].sum()
        proporcion_local_goles_totales[0]=calculosSin100(contador_local_goles_totales[0],contador_local_partidos[0])

        contador_local_goles_totales[1]=datos_partidos_jugados_local_como_visitante['total_goles'].sum()+contador_local_goles_totales[0]
        proporcion_local_goles_totales[1]=calculosSin100(contador_local_goles_totales[1],contador_local_partidos[1])





        #visitante acumulador goles marcados
        contador_visitante_goles_marcados[0]=datos_partidos_jugados_visitante_como_visitante['resultado_visitante'].sum()
        proporcion_visitante_goles_marcados[0]=calculosSin100(contador_visitante_goles_marcados[0],contador_visitante_partidos[0])

        contador_visitante_goles_marcados[1]=datos_partidos_jugados_visitante_como_local['resultado_local'].sum()+contador_visitante_goles_marcados[0]
        proporcion_visitante_goles_marcados[1]=calculosSin100(contador_visitante_goles_marcados[1],contador_visitante_partidos[1])






        #visitante acumulador goles totales
        contador_visitante_goles_totales[0]=datos_partidos_jugados_visitante_como_visitante['total_goles'].sum()
        proporcion_visitante_goles_totales[0]=calculosSin100(contador_visitante_goles_totales[0],contador_local_partidos[0])

        contador_visitante_goles_totales[1]=datos_partidos_jugados_visitante_como_local['total_goles'].sum()+contador_visitante_goles_totales[0]
        proporcion_visitante_goles_totales[1]=calculosSin100(contador_visitante_goles_totales[1],contador_visitante_partidos[1])





        #local acumulador goles encajados
        contador_local_goles_encajados[0]=datos_partidos_jugados_local_como_local['resultado_visitante'].sum()
        proporcion_local_goles_encajados[0]=calculosSin100(contador_local_goles_encajados[0],contador_local_partidos[0])

        contador_local_goles_encajados[1]=datos_partidos_jugados_local_como_visitante['resultado_local'].sum()+contador_local_goles_encajados[0]
        proporcion_local_goles_encajados[1]=calculosSin100(contador_local_goles_encajados[1],contador_local_partidos[1])








        #visitante acumulador goles encajados
        contador_visitante_goles_encajados[0]=datos_partidos_jugados_visitante_como_visitante['resultado_local'].sum()
        proporcion_visitante_goles_encajados[0]=calculosSin100(contador_visitante_goles_encajados[0],contador_visitante_partidos[0])

        contador_visitante_goles_encajados[1]=datos_partidos_jugados_visitante_como_local['resultado_visitante'].sum()+contador_visitante_goles_encajados[0]
        proporcion_visitante_goles_encajados[1]=calculosSin100(contador_visitante_goles_encajados[1],contador_visitante_partidos[1])









        #local amarillas
        contador_local_amarillas[0]=datos_partidos_jugados_local_como_local['amarillas_local'].sum()
        proporcion_local_amarillas[0]=calculosSin100(contador_local_amarillas[0],contador_local_partidos[0])

        contador_local_amarillas[1]=datos_partidos_jugados_local_como_visitante['amarillas_visitante'].sum()+contador_local_amarillas[0]
        proporcion_local_amarillas[1]=calculosSin100(contador_local_amarillas[1],contador_local_partidos[1])








        #visitante amarillas
        contador_visitante_amarillas[0]=datos_partidos_jugados_visitante_como_visitante['amarillas_visitante'].sum()
        proporcion_visitante_amarillas[0]=calculosSin100(contador_visitante_amarillas[0],contador_visitante_partidos[0])

        contador_visitante_amarillas[1]=datos_partidos_jugados_visitante_como_local['amarillas_local'].sum()+contador_visitante_amarillas[0]
        proporcion_visitante_amarillas[1]=calculosSin100(contador_visitante_amarillas[1],contador_visitante_partidos[1])








        #local rojas
        contador_local_rojas[0]=datos_partidos_jugados_local_como_local['rojas_local'].sum()
        proporcion_local_rojas[0]=calculosSin100(contador_local_rojas[0],contador_local_partidos[0])

        contador_local_rojas[1]=datos_partidos_jugados_local_como_visitante['rojas_visitante'].sum()+contador_local_rojas[0]
        proporcion_local_rojas[1]=calculosSin100(contador_local_rojas[1],contador_local_partidos[1])








        #visitante rojas
        contador_visitante_rojas[0]=datos_partidos_jugados_visitante_como_visitante['rojas_visitante'].sum()
        proporcion_visitante_rojas[0]=calculosSin100(contador_visitante_rojas[0],contador_visitante_partidos[0])

        contador_visitante_rojas[1]=datos_partidos_jugados_visitante_como_local['rojas_local'].sum()+contador_visitante_rojas[0]
        proporcion_visitante_rojas[1]=calculosSin100(contador_visitante_rojas[1],contador_visitante_partidos[1])







        #local cambios
        contador_local_cambios[0]=datos_partidos_jugados_local_como_local['cambios_local'].sum()
        proporcion_local_cambios[0]=calculosSin100(contador_local_cambios[0],contador_local_partidos[0])

        contador_local_cambios[1]=datos_partidos_jugados_local_como_visitante['cambios_visitante'].sum()+contador_local_cambios[0]
        proporcion_local_cambios[1]=calculosSin100(contador_local_cambios[1],contador_local_partidos[1])









        #visitante cambios
        contador_visitante_cambios[0]=datos_partidos_jugados_visitante_como_visitante['cambios_visitante'].sum()
        proporcion_visitante_cambios[0]=calculosSin100(contador_visitante_cambios[0],contador_visitante_partidos[0])

        contador_visitante_cambios[1]=datos_partidos_jugados_visitante_como_local['cambios_local'].sum()+contador_visitante_cambios[0]
        proporcion_visitante_cambios[1]=calculosSin100(contador_visitante_cambios[1],contador_visitante_partidos[1])






        #local posesion
        contador_local_posesion[0]=datos_partidos_jugados_local_como_local['posesion_local'].sum()
        proporcion_local_posesion[0]=calculosSin100(contador_local_posesion[0],contador_local_partidos[0])

        contador_local_posesion[1]=datos_partidos_jugados_local_como_visitante['posesion_visitante'].sum()+contador_local_posesion[0]
        proporcion_local_posesion[1]=calculosSin100(contador_local_posesion[1],contador_local_partidos[1])







        #visitante posesion
        contador_visitante_posesion[0]=datos_partidos_jugados_visitante_como_visitante['posesion_visitante'].sum()
        proporcion_visitante_posesion[0]=calculosSin100(contador_visitante_posesion[0],contador_visitante_partidos[0])

        contador_visitante_posesion[1]=datos_partidos_jugados_visitante_como_local['posesion_local'].sum()+contador_visitante_posesion[0]
        proporcion_visitante_posesion[1]=calculosSin100(contador_visitante_posesion[1],contador_visitante_partidos[1])






        #local total_tiros
        contador_local_total_tiros[0]=datos_partidos_jugados_local_como_local['total_tiros_local'].sum()
        proporcion_local_total_tiros[0]=calculosSin100(contador_local_total_tiros[0],contador_local_partidos[0])

        contador_local_total_tiros[1]=datos_partidos_jugados_local_como_visitante['total_tiros_visitante'].sum()+contador_local_total_tiros[0]
        proporcion_local_total_tiros[1]=calculosSin100(contador_local_total_tiros[1],contador_local_partidos[1])






        #visitante total_tiros
        contador_visitante_total_tiros[0]=datos_partidos_jugados_visitante_como_visitante['total_tiros_visitante'].sum()
        proporcion_visitante_total_tiros[0]=calculosSin100(contador_visitante_total_tiros[0],contador_visitante_partidos[0])

        contador_visitante_total_tiros[1]=datos_partidos_jugados_visitante_como_local['total_tiros_local'].sum()+contador_visitante_total_tiros[0]
        proporcion_visitante_total_tiros[1]=calculosSin100(contador_visitante_total_tiros[1],contador_visitante_partidos[1])






        #local corners_afavor
        contador_local_corners_afavor[0]=datos_partidos_jugados_local_como_local['corners_local'].sum()
        proporcion_local_corners_afavor[0]=calculosSin100(contador_local_corners_afavor[0],contador_local_partidos[0])

        contador_local_corners_afavor[1]=datos_partidos_jugados_local_como_visitante['corners_visitante'].sum()+contador_local_corners_afavor[0]
        proporcion_local_corners_afavor[1]=calculosSin100(contador_local_corners_afavor[1],contador_local_partidos[1])









        #visitante corners_afavor
        contador_visitante_corners_afavor[0]=datos_partidos_jugados_visitante_como_visitante['corners_visitante'].sum()
        proporcion_visitante_corners_afavor[0]=calculosSin100(contador_visitante_corners_afavor[0],contador_visitante_partidos[0])

        contador_visitante_corners_afavor[1]=datos_partidos_jugados_visitante_como_local['corners_local'].sum()+contador_visitante_corners_afavor[0]
        proporcion_visitante_corners_afavor[1]=calculosSin100(contador_visitante_corners_afavor[1],contador_visitante_partidos[1])






        #local corners_encontra
        contador_local_corners_encontra[0]=datos_partidos_jugados_local_como_local['corners_visitante'].sum()
        proporcion_local_corners_encontra[0]=calculosSin100(contador_local_corners_encontra[0],contador_local_partidos[0])

        contador_local_corners_encontra[1]=datos_partidos_jugados_local_como_visitante['corners_local'].sum()+contador_local_corners_encontra[0]
        proporcion_local_corners_encontra[1]=calculosSin100(contador_local_corners_encontra[1],contador_local_partidos[1])





        #visitante corners_encontra
        contador_visitante_corners_encontra[0]=datos_partidos_jugados_visitante_como_visitante['corners_local'].sum()
        proporcion_visitante_corners_encontra[0]=calculosSin100(contador_visitante_corners_encontra[0],contador_visitante_partidos[0])

        contador_visitante_corners_encontra[1]=datos_partidos_jugados_visitante_como_local['corners_visitante'].sum()+contador_visitante_corners_encontra[0]
        proporcion_visitante_corners_encontra[1]=calculosSin100(contador_visitante_corners_encontra[1],contador_visitante_partidos[1])
    

        '''print(contador_local_perdidos[1])
        print(contador_local_puntos[1])
        print(contador_visitante_puntos[1])
        print(contador_visitante_mas05_marcados[0])
        print(contador_visitante_mas05_marcados[1])
        print(contador_visitante_mas15_marcados[0])
        print(contador_visitante_mas15_marcados[1])
        print(contador_visitante_mas05_encajados[0])
        print(contador_visitante_mas05_encajados[1])
        print(contador_visitante_mas15_encajados[0])
        print(contador_visitante_mas15_encajados[1])
        print("\n")'''

        '''
        print("amarillas local sitio: "+str(contador_local_amarillas[0]))
        print("amarillas local general: "+str(contador_local_amarillas[1]))
        print("amarillas visitante sitio: "+str(contador_visitante_amarillas[0]))
        print("amarillas visitante general: "+str(contador_visitante_amarillas[1]))
        print("partidos local local: "+str(contador_local_partidos[0]))
        print("partidos local total: "+str(contador_local_partidos[1]))
        print("\n")
        print("rojas local sitio: "+str(contador_local_rojas[0]))
        print("rojas local general: "+str(contador_local_rojas[1]))
        print("rojas visitante sitio: "+str(contador_visitante_rojas[0]))
        print("rojas visitante general: "+str(contador_visitante_rojas[1]))
        print("partidos visitante local: "+str(contador_visitante_partidos[0]))
        print("partidos visitante total: "+str(contador_visitante_partidos[1]))
        print("\n")
        '''





        contador_local_cambios_76_final[0]=0
        contador_local_cambios_76_final[1]=0
        contador_local_cambios_61_75[0]=0
        contador_local_cambios_61_75[1]=0
        contador_local_cambios_45_60[0]=0
        contador_local_cambios_45_60[1]=0
        contador_local_cambios_antes_descanso[0]=0
        contador_local_cambios_antes_descanso[1]=0
        contador_local_cambios_amarillas[0]=0
        contador_local_cambios_amarillas[1]=0
        contador_local_cambios_lesionados[0]=0
        contador_local_cambios_lesionados[1]=0
        contador_local_cambios_goleadores[0]=0
        contador_local_cambios_goleadores[1]=0
        contador_local_cambios_asistentes[0]=0
        contador_local_cambios_asistentes[1]=0
        contador_local_cambios_delanteros_a_centrocampistas[0]=0
        contador_local_cambios_delanteros_a_centrocampistas[1]=0
        contador_local_cambios_delanteros_a_defensas[0]=0
        contador_local_cambios_delanteros_a_defensas[1]=0
        contador_local_cambios_defensas_a_centrocampistas[0]=0
        contador_local_cambios_defensas_a_centrocampistas[1]=0
        contador_local_cambios_defensas_a_delanteros[0]=0
        contador_local_cambios_defensas_a_delanteros[1]=0
        contador_local_cambios_centrocampistas_a_delanteros[0]=0
        contador_local_cambios_centrocampistas_a_delanteros[1]=0
        contador_local_cambios_centrocampistas_a_defensas[0]=0
        contador_local_cambios_centrocampistas_a_defensas[1]=0




        contador_visitante_cambios_76_final[0]=0
        contador_visitante_cambios_76_final[1]=0
        contador_visitante_cambios_61_75[0]=0
        contador_visitante_cambios_61_75[1]=0
        contador_visitante_cambios_45_60[0]=0
        contador_visitante_cambios_45_60[1]=0
        contador_visitante_cambios_antes_descanso[0]=0
        contador_visitante_cambios_antes_descanso[1]=0
        contador_visitante_cambios_amarillas[0]=0
        contador_visitante_cambios_amarillas[1]=0
        contador_visitante_cambios_lesionados[0]=0
        contador_visitante_cambios_lesionados[1]=0
        contador_visitante_cambios_goleadores[0]=0
        contador_visitante_cambios_goleadores[1]=0
        contador_visitante_cambios_asistentes[0]=0
        contador_visitante_cambios_asistentes[1]=0
        contador_visitante_cambios_delanteros_a_centrocampistas[0]=0
        contador_visitante_cambios_delanteros_a_centrocampistas[1]=0
        contador_visitante_cambios_delanteros_a_defensas[0]=0
        contador_visitante_cambios_delanteros_a_defensas[1]=0
        contador_visitante_cambios_defensas_a_centrocampistas[0]=0
        contador_visitante_cambios_defensas_a_centrocampistas[1]=0
        contador_visitante_cambios_defensas_a_delanteros[0]=0
        contador_visitante_cambios_defensas_a_delanteros[1]=0
        contador_visitante_cambios_centrocampistas_a_delanteros[0]=0
        contador_visitante_cambios_centrocampistas_a_delanteros[1]=0
        contador_visitante_cambios_centrocampistas_a_defensas[0]=0
        contador_visitante_cambios_centrocampistas_a_defensas[1]=0


        valores_unicos_partidos = datos_jugadores_partidos_filtrados_local_como_local['id_partido'].unique()
        valores_unicos_partidos=list(valores_unicos_partidos)
        

        #local como local
        print("Cambios local como local----------------------------------")
        dataframe_cambios_local_local=pd.DataFrame(columns=["nombreSale","nombreEntra","posicionSale","posicionEntra","minuto","goles","asistencias","lesion","amarillas"])
        dataframe_datos_totales_jugadores_local_local=pd.DataFrame(columns=["id_jugador","nombre","equipo","posicion","id_partido","titular"])
        for indexJug, rowJug in datos_jugadores_partidos_filtrados_local_como_local.iterrows():
            id_jugador = rowJug['id_jugador']
            sustituido_id_jugador = rowJug['sustituido_por']
            cambio = rowJug['cambio']
            amarillas = rowJug['amarilla']
            goles = rowJug['goles']
            asistencias = rowJug['asistencias']
            lesion = rowJug['lesion']
            id_partido_actual = rowJug['id_partido']
            titular_actual = rowJug['titular']


            #nombre del jugador que sale
            resultado = jugadores.loc[(jugadores['id_jugador'] == id_jugador) ]               
            if not resultado.empty:
                nombre = resultado['nombre'].values[0]


            #equipo del que sale
            resultado = jugadores.loc[(jugadores['id_jugador'] == id_jugador) ]               
            if not resultado.empty:
                id_equipo_jugador = resultado['id_equipo'].values[0]
            else:
                print(f"No se encontro en nombre")


            #buscamos posicion del que sale
            resultado = jugadores.loc[(jugadores['id_jugador'] == id_jugador) ]               
            if not resultado.empty:
                posicion = resultado['posicion'].values[0]
            else:
                print(f"No se encontro en busqueda posicion")



            if id_equipo_jugador==id_equipo_local:
                if titular_actual==1:
                    dataframe_datos_totales_jugadores_local_local.loc[len(dataframe_datos_totales_jugadores_local_local)]=[id_jugador,nombre,id_equipo_jugador,posicion,id_partido_actual,titular_actual]


                    indice_anterior = datos_jugadores_partidos_filtrados_local_como_local.index.get_loc(indexJug) - 1
                    while indice_anterior >= 0:
                        fila_anterior = datos_jugadores_partidos_filtrados_local_como_local.iloc[indice_anterior]
                        indice_actual = valores_unicos_partidos.index(id_partido_actual)
                        indice_revisado = valores_unicos_partidos.index(fila_anterior['id_partido'])

                        if indice_actual-1==indice_revisado:
                            if fila_anterior['id_jugador'] == id_jugador:
                                titular_anterior = fila_anterior['titular']
                                if titular_anterior != titular_actual:
                                    if posicion=="Defensa":
                                        contador_local_cambios_alineacion_defensa[0]=contador_local_cambios_alineacion_defensa[0]+1
                                    elif posicion=="Centrocampista":
                                        contador_local_cambios_alineacion_centrocampista[0]=contador_local_cambios_alineacion_centrocampista[0]+1
                                    elif posicion=="Delantero":
                                        contador_local_cambios_alineacion_delantero[0]=contador_local_cambios_alineacion_delantero[0]+1
                                    '''if id_equipo_jugador==5:
                                        print(f"{id_partido_actual}: equipo: {id_equipo_jugador} El jugador con id {nombre} diferente")'''
                                break

                        if indice_anterior==0:
                            if posicion=="Defensa":
                                contador_local_cambios_alineacion_defensa[0]=contador_local_cambios_alineacion_defensa[0]+1
                            elif posicion=="Centrocampista":
                                contador_local_cambios_alineacion_centrocampista[0]=contador_local_cambios_alineacion_centrocampista[0]+1
                            elif posicion=="Delantero":
                                contador_local_cambios_alineacion_delantero[0]=contador_local_cambios_alineacion_delantero[0]+1
                            '''if id_equipo_jugador==5:
                                print(f"{id_partido_actual}: equipo: {id_equipo_jugador} El jugador con id {nombre} titular nuevo")'''


                        indice_anterior -= 1




           




            
            


            if cambio>0 and sustituido_id_jugador>0 and id_equipo_jugador==id_equipo_local:


                #buscamos posicion del que entra
                resultado = jugadores.loc[(jugadores['id_jugador'] == sustituido_id_jugador) ]               
                if not resultado.empty:
                    posicion_sustituto = resultado['posicion'].values[0]
                else:
                    #print(f"No se encontro en busqueda posicion")
                    posicion_sustituto="No encontrada"
                
                #nombre del que entra
                resultado = jugadores.loc[(jugadores['id_jugador'] == sustituido_id_jugador) ]               
                if not resultado.empty:
                    nombreEntra = resultado['nombre'].values[0]
                else:
                    print(f"No se encontro en nombre")
                


                
                dataframe_cambios_local_local.loc[len(dataframe_cambios_local_local)]=[nombre, nombreEntra,posicion,posicion_sustituto,cambio,goles,asistencias,lesion,amarillas]



                #minutos analisis cambio
                if cambio<=45:
                    contador_local_cambios_antes_descanso[0]=contador_local_cambios_antes_descanso[0]+1
                elif cambio<=60 and cambio>45:
                    contador_local_cambios_45_60[0]=contador_local_cambios_45_60[0]+1    
                elif cambio<=75 and cambio>60:
                    contador_local_cambios_61_75[0]=contador_local_cambios_61_75[0]+1 
                else:
                    contador_local_cambios_76_final[0]=contador_local_cambios_76_final[0]+1 




                #posiciones analisis cambios
                if posicion=="Delantero" and posicion_sustituto=="Defensa":
                    contador_local_cambios_delanteros_a_defensas[0]=contador_local_cambios_delanteros_a_defensas[0]+1
                elif posicion=="Delantero" and posicion_sustituto=="Centrocampista":
                    contador_local_cambios_delanteros_a_centrocampistas[0]=contador_local_cambios_delanteros_a_centrocampistas[0]+1               
                elif posicion=="Defensa" and posicion_sustituto=="Centrocampista":
                    contador_local_cambios_defensas_a_centrocampistas[0]=contador_local_cambios_defensas_a_centrocampistas[0]+1  
                elif posicion=="Defensa" and posicion_sustituto=="Delantero":
                    contador_local_cambios_defensas_a_delanteros[0]=contador_local_cambios_defensas_a_delanteros[0]+1 
                elif posicion=="Centrocampista" and posicion_sustituto=="Delantero":
                    contador_local_cambios_centrocampistas_a_delanteros[0]=contador_local_cambios_centrocampistas_a_delanteros[0]+1       
                elif posicion=="Centrocampista" and posicion_sustituto=="Defensa":
                    contador_local_cambios_centrocampistas_a_defensas[0]=contador_local_cambios_centrocampistas_a_defensas[0]+1    




                #otros campos
                if amarillas>0:
                    contador_local_cambios_amarillas[0]=contador_local_cambios_amarillas[0] +1
                if goles>0:
                    contador_local_cambios_goleadores[0]=contador_local_cambios_goleadores[0] +1
                if asistencias>0:
                    contador_local_cambios_asistentes[0]=contador_local_cambios_asistentes[0] +1
                if lesion>0:
                    contador_local_cambios_lesionados[0]=contador_local_cambios_lesionados[0] +1


                media_local_cambio_minutos[0]=media_local_cambio_minutos[0]+cambio



        dataframe_cambios_local_local.to_csv('csv/estadisticasCambiosLocalLocal.csv', index=False) 
        dataframe_datos_totales_jugadores_local_local.to_csv('csv/titulLocalLocal.csv', index=False)


















        contador_local_cambios_antes_descanso[1]=contador_local_cambios_antes_descanso[0]
        contador_local_cambios_45_60[1]=contador_local_cambios_45_60[0]
        contador_local_cambios_61_75[1]=contador_local_cambios_61_75[0]
        contador_local_cambios_76_final[1]=contador_local_cambios_76_final[0]
        contador_local_cambios_delanteros_a_defensas[1]=contador_local_cambios_delanteros_a_defensas[0]
        contador_local_cambios_delanteros_a_centrocampistas[1]=contador_local_cambios_delanteros_a_centrocampistas[0]
        contador_local_cambios_defensas_a_centrocampistas[1]=contador_local_cambios_defensas_a_centrocampistas[0]
        contador_local_cambios_defensas_a_delanteros[1]=contador_local_cambios_defensas_a_delanteros[0]
        contador_local_cambios_centrocampistas_a_delanteros[1]=contador_local_cambios_centrocampistas_a_delanteros[0]
        contador_local_cambios_centrocampistas_a_defensas[1]=contador_local_cambios_centrocampistas_a_defensas[0]
        contador_local_cambios_amarillas[1]=contador_local_cambios_amarillas[0]
        contador_local_cambios_goleadores[1]=contador_local_cambios_goleadores[0]
        contador_local_cambios_asistentes[1]=contador_local_cambios_asistentes[0]
        contador_local_cambios_lesionados[1]=contador_local_cambios_lesionados[0]
        media_local_cambio_minutos[1]=media_local_cambio_minutos[0]


        contador_local_cambios_alineacion_delantero[1]=contador_local_cambios_alineacion_delantero[0]
        contador_local_cambios_alineacion_centrocampista[1]=contador_local_cambios_alineacion_centrocampista[0]
        contador_local_cambios_alineacion_defensa[1]=contador_local_cambios_alineacion_defensa[0]



        valores_unicos_partidos = datos_jugadores_partidos_filtrados_local_como_visitante['id_partido'].unique()
        valores_unicos_partidos=list(valores_unicos_partidos)

        #local como visitante
        print("Cambios local como visitante----------------------------------")
        dataframe_cambios_local_visitante=pd.DataFrame(columns=["nombreSale","nombreEntra","posicionSale","posicionEntra","minuto","goles","asistencias","lesion","amarillas"])
        dataframe_datos_totales_jugadores_local_visitante=pd.DataFrame(columns=["id_jugador","nombre","equipo","posicion","id_partido","titular"])
        for indexJug2, rowJug2 in datos_jugadores_partidos_filtrados_local_como_visitante.iterrows():
            id_jugador = rowJug2['id_jugador']
            sustituido_id_jugador = rowJug2['sustituido_por']
            cambio = rowJug2['cambio']
            amarillas = rowJug2['amarilla']
            goles = rowJug2['goles']
            asistencias = rowJug2['asistencias']
            lesion = rowJug2['lesion']
            id_partido_actual = rowJug2['id_partido']
            titular_actual = rowJug2['titular']


            #nombre del jugador que sale
            resultado = jugadores.loc[(jugadores['id_jugador'] == id_jugador) ]               
            if not resultado.empty:
                nombre = resultado['nombre'].values[0]


            #equipo del que sale
            resultado = jugadores.loc[(jugadores['id_jugador'] == id_jugador) ]               
            if not resultado.empty:
                id_equipo_jugador = resultado['id_equipo'].values[0]
            else:
                print(f"No se encontro en nombre")


            #buscamos posicion del que sale
            resultado = jugadores.loc[(jugadores['id_jugador'] == id_jugador) ]               
            if not resultado.empty:
                posicion = resultado['posicion'].values[0]
            else:
                print(f"No se encontro en busqueda posicion")




            if id_equipo_jugador==id_equipo_local:
                if titular_actual==1:
                    dataframe_datos_totales_jugadores_local_visitante.loc[len(dataframe_datos_totales_jugadores_local_visitante)]=[id_jugador,nombre,id_equipo_jugador,posicion,id_partido_actual,titular_actual]


                    indice_anterior = datos_jugadores_partidos_filtrados_local_como_visitante.index.get_loc(indexJug2) - 1
                    while indice_anterior >= 0:
                        fila_anterior = datos_jugadores_partidos_filtrados_local_como_visitante.iloc[indice_anterior]
                        indice_actual = valores_unicos_partidos.index(id_partido_actual)
                        indice_revisado = valores_unicos_partidos.index(fila_anterior['id_partido'])

                        if indice_actual-1==indice_revisado:
                            if fila_anterior['id_jugador'] == id_jugador:
                                titular_anterior = fila_anterior['titular']
                                if titular_anterior != titular_actual:
                                    if posicion=="Defensa":
                                        contador_local_cambios_alineacion_defensa[1]=contador_local_cambios_alineacion_defensa[1]+1
                                    elif posicion=="Centrocampista":
                                        contador_local_cambios_alineacion_centrocampista[1]=contador_local_cambios_alineacion_centrocampista[1]+1
                                    elif posicion=="Delantero":
                                        contador_local_cambios_alineacion_delantero[1]=contador_local_cambios_alineacion_delantero[1]+1
                                    '''if id_equipo_jugador==5:
                                        print(f"{id_partido_actual}: equipo: {id_equipo_jugador} El jugador con id {nombre} diferente")'''
                                break

                        if indice_anterior==0:
                            if posicion=="Defensa":
                                contador_local_cambios_alineacion_defensa[1]=contador_local_cambios_alineacion_defensa[1]+1
                            elif posicion=="Centrocampista":
                                contador_local_cambios_alineacion_centrocampista[1]=contador_local_cambios_alineacion_centrocampista[1]+1
                            elif posicion=="Delantero":
                                contador_local_cambios_alineacion_delantero[1]=contador_local_cambios_alineacion_delantero[1]+1
                            '''if id_equipo_jugador==5:
                                print(f"{id_partido_actual}: equipo: {id_equipo_jugador} El jugador con id {nombre} titular nuevo")'''


                        indice_anterior -= 1







            if cambio>0 and sustituido_id_jugador>0 and id_equipo_jugador==id_equipo_local:




                #buscamos posicion del que entra
                resultado = jugadores.loc[(jugadores['id_jugador'] == sustituido_id_jugador) ]               
                if not resultado.empty:
                    posicion_sustituto = resultado['posicion'].values[0]
                else:
                    #print(f"No se encontro en busqueda posicion")
                    posicion_sustituto="No encontrada"

                #nombre del que entra
                resultado = jugadores.loc[(jugadores['id_jugador'] == sustituido_id_jugador) ]               
                if not resultado.empty:
                    nombreEntra = resultado['nombre'].values[0]
                else:
                    print(f"No se encontro en nombre")
                

                dataframe_cambios_local_visitante.loc[len(dataframe_cambios_local_visitante)]=[nombre, nombreEntra,posicion,posicion_sustituto,cambio,goles,asistencias,lesion,amarillas]






                #minutos analisis cambio
                if cambio<=45:
                    contador_local_cambios_antes_descanso[1]=contador_local_cambios_antes_descanso[1]+1
                elif cambio<=60 and cambio>45:
                    contador_local_cambios_45_60[1]=contador_local_cambios_45_60[1]+1    
                elif cambio<=75 and cambio>60:
                    contador_local_cambios_61_75[1]=contador_local_cambios_61_75[1]+1 
                else:
                    contador_local_cambios_76_final[1]=contador_local_cambios_76_final[1]+1 




                #posiciones analisis cambios
                if posicion=="Delantero" and posicion_sustituto=="Defensa":
                    contador_local_cambios_delanteros_a_defensas[1]=contador_local_cambios_delanteros_a_defensas[1]+1
                elif posicion=="Delantero" and posicion_sustituto=="Centrocampista":
                    contador_local_cambios_delanteros_a_centrocampistas[1]=contador_local_cambios_delanteros_a_centrocampistas[1]+1               
                elif posicion=="Defensa" and posicion_sustituto=="Centrocampista":
                    contador_local_cambios_defensas_a_centrocampistas[1]=contador_local_cambios_defensas_a_centrocampistas[1]+1  
                elif posicion=="Defensa" and posicion_sustituto=="Delantero":
                    contador_local_cambios_defensas_a_delanteros[1]=contador_local_cambios_defensas_a_delanteros[1]+1 
                elif posicion=="Centrocampista" and posicion_sustituto=="Delantero":
                    contador_local_cambios_centrocampistas_a_delanteros[1]=contador_local_cambios_centrocampistas_a_delanteros[1]+1       
                elif posicion=="Centrocampista" and posicion_sustituto=="Defensa":
                    contador_local_cambios_centrocampistas_a_defensas[1]=contador_local_cambios_centrocampistas_a_defensas[1]+1    




                #otros campos
                if amarillas>0:
                    contador_local_cambios_amarillas[1]=contador_local_cambios_amarillas[1] +1
                if goles>0:
                    contador_local_cambios_goleadores[1]=contador_local_cambios_goleadores[1] +1
                if asistencias>0:
                    contador_local_cambios_asistentes[1]=contador_local_cambios_asistentes[1] +1
                if lesion>0:
                    contador_local_cambios_lesionados[1]=contador_local_cambios_lesionados[1] +1


                media_local_cambio_minutos[1]=media_local_cambio_minutos[1]+cambio




        dataframe_cambios_local_visitante.to_csv('csv/estadisticasCambiosLocalVisitante.csv', index=False) 
        dataframe_datos_totales_jugadores_local_visitante.to_csv('csv/titulLocalVisitante.csv', index=False)





















        #visitante como visitante


        valores_unicos_partidos = datos_jugadores_partidos_filtrados_visitante_como_visitante['id_partido'].unique()
        valores_unicos_partidos=list(valores_unicos_partidos)
        print("Cambios visitante como visitante----------------------------------")
        dataframe_cambios_visitante_visitante=pd.DataFrame(columns=["nombreSale","nombreEntra","posicionSale","posicionEntra","minuto","goles","asistencias","lesion","amarillas"])
        dataframe_datos_totales_jugadores_visitante_visitante=pd.DataFrame(columns=["id_jugador","nombre","equipo","posicion","id_partido","titular"])
        for indexJug1, rowJug1 in datos_jugadores_partidos_filtrados_visitante_como_visitante.iterrows():
            id_jugador = rowJug1['id_jugador']
            sustituido_id_jugador = rowJug1['sustituido_por']
            cambio = rowJug1['cambio']
            amarillas = rowJug1['amarilla']
            goles = rowJug1['goles']
            asistencias = rowJug1['asistencias']
            lesion = rowJug1['lesion']
            id_partido_actual = rowJug1['id_partido']
            titular_actual = rowJug1['titular']


            #nombre del jugador que sale
            resultado = jugadores.loc[(jugadores['id_jugador'] == id_jugador) ]               
            if not resultado.empty:
                nombre = resultado['nombre'].values[0]


            #equipo del que sale
            resultado = jugadores.loc[(jugadores['id_jugador'] == id_jugador) ]               
            if not resultado.empty:
                id_equipo_jugador = resultado['id_equipo'].values[0]
            else:
                print(f"No se encontro en nombre")


            #buscamos posicion del que sale
            resultado = jugadores.loc[(jugadores['id_jugador'] == id_jugador) ]               
            if not resultado.empty:
                posicion = resultado['posicion'].values[0]
            else:
                print(f"No se encontro en busqueda posicion")



            if id_equipo_jugador==id_equipo_visitante:
                if titular_actual==1:
                    dataframe_datos_totales_jugadores_visitante_visitante.loc[len(dataframe_datos_totales_jugadores_visitante_visitante)]=[id_jugador,nombre,id_equipo_jugador,posicion,id_partido_actual,titular_actual]


                    indice_anterior = datos_jugadores_partidos_filtrados_visitante_como_visitante.index.get_loc(indexJug1) - 1
                    while indice_anterior >= 0:
                        fila_anterior = datos_jugadores_partidos_filtrados_visitante_como_visitante.iloc[indice_anterior]
                        indice_actual = valores_unicos_partidos.index(id_partido_actual)
                        indice_revisado = valores_unicos_partidos.index(fila_anterior['id_partido'])

                        if indice_actual-1==indice_revisado:
                            if fila_anterior['id_jugador'] == id_jugador:
                                titular_anterior = fila_anterior['titular']
                                if titular_anterior != titular_actual:
                                    if posicion=="Defensa":
                                        contador_visitante_cambios_alineacion_defensa[0]=contador_visitante_cambios_alineacion_defensa[0]+1
                                    elif posicion=="Centrocampista":
                                        contador_visitante_cambios_alineacion_centrocampista[0]=contador_visitante_cambios_alineacion_centrocampista[0]+1
                                    elif posicion=="Delantero":
                                        contador_visitante_cambios_alineacion_delantero[0]=contador_visitante_cambios_alineacion_delantero[0]+1
                                    '''if id_equipo_jugador==13:
                                        print(f"{id_partido_actual}: equipo: {id_equipo_jugador} El jugador con id {nombre} diferente")'''
                                break

                        if indice_anterior==0:
                            if posicion=="Defensa":
                                contador_visitante_cambios_alineacion_defensa[0]=contador_visitante_cambios_alineacion_defensa[0]+1
                            elif posicion=="Centrocampista":
                                contador_visitante_cambios_alineacion_centrocampista[0]=contador_visitante_cambios_alineacion_centrocampista[0]+1
                            elif posicion=="Delantero":
                                contador_visitante_cambios_alineacion_delantero[0]=contador_visitante_cambios_alineacion_delantero[0]+1
                            '''if id_equipo_jugador==13:
                                print(f"{id_partido_actual}: equipo: {id_equipo_jugador} El jugador con id {nombre} titular nuevo")'''


                        indice_anterior -= 1




            if cambio>0 and sustituido_id_jugador>0 and id_equipo_jugador==id_equipo_visitante:






                #buscamos posicion del que entra
                resultado = jugadores.loc[(jugadores['id_jugador'] == sustituido_id_jugador) ]               
                if not resultado.empty:
                    posicion_sustituto = resultado['posicion'].values[0]
                else:
                    #print(f"No se encontro en busqueda posicion")
                    posicion_sustituto="No encontrada"

                
                #nombre del que entra
                resultado = jugadores.loc[(jugadores['id_jugador'] == sustituido_id_jugador) ]               
                if not resultado.empty:
                    nombreEntra = resultado['nombre'].values[0]
                else:
                    print(f"No se encontro en nombre")
                



                dataframe_cambios_visitante_visitante.loc[len(dataframe_cambios_visitante_visitante)]=[nombre, nombreEntra,posicion,posicion_sustituto,cambio,goles,asistencias,lesion,amarillas]


                #minutos analisis cambio
                if cambio<=45:
                    contador_visitante_cambios_antes_descanso[0]=contador_visitante_cambios_antes_descanso[0]+1
                elif cambio<=60 and cambio>45:
                    contador_visitante_cambios_45_60[0]=contador_visitante_cambios_45_60[0]+1    
                elif cambio<=75 and cambio>60:
                    contador_visitante_cambios_61_75[0]=contador_visitante_cambios_61_75[0]+1 
                else:
                    contador_visitante_cambios_76_final[0]=contador_visitante_cambios_76_final[0]+1 




                #posiciones analisis cambios
                if posicion=="Delantero" and posicion_sustituto=="Defensa":
                    contador_visitante_cambios_delanteros_a_defensas[0]=contador_visitante_cambios_delanteros_a_defensas[0]+1
                elif posicion=="Delantero" and posicion_sustituto=="Centrocampista":
                    contador_visitante_cambios_delanteros_a_centrocampistas[0]=contador_visitante_cambios_delanteros_a_centrocampistas[0]+1               
                elif posicion=="Defensa" and posicion_sustituto=="Centrocampista":
                    contador_visitante_cambios_defensas_a_centrocampistas[0]=contador_visitante_cambios_defensas_a_centrocampistas[0]+1  
                elif posicion=="Defensa" and posicion_sustituto=="Delantero":
                    contador_visitante_cambios_defensas_a_delanteros[0]=contador_visitante_cambios_defensas_a_delanteros[0]+1 
                elif posicion=="Centrocampista" and posicion_sustituto=="Delantero":
                    contador_visitante_cambios_centrocampistas_a_delanteros[0]=contador_visitante_cambios_centrocampistas_a_delanteros[0]+1       
                elif posicion=="Centrocampista" and posicion_sustituto=="Defensa":
                    contador_visitante_cambios_centrocampistas_a_defensas[0]=contador_visitante_cambios_centrocampistas_a_defensas[0]+1    




                #otros campos
                if amarillas>0:
                    contador_visitante_cambios_amarillas[0]=contador_visitante_cambios_amarillas[0] +1
                if goles>0:
                    contador_visitante_cambios_goleadores[0]=contador_visitante_cambios_goleadores[0] +1
                if asistencias>0:
                    contador_visitante_cambios_asistentes[0]=contador_visitante_cambios_asistentes[0] +1
                if lesion>0:
                    contador_visitante_cambios_lesionados[0]=contador_visitante_cambios_lesionados[0] +1


                media_visitante_cambio_minutos[0]=media_visitante_cambio_minutos[0]+cambio



        dataframe_cambios_visitante_visitante.to_csv('csv/estadisticasCambiosVisitanteVisitante.csv', index=False) 
        dataframe_datos_totales_jugadores_visitante_visitante.to_csv('csv/titulVisitanteVisitante.csv', index=False)





       


        contador_visitante_cambios_antes_descanso[1]=contador_visitante_cambios_antes_descanso[0]
        contador_visitante_cambios_45_60[1]=contador_visitante_cambios_45_60[0]
        contador_visitante_cambios_61_75[1]=contador_visitante_cambios_61_75[0]
        contador_visitante_cambios_76_final[1]=contador_visitante_cambios_76_final[0]
        contador_visitante_cambios_delanteros_a_defensas[1]=contador_visitante_cambios_delanteros_a_defensas[0]
        contador_visitante_cambios_delanteros_a_centrocampistas[1]=contador_visitante_cambios_delanteros_a_centrocampistas[0]
        contador_visitante_cambios_defensas_a_centrocampistas[1]=contador_visitante_cambios_defensas_a_centrocampistas[0]
        contador_visitante_cambios_defensas_a_delanteros[1]=contador_visitante_cambios_defensas_a_delanteros[0]
        contador_visitante_cambios_centrocampistas_a_delanteros[1]=contador_visitante_cambios_centrocampistas_a_delanteros[0]
        contador_visitante_cambios_centrocampistas_a_defensas[1]=contador_visitante_cambios_centrocampistas_a_defensas[0]
        contador_visitante_cambios_amarillas[1]=contador_visitante_cambios_amarillas[0]
        contador_visitante_cambios_goleadores[1]=contador_visitante_cambios_goleadores[0]
        contador_visitante_cambios_asistentes[1]=contador_visitante_cambios_asistentes[0]
        contador_visitante_cambios_lesionados[1]=contador_visitante_cambios_lesionados[0]
        media_visitante_cambio_minutos[1]=media_visitante_cambio_minutos[0]


        contador_visitante_cambios_alineacion_delantero[1]=contador_visitante_cambios_alineacion_delantero[0]
        contador_visitante_cambios_alineacion_centrocampista[1]=contador_visitante_cambios_alineacion_centrocampista[0]
        contador_visitante_cambios_alineacion_defensa[1]=contador_visitante_cambios_alineacion_defensa[0]


        #visitante como local
        valores_unicos_partidos = datos_jugadores_partidos_filtrados_visitante_como_local['id_partido'].unique()
        valores_unicos_partidos=list(valores_unicos_partidos)
        print("Cambios visitante como local----------------------------------")
        dataframe_cambios_visitante_local=pd.DataFrame(columns=["nombreSale","nombreEntra","posicionSale","posicionEntra","minuto","goles","asistencias","lesion","amarillas"])
        dataframe_datos_totales_jugadores_visitante_local=pd.DataFrame(columns=["id_jugador","nombre","equipo","posicion","id_partido","titular"])
        for indexJug3, rowJug3 in datos_jugadores_partidos_filtrados_visitante_como_local.iterrows():
            id_jugador = rowJug3['id_jugador']
            sustituido_id_jugador = rowJug3['sustituido_por']
            cambio = rowJug3['cambio']
            amarillas = rowJug3['amarilla']
            goles = rowJug3['goles']
            asistencias = rowJug3['asistencias']
            lesion = rowJug3['lesion']
            id_partido_actual = rowJug3['id_partido']
            titular_actual = rowJug3['titular']


            #nombre del jugador que sale
            resultado = jugadores.loc[(jugadores['id_jugador'] == id_jugador) ]               
            if not resultado.empty:
                nombre = resultado['nombre'].values[0]


            #equipo del que sale
            resultado = jugadores.loc[(jugadores['id_jugador'] == id_jugador) ]               
            if not resultado.empty:
                id_equipo_jugador = resultado['id_equipo'].values[0]
            else:
                print(f"No se encontro en nombre")


            #buscamos posicion del que sale
            resultado = jugadores.loc[(jugadores['id_jugador'] == id_jugador) ]               
            if not resultado.empty:
                posicion = resultado['posicion'].values[0]
            else:
                print(f"No se encontro en busqueda posicion")




            if id_equipo_jugador==id_equipo_visitante:
                if titular_actual==1:
                    dataframe_datos_totales_jugadores_visitante_local.loc[len(dataframe_datos_totales_jugadores_visitante_local)]=[id_jugador,nombre,id_equipo_jugador,posicion,id_partido_actual,titular_actual]


                    indice_anterior = datos_jugadores_partidos_filtrados_visitante_como_local.index.get_loc(indexJug3) - 1
                    while indice_anterior >= 0:
                        fila_anterior = datos_jugadores_partidos_filtrados_visitante_como_local.iloc[indice_anterior]
                        indice_actual = valores_unicos_partidos.index(id_partido_actual)
                        indice_revisado = valores_unicos_partidos.index(fila_anterior['id_partido'])

                        if indice_actual-1==indice_revisado:
                            if fila_anterior['id_jugador'] == id_jugador:
                                titular_anterior = fila_anterior['titular']
                                if titular_anterior != titular_actual:
                                    if posicion=="Defensa":
                                        contador_visitante_cambios_alineacion_defensa[1]=contador_visitante_cambios_alineacion_defensa[1]+1
                                    elif posicion=="Centrocampista":
                                        contador_visitante_cambios_alineacion_centrocampista[1]=contador_visitante_cambios_alineacion_centrocampista[1]+1
                                    elif posicion=="Delantero":
                                        contador_visitante_cambios_alineacion_delantero[1]=contador_visitante_cambios_alineacion_delantero[1]+1
                                    '''if id_equipo_jugador==13:
                                        print(f"{id_partido_actual}: equipo: {id_equipo_jugador} El jugador con id {nombre} diferente")'''
                                break

                        if indice_anterior==0:
                            if posicion=="Defensa":
                                contador_visitante_cambios_alineacion_defensa[1]=contador_visitante_cambios_alineacion_defensa[1]+1
                            elif posicion=="Centrocampista":
                                contador_visitante_cambios_alineacion_centrocampista[1]=contador_visitante_cambios_alineacion_centrocampista[1]+1
                            elif posicion=="Delantero":
                                contador_visitante_cambios_alineacion_delantero[1]=contador_visitante_cambios_alineacion_delantero[1]+1
                            '''if id_equipo_jugador==13:
                                print(f"{id_partido_actual}: equipo: {id_equipo_jugador} El jugador con id {nombre} titular nuevo")'''


                        indice_anterior -= 1


         
            


            if cambio>0 and sustituido_id_jugador>0 and id_equipo_jugador==id_equipo_visitante:





                #buscamos posicion del que entra
                resultado = jugadores.loc[(jugadores['id_jugador'] == sustituido_id_jugador) ]               
                if not resultado.empty:
                    posicion_sustituto = resultado['posicion'].values[0]
                else:
                    #print(f"No se encontro en busqueda posicion")
                    posicion_sustituto="No encontrada"
                

                #nombre del que entra
                resultado = jugadores.loc[(jugadores['id_jugador'] == sustituido_id_jugador) ]               
                if not resultado.empty:
                    nombreEntra = resultado['nombre'].values[0]
                else:
                    print(f"No se encontro en nombre")


                dataframe_cambios_visitante_local.loc[len(dataframe_cambios_visitante_local)]=[nombre, nombreEntra,posicion,posicion_sustituto,cambio,goles,asistencias,lesion,amarillas]





                #minutos analisis cambio
                if cambio<=45:
                    contador_visitante_cambios_antes_descanso[1]=contador_visitante_cambios_antes_descanso[1]+1
                elif cambio<=60 and cambio>45:
                    contador_visitante_cambios_45_60[1]=contador_visitante_cambios_45_60[1]+1   
                elif cambio<=75 and cambio>60:
                    contador_visitante_cambios_61_75[1]=contador_visitante_cambios_61_75[1]+1 
                else:
                    contador_visitante_cambios_76_final[1]=contador_visitante_cambios_76_final[1]+1 




                #posiciones analisis cambios
                if posicion=="Delantero" and posicion_sustituto=="Defensa":
                    contador_visitante_cambios_delanteros_a_defensas[1]=contador_visitante_cambios_delanteros_a_defensas[1]+1
                elif posicion=="Delantero" and posicion_sustituto=="Centrocampista":
                    contador_visitante_cambios_delanteros_a_centrocampistas[1]=contador_visitante_cambios_delanteros_a_centrocampistas[1]+1               
                elif posicion=="Defensa" and posicion_sustituto=="Centrocampista":
                    contador_visitante_cambios_defensas_a_centrocampistas[1]=contador_visitante_cambios_defensas_a_centrocampistas[1]+1  
                elif posicion=="Defensa" and posicion_sustituto=="Delantero":
                    contador_visitante_cambios_defensas_a_delanteros[1]=contador_visitante_cambios_defensas_a_delanteros[1]+1 
                elif posicion=="Centrocampista" and posicion_sustituto=="Delantero":
                    contador_visitante_cambios_centrocampistas_a_delanteros[1]=contador_visitante_cambios_centrocampistas_a_delanteros[1]+1       
                elif posicion=="Centrocampista" and posicion_sustituto=="Defensa":
                    contador_visitante_cambios_centrocampistas_a_defensas[1]=contador_visitante_cambios_centrocampistas_a_defensas[1]+1    




                #otros campos
                if amarillas>0:
                    contador_visitante_cambios_amarillas[1]=contador_visitante_cambios_amarillas[1] +1
                if goles>0:
                    contador_visitante_cambios_goleadores[1]=contador_visitante_cambios_goleadores[1] +1
                if asistencias>0:
                    contador_visitante_cambios_asistentes[1]=contador_visitante_cambios_asistentes[1] +1
                if lesion>0:
                    contador_visitante_cambios_lesionados[1]=contador_visitante_cambios_lesionados[1] +1


                media_visitante_cambio_minutos[1]=media_visitante_cambio_minutos[1]+cambio



        dataframe_cambios_visitante_local.to_csv('csv/estadisticasCambiosVisitanteLocal.csv', index=False) 
        dataframe_datos_totales_jugadores_visitante_local.to_csv('csv/titulVisitanteLocal.csv', index=False)


        
   
        




        '''
        print(contador_local_cambios_alineacion_defensa[0])
        print(contador_local_cambios_alineacion_centrocampista[0])
        print(contador_local_cambios_alineacion_delantero[0])
        print(contador_local_cambios_alineacion_defensa[1])
        print(contador_local_cambios_alineacion_centrocampista[1])
        print(contador_local_cambios_alineacion_delantero[1])
        print("\n")
        print(contador_visitante_cambios_alineacion_defensa[0])
        print(contador_visitante_cambios_alineacion_centrocampista[0])
        print(contador_visitante_cambios_alineacion_delantero[0])
        print(contador_visitante_cambios_alineacion_defensa[1])
        print(contador_visitante_cambios_alineacion_centrocampista[1])
        print(contador_visitante_cambios_alineacion_delantero[1])
        '''









        media_local_cambio_minutos[0]=calculosSin100(media_local_cambio_minutos[0],contador_local_cambios[0])
        media_local_cambio_minutos[1]=calculosSin100(media_local_cambio_minutos[1],contador_local_cambios[1])
        media_visitante_cambio_minutos[0]=calculosSin100(media_visitante_cambio_minutos[0],contador_visitante_cambios[0])
        media_visitante_cambio_minutos[1]=calculosSin100(media_visitante_cambio_minutos[1],contador_visitante_cambios[1])



        proporcion_local_cambios_amarillas[0]=calculosSin100(contador_local_cambios_amarillas[0],contador_local_partidos[0])
        proporcion_local_cambios_amarillas[1]=calculosSin100(contador_local_cambios_amarillas[1],contador_local_partidos[1])
        proporcion_visitante_cambios_amarillas[0]=calculosSin100(contador_visitante_cambios_amarillas[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_amarillas[1]=calculosSin100(contador_visitante_cambios_amarillas[1],contador_visitante_partidos[1])


        proporcion_local_cambios_lesionados[0]=calculosSin100(contador_local_cambios_lesionados[0],contador_local_partidos[0])
        proporcion_local_cambios_lesionados[1]=calculosSin100(contador_local_cambios_lesionados[1],contador_local_partidos[1])
        proporcion_visitante_cambios_lesionados[0]=calculosSin100(contador_visitante_cambios_lesionados[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_lesionados[1]=calculosSin100(contador_visitante_cambios_lesionados[1],contador_visitante_partidos[1])


        proporcion_local_cambios_goleadores[0]=calculosSin100(contador_local_cambios_goleadores[0],contador_local_partidos[0])
        proporcion_local_cambios_goleadores[1]=calculosSin100(contador_local_cambios_goleadores[1],contador_local_partidos[1])
        proporcion_visitante_cambios_goleadores[0]=calculosSin100(contador_visitante_cambios_goleadores[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_goleadores[1]=calculosSin100(contador_visitante_cambios_goleadores[1],contador_visitante_partidos[1])


        proporcion_local_cambios_asistentes[0]=calculosSin100(contador_local_cambios_asistentes[0],contador_local_partidos[0])
        proporcion_local_cambios_asistentes[1]=calculosSin100(contador_local_cambios_asistentes[1],contador_local_partidos[1])
        proporcion_visitante_cambios_asistentes[0]=calculosSin100(contador_visitante_cambios_asistentes[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_asistentes[1]=calculosSin100(contador_visitante_cambios_asistentes[1],contador_visitante_partidos[1])


        proporcion_local_cambios_alineacion_defensa[0]=calculosSin100(contador_local_cambios_alineacion_defensa[0],contador_local_partidos[0])
        proporcion_local_cambios_alineacion_defensa[1]=calculosSin100(contador_local_cambios_alineacion_defensa[1],contador_local_partidos[1])
        proporcion_visitante_cambios_alineacion_defensa[0]=calculosSin100(contador_visitante_cambios_alineacion_defensa[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_alineacion_defensa[1]=calculosSin100(contador_visitante_cambios_alineacion_defensa[1],contador_visitante_partidos[1])


        proporcion_local_cambios_alineacion_centrocampista[0]=calculosSin100(contador_local_cambios_alineacion_centrocampista[0],contador_local_partidos[0])
        proporcion_local_cambios_alineacion_centrocampista[1]=calculosSin100(contador_local_cambios_alineacion_centrocampista[1],contador_local_partidos[1])
        proporcion_visitante_cambios_alineacion_centrocampista[0]=calculosSin100(contador_visitante_cambios_alineacion_centrocampista[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_alineacion_centrocampista[1]=calculosSin100(contador_visitante_cambios_alineacion_centrocampista[1],contador_visitante_partidos[1])


        proporcion_local_cambios_alineacion_delantero[0]=calculosSin100(contador_local_cambios_alineacion_delantero[0],contador_local_partidos[0])
        proporcion_local_cambios_alineacion_delantero[1]=calculosSin100(contador_local_cambios_alineacion_delantero[1],contador_local_partidos[1])
        proporcion_visitante_cambios_alineacion_delantero[0]=calculosSin100(contador_visitante_cambios_alineacion_delantero[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_alineacion_delantero[1]=calculosSin100(contador_visitante_cambios_alineacion_delantero[1],contador_visitante_partidos[1])


        proporcion_local_cambios_delanteros_a_defensas[0]=calculosSin100(contador_local_cambios_delanteros_a_defensas[0],contador_local_partidos[0])
        proporcion_local_cambios_delanteros_a_defensas[1]=calculosSin100(contador_local_cambios_delanteros_a_defensas[1],contador_local_partidos[1])
        proporcion_visitante_cambios_delanteros_a_defensas[0]=calculosSin100(contador_visitante_cambios_delanteros_a_defensas[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_delanteros_a_defensas[1]=calculosSin100(contador_visitante_cambios_delanteros_a_defensas[1],contador_visitante_partidos[1])


        proporcion_local_cambios_delanteros_a_centrocampistas[0]=calculosSin100(contador_local_cambios_delanteros_a_centrocampistas[0],contador_local_partidos[0])
        proporcion_local_cambios_delanteros_a_centrocampistas[1]=calculosSin100(contador_local_cambios_delanteros_a_centrocampistas[1],contador_local_partidos[1])
        proporcion_visitante_cambios_delanteros_a_centrocampistas[0]=calculosSin100(contador_visitante_cambios_delanteros_a_centrocampistas[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_delanteros_a_centrocampistas[1]=calculosSin100(contador_visitante_cambios_delanteros_a_centrocampistas[1],contador_visitante_partidos[1])



        proporcion_local_cambios_defensas_a_centrocampistas[0]=calculosSin100(contador_local_cambios_defensas_a_centrocampistas[0],contador_local_partidos[0])
        proporcion_local_cambios_defensas_a_centrocampistas[1]=calculosSin100(contador_local_cambios_defensas_a_centrocampistas[1],contador_local_partidos[1])
        proporcion_visitante_cambios_defensas_a_centrocampistas[0]=calculosSin100(contador_visitante_cambios_defensas_a_centrocampistas[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_defensas_a_centrocampistas[1]=calculosSin100(contador_visitante_cambios_defensas_a_centrocampistas[1],contador_visitante_partidos[1])


        proporcion_local_cambios_defensas_a_delanteros[0]=calculosSin100(contador_local_cambios_defensas_a_delanteros[0],contador_local_partidos[0])
        proporcion_local_cambios_defensas_a_delanteros[1]=calculosSin100(contador_local_cambios_defensas_a_delanteros[1],contador_local_partidos[1])
        proporcion_visitante_cambios_defensas_a_delanteros[0]=calculosSin100(contador_visitante_cambios_defensas_a_delanteros[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_defensas_a_delanteros[1]=calculosSin100(contador_visitante_cambios_defensas_a_delanteros[1],contador_visitante_partidos[1])



        proporcion_local_cambios_centrocampistas_a_delanteros[0]=calculosSin100(contador_local_cambios_centrocampistas_a_delanteros[0],contador_local_partidos[0])
        proporcion_local_cambios_centrocampistas_a_delanteros[1]=calculosSin100(contador_local_cambios_centrocampistas_a_delanteros[1],contador_local_partidos[1])
        proporcion_visitante_cambios_centrocampistas_a_delanteros[0]=calculosSin100(contador_visitante_cambios_centrocampistas_a_delanteros[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_centrocampistas_a_delanteros[1]=calculosSin100(contador_visitante_cambios_centrocampistas_a_delanteros[1],contador_visitante_partidos[1])


        proporcion_local_cambios_centrocampistas_a_defensas[0]=calculosSin100(contador_local_cambios_centrocampistas_a_defensas[0],contador_local_partidos[0])
        proporcion_local_cambios_centrocampistas_a_defensas[1]=calculosSin100(contador_local_cambios_centrocampistas_a_defensas[1],contador_local_partidos[1])
        proporcion_visitante_cambios_centrocampistas_a_defensas[0]=calculosSin100(contador_visitante_cambios_centrocampistas_a_defensas[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_centrocampistas_a_defensas[1]=calculosSin100(contador_visitante_cambios_centrocampistas_a_defensas[1],contador_visitante_partidos[1])


        proporcion_local_cambios_antes_descanso[0]=calculosSin100(contador_local_cambios_antes_descanso[0],contador_local_partidos[0])
        proporcion_local_cambios_antes_descanso[1]=calculosSin100(contador_local_cambios_antes_descanso[1],contador_local_partidos[1])
        proporcion_visitante_cambios_antes_descanso[0]=calculosSin100(contador_visitante_cambios_antes_descanso[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_antes_descanso[1]=calculosSin100(contador_visitante_cambios_antes_descanso[1],contador_visitante_partidos[1])

        proporcion_local_cambios_45_60[0]=calculosSin100(contador_local_cambios_45_60[0],contador_local_partidos[0])
        proporcion_local_cambios_45_60[1]=calculosSin100(contador_local_cambios_45_60[1],contador_local_partidos[1])
        proporcion_visitante_cambios_45_60[0]=calculosSin100(contador_visitante_cambios_45_60[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_45_60[1]=calculosSin100(contador_visitante_cambios_45_60[1],contador_visitante_partidos[1])

        proporcion_local_cambios_61_75[0]=calculosSin100(contador_local_cambios_61_75[0],contador_local_partidos[0])
        proporcion_local_cambios_61_75[1]=calculosSin100(contador_local_cambios_61_75[1],contador_local_partidos[1])
        proporcion_visitante_cambios_61_75[0]=calculosSin100(contador_visitante_cambios_61_75[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_61_75[1]=calculosSin100(contador_visitante_cambios_61_75[1],contador_visitante_partidos[1])

        proporcion_local_cambios_76_final[0]=calculosSin100(contador_local_cambios_76_final[0],contador_local_partidos[0])
        proporcion_local_cambios_76_final[1]=calculosSin100(contador_local_cambios_76_final[1],contador_local_partidos[1])
        proporcion_visitante_cambios_76_final[0]=calculosSin100(contador_visitante_cambios_76_final[0],contador_visitante_partidos[0])
        proporcion_visitante_cambios_76_final[1]=calculosSin100(contador_visitante_cambios_76_final[1],contador_visitante_partidos[1])


        dataframe_indicadores_equipos_prepartido.loc[len(dataframe_indicadores_equipos_prepartido)]=[
            id_indicadores_equipo_prepartido,
            id_partido,
            porcentaje_local_ganados[0],
            porcentaje_local_ganados[1],
            porcentaje_local_empatados[0],
            porcentaje_local_empatados[1],
            porcentaje_local_perdidos[0],
            porcentaje_local_perdidos[1],
            porcentaje_visitante_ganados[0],
            porcentaje_visitante_ganados[1],
            porcentaje_visitante_empatados[0],
            porcentaje_visitante_empatados[1],
            porcentaje_visitante_perdidos[0],
            porcentaje_visitante_perdidos[1],
            proporcion_local_puntos[0],
            proporcion_local_puntos[1],
            proporcion_visitante_puntos[0],
            proporcion_visitante_puntos[1],
            porcentaje_local_mas15[0],
            porcentaje_local_mas15[1],
            porcentaje_visitante_mas15[0],
            porcentaje_visitante_mas15[1],
            porcentaje_local_mas25[0],
            porcentaje_local_mas25[1],
            porcentaje_visitante_mas25[0],
            porcentaje_visitante_mas25[1],
            porcentaje_local_mas35[0],
            porcentaje_local_mas35[1],
            porcentaje_visitante_mas35[0],
            porcentaje_visitante_mas35[1],
            porcentaje_local_mas45[0],
            porcentaje_local_mas45[1],
            porcentaje_visitante_mas45[0],
            porcentaje_visitante_mas45[1],
            proporcion_local_goles_totales[0],
            proporcion_local_goles_totales[1],
            proporcion_local_goles_marcados[0],
            proporcion_local_goles_marcados[1],
            proporcion_local_goles_encajados[0],
            proporcion_local_goles_encajados[1],
            proporcion_visitante_goles_totales[0],
            proporcion_visitante_goles_totales[1],
            proporcion_visitante_goles_marcados[0],
            proporcion_visitante_goles_marcados[1],
            proporcion_visitante_goles_encajados[0],
            proporcion_visitante_goles_encajados[1],
            porcentaje_local_mas05_marcados[0],
            porcentaje_local_mas05_marcados[1],
            porcentaje_local_mas15_marcados[0],
            porcentaje_local_mas15_marcados[1],
            porcentaje_local_mas25_marcados[0],
            porcentaje_local_mas25_marcados[1],
            porcentaje_local_mas05_encajados[0],
            porcentaje_local_mas05_encajados[1],
            porcentaje_local_mas15_encajados[0],
            porcentaje_local_mas15_encajados[1],
            porcentaje_local_mas25_encajados[0],
            porcentaje_local_mas25_encajados[1],
            porcentaje_visitante_mas05_marcados[0],
            porcentaje_visitante_mas05_marcados[1],
            porcentaje_visitante_mas15_marcados[0],
            porcentaje_visitante_mas15_marcados[1],
            porcentaje_visitante_mas25_marcados[0],
            porcentaje_visitante_mas25_marcados[1],
            porcentaje_visitante_mas05_encajados[0],
            porcentaje_visitante_mas05_encajados[1],
            porcentaje_visitante_mas15_encajados[0],
            porcentaje_visitante_mas15_encajados[1],
            porcentaje_visitante_mas25_encajados[0],
            porcentaje_visitante_mas25_encajados[1],
            proporcion_local_amarillas[0],
            proporcion_local_amarillas[1],
            proporcion_visitante_amarillas[0],
            proporcion_visitante_amarillas[1],
            proporcion_local_rojas[0],
            proporcion_local_rojas[1],
            proporcion_visitante_rojas[0],
            proporcion_visitante_rojas[1],
            proporcion_local_cambios[0],
            proporcion_local_cambios[1],
            proporcion_visitante_cambios[0],
            proporcion_visitante_cambios[1],
            proporcion_local_posesion[0],
            proporcion_local_posesion[1],
            proporcion_visitante_posesion[0],
            proporcion_visitante_posesion[1],
            proporcion_local_total_tiros[0],
            proporcion_local_total_tiros[1],
            proporcion_visitante_total_tiros[0],
            proporcion_visitante_total_tiros[1],
            proporcion_local_corners_afavor[0],
            proporcion_local_corners_afavor[1],
            proporcion_visitante_corners_afavor[0],
            proporcion_visitante_corners_afavor[1],
            proporcion_local_corners_encontra[0],
            proporcion_local_corners_encontra[1],
            proporcion_visitante_corners_encontra[0],
            proporcion_visitante_corners_encontra[1],
            proporcion_local_cambios_lesionados[0],
            proporcion_local_cambios_lesionados[1],
            proporcion_visitante_cambios_lesionados[0],
            proporcion_visitante_cambios_lesionados[1],
            proporcion_local_cambios_amarillas[0],
            proporcion_local_cambios_amarillas[1],
            proporcion_visitante_cambios_amarillas[0],
            proporcion_visitante_cambios_amarillas[1],
            proporcion_local_cambios_goleadores[0],
            proporcion_local_cambios_goleadores[1],
            proporcion_visitante_cambios_goleadores[0],
            proporcion_visitante_cambios_goleadores[1],
            proporcion_local_cambios_asistentes[0],
            proporcion_local_cambios_asistentes[1],
            proporcion_visitante_cambios_asistentes[0],
            proporcion_visitante_cambios_asistentes[1],
            media_local_cambio_minutos[0],
            media_local_cambio_minutos[1],
            media_visitante_cambio_minutos[0],
            media_visitante_cambio_minutos[1],
            proporcion_local_cambios_delanteros_a_centrocampistas[0],
            proporcion_local_cambios_delanteros_a_centrocampistas[1],
            proporcion_visitante_cambios_delanteros_a_centrocampistas[0],
            proporcion_visitante_cambios_delanteros_a_centrocampistas[1],
            proporcion_local_cambios_delanteros_a_defensas[0],
            proporcion_local_cambios_delanteros_a_defensas[1],
            proporcion_visitante_cambios_delanteros_a_defensas[0],
            proporcion_visitante_cambios_delanteros_a_defensas[1],
            proporcion_local_cambios_centrocampistas_a_delanteros[0],
            proporcion_local_cambios_centrocampistas_a_delanteros[1],
            proporcion_visitante_cambios_centrocampistas_a_delanteros[0],
            proporcion_visitante_cambios_centrocampistas_a_delanteros[1],
            proporcion_local_cambios_centrocampistas_a_defensas[0],
            proporcion_local_cambios_centrocampistas_a_defensas[1],
            proporcion_visitante_cambios_centrocampistas_a_defensas[0],
            proporcion_visitante_cambios_centrocampistas_a_defensas[1],
            proporcion_local_cambios_defensas_a_delanteros[0],
            proporcion_local_cambios_defensas_a_delanteros[1],
            proporcion_visitante_cambios_defensas_a_delanteros[0],
            proporcion_visitante_cambios_defensas_a_delanteros[1],
            proporcion_local_cambios_defensas_a_centrocampistas[0],
            proporcion_local_cambios_defensas_a_centrocampistas[1],
            proporcion_visitante_cambios_defensas_a_centrocampistas[0],
            proporcion_visitante_cambios_defensas_a_centrocampistas[1],
            proporcion_local_cambios_antes_descanso[0],
            proporcion_local_cambios_antes_descanso[1],
            proporcion_visitante_cambios_antes_descanso[0],
            proporcion_visitante_cambios_antes_descanso[1],
            proporcion_local_cambios_45_60[0],
            proporcion_local_cambios_45_60[1],
            proporcion_visitante_cambios_45_60[0],
            proporcion_visitante_cambios_45_60[1],
            proporcion_local_cambios_61_75[0],
            proporcion_local_cambios_61_75[1],
            proporcion_visitante_cambios_61_75[0],
            proporcion_visitante_cambios_61_75[1],
            proporcion_local_cambios_76_final[0],
            proporcion_local_cambios_76_final[1],
            proporcion_visitante_cambios_76_final[0],
            proporcion_visitante_cambios_76_final[1],
            proporcion_local_cambios_alineacion_defensa[0],
            proporcion_local_cambios_alineacion_defensa[1],
            proporcion_visitante_cambios_alineacion_defensa[0],
            proporcion_visitante_cambios_alineacion_defensa[1],
            proporcion_local_cambios_alineacion_centrocampista[0],
            proporcion_local_cambios_alineacion_centrocampista[1],
            proporcion_visitante_cambios_alineacion_centrocampista[0],
            proporcion_visitante_cambios_alineacion_centrocampista[1],
            proporcion_local_cambios_alineacion_delantero[0],
            proporcion_local_cambios_alineacion_delantero[1],
            proporcion_visitante_cambios_alineacion_delantero[0],
            proporcion_visitante_cambios_alineacion_delantero[1]


        ]
        id_indicadores_equipo_prepartido=id_indicadores_equipo_prepartido+1

dataframe_indicadores_equipos_prepartido.to_csv('csv/indicadoresEquipoPrepartido.csv', index=False) 

