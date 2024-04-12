import os
import requests
from os import path
import os.path
import csv_tools
import data_collect as dc


def store_file(ruta,attrs):
    if (not path.exists(ruta)):
        os.mkdir(ruta)

    return

def open_file(ruta,attrs):
    
    return

def get_all_data():
    session = requests.session()
    leagues = ['bundesliga','primera','premier','serie_a']
    seasons = range(2016,2020)
    RUTA = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data')
    print(RUTA)
    for league in leagues:
        RUTA_LEAGUE = os.path.join(RUTA,league)
        for season in seasons:
            RUTA_SEASON = os.path.join(RUTA_LEAGUE,str(season))
            if (not path.exists(RUTA_SEASON)):
                os.makedirs(RUTA_SEASON) 
            teams = dc.getTeamsFromLeague(league,season,session)
            for team in teams:
                for team2 in teams:
                    if team == team2:
                        continue
                    storeAlineacion(RUTA_SEASON,team,team2,season,session)

               #storeTeamInfo(RUTA_SEASON, team,league,season,session)
            #storeTeamsFromLeague(RUTA_SEASON,league,season,session)
            
def storeTeamsFromLeague(ruta,league,season,session):
    data = dc.getTeamsFromLeague(league,season,session)
    filename = os.path.join(ruta,'teams.csv')
    csv_tools.writeListOfObjectsToCSV(data,filename)
    return

def storeTeamInfo(ruta,team,league,season,sesion):
    data = dc.getTeamInfo(team,season,sesion)
    ruta = os.path.join(ruta,'teamInfo')
    if (not path.exists(ruta)):
        os.mkdir(ruta) 
    filename = os.path.join(ruta, team + '.csv')
    csv_tools.writeListOfObjectsToCSV(data,filename)
    return

def storeAlineacion(ruta,teamLocal,teamVisitante,season,sesion):
    data,data2 = dc.getAlineacion(teamLocal,teamVisitante,season,sesion)
    ruta = os.path.join(ruta,'alineacion')
    if (not path.exists(ruta)):
        os.mkdir(ruta) 
    filename = os.path.join(ruta,teamLocal + '_' + teamVisitante + '.csv')
    csv_tools.writeListOfObjectsToCSV(data,filename)
    return

def storeClasificacion(ruta,league,season,group,jornada,sesion):
    data = dc.getClasificacion(league,season,group,jornada,sesion)
    ruta = os.path.join(ruta,'clasificacion')
    if (not path.exists(ruta)):
        os.mkdir(ruta) 
    filename = os.path.join(ruta,group + '_' + jornada + '.csv')
    csv_tools.writeListOfObjectsToCSV(data,filename)
    return

def storePartidos(ruta,league,season,group,sesion):
    data = dc.getPartidos(league,season,group,sesion)
    ruta = os.path.join(ruta,'partidos')
    if (not path.exists(ruta)):
        os.mkdir(ruta) 
    filename = os.path.join(ruta,group + '.csv')
    csv_tools.writeListOfObjectsToCSV(data,filename)
    return

def storePlantilla(ruta,team,season,sesion):
    data = dc.getPlantilla(team,season,sesion)
    ruta = os.path.join(ruta,'plantilla')
    if (not path.exists(ruta)):
        os.mkdir(ruta) 
    filename = os.path.join(ruta,team + '.csv')
    csv_tools.writeListOfObjectsToCSV(data,filename)
    return

def storeAllMatchesByTeam(ruta, team, season,sesion):
    data = dc.getAllMatchesByTeam(team,season,sesion)
    ruta = os.path.join(ruta,'allPartidos')
    if (not path.exists(ruta)):
        os.mkdir(ruta) 
    filename = os.path.join(ruta,team + '.csv')
    csv_tools.writeListOfObjectsToCSV(data,filename)
    return






def getTeamsFromLeague(league,season,sesion):
    ruta = os.path.join(os.path.join(RUTA,league),season)
    return teams

#Recupera informacion de un equipo en una temporada
def getTeamInfo(team,season,sesion):

    return equipo
    
#Recupera la alineacion de cada equipo para una jornada
def getAlineacion(teamLocal, teamVisitante, season,sesion):
    return alineacion_local, alineacion_visitante

#Recupera la clasificacion de un equipo en una jornada 
def getClasificacion(league,season,group,jornada,sesion):
   
    return lista

#Recupera la informacion de los partidos de una liga
def getPartidos(league,season,group,sesion):

    return lista

#recupera la plantilla de un equipo de una liga
def getPlantilla(team,season,sesion):
    return lista

#recupera la lista de partidos de un equipo en una temporada
def getAllMatchesByTeam(team, season,sesion):
    return lista

#TODO Not implemented yet
def getAllLeagues():

    return lista

def getAllTeamsInfo(league,season,teams_dict,sesion):

    return


get_all_data()