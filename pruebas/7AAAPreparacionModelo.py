
import pandas as pd



#funciones
def evaluar_resultado(row):
    if row['resultado_local'] > row['resultado_visitante']:
        return '1'
    elif row['resultado_local'] == row['resultado_visitante']:
        return 'X'
    else:
        return '2'

# liga y temporada a analizar
ligas=['bundesliga']
temporadas=[2022]


# para cada liga y temporada, se convierten los indicadores
for liga in ligas:
    for temporada in temporadas:
        print("Procesando: "+liga+"-"+str(temporada))

        #cargamos csv
        indicadores_equipos_historico = pd.read_csv('csv/indicadoresEquipoHistorico-'+liga+'-'+str(temporada)+'.csv')
        datos_partidos_jugados = pd.read_csv('csv/datosPartidosJugados-'+liga+'-'+str(temporada)+'.csv')
        datos_jugadores_partidos = pd.read_csv('csv/datosJugadoresPartidos-'+liga+'-'+str(temporada)+'.csv')
        partidos = pd.read_csv('csv/partidos-'+liga+'-'+str(temporada)+'.csv')

        if 'resultado_local' not in indicadores_equipos_historico.columns:
            indicadores_equipos_historico['resultado_local'] = None
        if 'resultado_visitante' not in indicadores_equipos_historico.columns:
            indicadores_equipos_historico['resultado_visitante'] = None
        if 'resultado_partido' not in indicadores_equipos_historico.columns:
            indicadores_equipos_historico['resultado_partido'] = None



        # Hacer un merge para añadir la columna 'jornada' a `indicadores_equipos_historico`
        indicadores_equipos_historico = indicadores_equipos_historico.merge(partidos[['id_partido', 'jornada']], on='id_partido', how='left')

        # Filtrar las filas donde la jornada es mayor a 9
        indicadores_equipos_historico = indicadores_equipos_historico[indicadores_equipos_historico['jornada'] > 9]




        # recorremos los indicadores
        for index, row in indicadores_equipos_historico.iterrows():
            id_partido = row['id_partido']
            resultado = datos_partidos_jugados.loc[(datos_partidos_jugados['id_partido'] == id_partido) ]               
            if not resultado.empty:
                resultado_local = resultado['resultado_local'].values[0]
                resultado_visitante = resultado['resultado_visitante'].values[0]
                indicadores_equipos_historico.at[index, 'resultado_local'] = resultado_local
                indicadores_equipos_historico.at[index, 'resultado_visitante'] = resultado_visitante
                if resultado_local>resultado_visitante:
                    indicadores_equipos_historico.at[index, 'resultado_partido'] = '1'
                elif resultado_local<resultado_visitante:
                    indicadores_equipos_historico.at[index, 'resultado_partido'] = '2'
                else:
                    indicadores_equipos_historico.at[index, 'resultado_partido'] = 'X'


            else:
                #print(f"No se encontro en busqueda posicion")
                posicion_sustituto="No encontrada"

        



        # guardamos los indicadores listos para utilizar por el modelo
        indicadores_equipos_historico.to_csv('csv/indicadoresEquipoHistoricoModelo-'+liga+'-'+str(temporada)+'.csv', index=False) 
        # vaciamos
        indicadores_equipos_historico = indicadores_equipos_historico.drop(indicadores_equipos_historico.index) 
