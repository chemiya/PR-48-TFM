#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import request_retry as req
import csv
import locale
from datetime import datetime
from bs4 import BeautifulSoup

URL_BASE="https://www.resultados-futbol.com/"
locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')

#====================================#
#============== CLASES ==============#
#====================================#

class Equipo:
    temporada=""
    foto=""
    nombre=""
    estadio=""
    entrenador=""
    ubicacion=""

class Alineacion:
    temporada=""
    jugador=""
    amarilla=""
    roja=""
    gol=""
    cambio=""
    estado=""
    equipo=""
    jornada=""
    lesion=""
    asistencia=""

class EquipoClasificaion:
    temporada=""
    jornada=""
    posicion=""
    nombre=""
    pjugados=""
    ganados=""
    empatados=""
    perdidos=""
    gfavor=""
    gcontra=""
    puntos=""

class Partido:
    temporada=""
    jornada=""
    fecha=""
    local=""
    foto_local=""
    visitante=""
    foto_visitante=""
    resultado=""

class Jugador:
	temporada=""
	foto=""
	pais=""
	equipo=""
	nombre=""
	edad=""
	goles=""
	rojas=""
	amarillas=""
	dorsal=""
	altura=""
	peso=""
	posicion=""

class PartidosEquipo:
    liga=''
    fecha=''
    estado=''
    local=''
    visitante=''
    resultado=''

#=====================================#
#============= FUNCIONES =============#
#=====================================#

#Recupera los ID de los equipos para una liga dada 
def getTeamsFromLeague(league,season,session):
    teams = dict()
    url = URL_BASE + league + str(season)

    try:
        page = session.get(url)
    except Exception as x:
        raise SystemExit(x)

    soup=BeautifulSoup(page.content,'html.parser')
    teamList = soup.find_all('li',class_='shield')

    for team in teamList:
        clave = team.find('a').attrs['href']
        clave = clave.strip('/')
    
        valor = team.find('img').attrs['title']

        teams[clave] = valor

    return teams

#Recupera informacion de un equipo en una temporada
def getTeamInfo(team,season,session):
    equipo = Equipo()
    url = URL_BASE + team + '/' + str(season)

    try:
        page = session.get(url)
    except Exception as x:
        raise SystemExit(x)

    soup=BeautifulSoup(page.content,'html.parser')
    
    nombre=soup.find('div', id='titlehc')
    nombre=nombre.find('h1').attrs['title']

    escudo=soup.find('div',id='previewArea')
    escudo=escudo.find('img').attrs['src']

    datos=soup.find('div',id='titlehc')

    entrenador=datos.find_all('p')
    entrenador=entrenador[0].find('span').string

    estadio=soup.find('div',class_='contentitem bi-stadium')
    estadio=estadio.find_all('li')
    estadio=estadio[0].find_all('span')
    estadio=estadio[1].string

    ubicacion=soup.find('div',class_='text')
    ubicacion=ubicacion.find_all('ul')
    #ubicacion=ubicacion[0].find_all('li')
    #ubicacion=ubicacion[4].find_all('span')
    #ubicacion=ubicacion[1].string

    equipo.temporada = season
    equipo.foto = escudo
    equipo.nombre = nombre
    equipo.estadio = estadio
    equipo.entrenador = entrenador
    equipo.ubicacion = "revisar"

    return equipo
    
#Recupera la alineacion de cada equipo para una jornada
def getAlineacion(teamLocal, teamVisitante, season,session):
    url = URL_BASE + "partido/" + teamLocal + '/' + teamVisitante + '/' + str(season)
    alineacion_local = []
    alineacion_visitante =[]

    try:
        page = session.get(url)
    except Exception as x:
        raise SystemExit(x)

    soup=BeautifulSoup(page.content,'html.parser')

    jornada=soup.find('div',class_='jornada')
    if None is jornada:
        return
    jornada=jornada.string

    #Busqueda de lesiones y asistencias en el equipo local
    local_lesion=soup.find_all('span',class_="left event_4")
    local_asistencias=soup.find_all('span',class_="left event_5")
    
    lesiones_local=[]
    for a in local_lesion:
        nombre=a.find('a')
        lesiones_local.append(nombre.string)

    asistencia_local=[]
    for a in local_asistencias:
        nombre=a.find('a')
        asistencia_local.append(nombre.string)

    #Busqueda de lesiones y asistencias en el equipo visitante
    visitante_lesion=soup.find_all('span',class_="right event_4")
    visitante_asistencia=soup.find_all('span',class_="right event_5")

    lesiones_visitante=[]
    for a in visitante_lesion:
        nombre=a.find('a')
        lesiones_visitante.append(nombre.string)

    asistencia_visitante=[]
    for a in visitante_asistencia:
        nombre=a.find('a')
        asistencia_visitante.append(nombre.string)

    #locales
    try:
        equipo_local=soup.find('div',class_='team team1')
        equipo_local=equipo_local.find_all('li',class_='')
    except:
        raise
    i=0
    for jugador in equipo_local:
        if i<11:
            estado="Titular"
        else:
            estado="Suplente"
        i=i+1

        nombre=jugador.find('h5',class_='align-player')
		
        eventos=jugador.find('div',class_='align-events')
        if None is eventos:
            continue
        if eventos.find('span',class_='flaticon-live-5'):
            amarilla="1"
        else:
            amarilla="0"

        if eventos.find('span',class_='flaticon-goal'):
            gol=eventos.find('span',class_='flaticon-goal')
            if gol.find('b',class_=''):
                gol=gol.find('b',class_='')
                gol=gol.string
            else:
                gol="1"
        else:
            gol="0"

        if eventos.find('span',class_='flaticon-up12'):
            cambio=eventos.find('span',class_='flaticon-up12')
            cambio=cambio.string
        else:
            cambio=""

        if eventos.find('span',class_='flaticon-live-3'):
            roja="1"
        else:
            roja="0"
		
        if eventos.find('span',class_='flaticon-live-4'):
            roja="1"
            amarilla="2"
        
        nombre=nombre.string
        lesion='0'
        for a in lesiones_local:
            if a == nombre:
                lesion='1'
        
        asistencia=0
        for a in asistencia_local:
            if a == nombre:
                asistencia=asistencia+1

        j=Alineacion()
        j.temporada=season
        j.jugador=nombre
        j.estado=estado
        j.amarilla=amarilla
        j.gol=gol
        if cambio!="":
            if cambio[1]=="'":
                j.cambio=cambio[:1]
            else:
                j.cambio=cambio[:2]
        else: 
            j.cambio=cambio
        j.roja=roja
        j.jornada=jornada
        j.equipo=teamLocal
        j.lesion=lesion
        j.asistencia=asistencia
        alineacion_local.append(j)

    #visitantes
    equipo_visitante=soup.find('div',class_='team team2')
    equipo_visitante=equipo_visitante.find_all('li',class_='')
    i=0
    for jugador in equipo_visitante:
        if i<11:
            estado="Titular"
        else:
            estado="Suplente" 
        i=i+1

        nombre=jugador.find('h5',class_='align-player')

        eventos=jugador.find('div',class_='align-events')
        if None is eventos:
            continue
        if eventos.find('span',class_='flaticon-live-5'):
            amarilla="1"
        else:
            amarilla="0"

        if eventos.find('span',class_='flaticon-goal'):
            gol=eventos.find('span',class_='flaticon-goal')
            if gol.find('b',class_=''):
                gol=gol.find('b',class_='')
                gol=gol.string
            else:
                gol="1"
        else:
            gol="0"

        if eventos.find('span',class_='flaticon-up12'):
            cambio=eventos.find('span',class_='flaticon-up12')
            cambio=cambio.string
        else:
            cambio=""

        if eventos.find('span',class_='flaticon-live-3'):
            roja="1"
        else:
            roja="0"

        if eventos.find('span',class_='flaticon-live-4'):
            roja="1"
            amarilla="2"

        nombre=nombre.string
        lesion=0
        for a in lesiones_visitante:
            if a == nombre:
                lesion=1

        asistencia=0
        for a in asistencia_visitante:
            if a == nombre:
                asistencia=asistencia+1

        j=Alineacion()
        j.temporada=season
        j.jugador=nombre
        j.estado=estado
        j.amarilla=amarilla
        j.gol=gol
        if cambio!="":
            if cambio[1]=="'":
                j.cambio=cambio[:1]
            else:
                j.cambio=cambio[:2]
        else: 
            j.cambio=cambio
        j.roja=roja
        j.jornada=jornada
        j.equipo=teamVisitante
        j.lesion=lesion
        j.asistencia=asistencia
        alineacion_visitante.append(j)
    
    return alineacion_local, alineacion_visitante

#Recupera la clasificacion de un equipo en una jornada 
def getClasificacion(league,season,group,jornada,session):
    url = URL_BASE + league + str(season) + '/grupo' + group + '/jornada' + str(jornada)
    lista = []

    try:
        page = session.get(url)
    except Exception as x:
        raise SystemExit(x)

    
    soup=BeautifulSoup(page.content,'html.parser')

    results=soup.find('table',id='tabla2')
    results=results.find('tbody')

    equipos=results.find_all('tr')
    jor='Jornada '+str(jornada)

    for equipo in equipos:
        nombre=equipo.find('a')
        if None in (nombre):
            continue
        nombre=nombre.attrs['href'].split('/')[1]

        puntos=equipo.find(class_='pts')
        puntos=puntos.string

        posicion=equipo.find('th')
        posicion=posicion.string

        pjugados=equipo.find(class_='pj')
        pjugados=pjugados.string

        ganados=equipo.find(class_='win')
        ganados=ganados.string

        empatados=equipo.find(class_='draw')
        empatados=empatados.string

        perdidos=equipo.find(class_='lose')
        perdidos=perdidos.string

        gfavor=equipo.find(class_='f')
        gfavor=gfavor.string

        gcontra=equipo.find(class_='c')
        gcontra=gcontra.string

        j=EquipoClasificaion()
        j.temporada=season
        j.jornada=jor
        j.posicion=posicion
        j.nombre=nombre
        j.puntos=puntos
        j.pjugados=pjugados
        j.ganados=ganados
        j.empatados=empatados
        j.perdidos=perdidos
        j.gfavor=gfavor
        j.gcontra=gcontra
        lista.append(j)
   
    return lista

#Recupera la informacion de los partidos de una liga
def getPartidos(league,season,group,session):
    url = URL_BASE + league + str(season) + '/grupo' + group + '/calendario'
    lista =[]

    try:
        page = session.get(url)
    except Exception as x:
        raise SystemExit(x)
    
    soup=BeautifulSoup(page.content,'html.parser')

    results=soup.find('div',class_="b2col-container col-calendar-content")
    jornadas=results.find_all('div',id='col-resultados')

    for jornada in jornadas:
        jor=jornada.find('div',class_='boxtop')
        jor=str(jor.find('span',class_='titlebox').string)
        jor=jor.split(' ')
        jor=jor[1]
        datos=jornada.find_all('tr')

        for i in datos:
            fecha=i.find('td',class_='fecha')

            local=i.find('td',class_='equipo1')
            visitante=i.find('td',class_='equipo2')

            foto_local=local.find('img').attrs['src']
            foto_visitante=visitante.find('img').attrs['src']

            local = local.find('a').attrs['href'].split('/')[1]
            visitante = visitante.find('a').attrs['href'].split('/')[1]

            resultado=i.find('td',class_='rstd')
            resultado=resultado.find('a',class_='url')
            
            p=Partido()
            p.temporada = season
            p.jornada = jor
            p.fecha=fecha.string
            p.local=local
            p.visitante=  visitante
            p.foto_local= foto_local
            p.foto_visitante= foto_visitante
            if resultado is None:
                p.resultado="Aplazado"
            else:
                p.resultado=resultado.string.strip(' ')
            lista.append(p)

    return lista

#recupera la plantilla de un equipo de una liga
def getPlantilla(team,season,session):
    url = URL_BASE + 'plantilla/' + team + '/' + str(season)
    lista = []

    try:
        page = session.get(url)
    except Exception as x:
        raise SystemExit(x)


    soup=BeautifulSoup(page.content,'html.parser')

    results=soup.find(class_='sdata_table')
    if results is None:
        return
    
    tabla=results.find('tbody')
    if tabla is None:
        return
    
    filas=tabla.find_all('tr')
    if filas is None:
        return

    posicion=""
    for i in filas:
        s=i.find('th').string
        if s in ("Portero","Defensa","Centrocampista","Delantero"):
            posicion=s
            continue

        numero=i.find(class_='num')
        
        foto=i.find(class_='sdata_player_img')
        foto=foto.find('img').attrs['src']

        nombre=i.find(class_='sdata_player_name')

        edad=i.find(class_='birthdate')

        pais=i.find(class_='ori')
        pais=pais.find('img').attrs['src']

        datos=i.find_all('td', class_='dat')
        altura=datos[0]
        peso=datos[1]
        goles=datos[2]
        rojas=datos[3]
        amarillas=datos[4]

        equipo=team

        j=Jugador()
        j.temporada=season
        j.foto=foto
        j.pais=pais
        j.equipo=equipo
        j.nombre=nombre.find('span').string
        j.edad=edad.string

        if goles.string == '-':
            j.goles='0'
        else:
            j.goles=goles.string

        if rojas.string == '-':
            j.rojas='0'
        else:
            j.rojas=rojas.string

        if amarillas.string == '-':
            j.amarillas='0'
        else:
            j.amarillas=amarillas.string

        j.dorsal=numero.string
        j.altura=altura.string
        j.peso=peso.string
        j.posicion=posicion

        lista.append(j)
    return lista

#recupera la lista de partidos de un equipo en una temporada
def getAllMatchesByTeam(team, season,session):
    url = URL_BASE + 'partidos/' + team + '/' + str(season)
    lista =[]

    try:
        page = session.get(url)
    except Exception as x:
        raise SystemExit(x)
    
    soup=BeautifulSoup(page.content,'html.parser')
    #league_information_v3
    info = soup.find('div',id='league_information_v3')

    leagues = info.find_all('div',class_='liga')

    for league in leagues:
        league_name = league.find('div', class_='title')
        league_name = league_name.find('a').attrs['href'].split('/')[-1]
        
        matches = league.find_all('tr')

        for match in matches:
            fecha = match.find('td',class_='time').string
            date_object = datetime.strptime(fecha,'%d %b %y')

            estado = match.find('td',class_='timer')
            estado = estado.find('span').string.strip(' ')

            local = match.find('td',class_='team-home')
            local = local.find('a').string

            visitante = match.find('td',class_='team-away')
            visitante = visitante.find('a').string

            resultado = match.find('td',class_='score')
            resultado = resultado.find('div').string

            o = PartidosEquipo()
            o.liga = league_name
            o.fecha = date_object
            o.estado = estado
            o.local = local
            o.visitante = visitante
            o.resultado = resultado

            lista.append(o)

    return lista

#TODO Not implemented yet
def getAllLeagues():
    url = URL_BASE
    lista =[]

    try:
        page = session.get(url,
        timeout=3)
    except Exception as x:
        raise SystemExit(x)
    
    soup=BeautifulSoup(page.content,'html.parser')
    
    ul = soup.find('ul',id='despla1')

    ul.findAll('li',attrs={'class': None})

    return lista

def getAllTeamsInfo(league,season,teams_dict,session):
    teams = teams_dict.keys()

    teams_output = dict()
    for team in teams:
        output_object = getTeamInfo(team,season,session)
        setattr(output_object,'id_equipo',team)
        setattr(output_object,'nombre',teams_dict[team])
        
        teams_output[team] = output_object

    return teams_output





#Guarda una lista de objetos en formato csv
def writeListOfObjectsToCSV(lista,fileName):
    with open(fileName,'w') as resultFile:
        members = [attr for attr in dir(lista[0]) if not callable(getattr(lista[0], attr)) and not attr.startswith("__")]
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows([members])

        for obj in lista:
            values = [getattr(obj, member) for member in members]
            wr.writerows([values])
    

#date_string = '26 ene 20'
#date_object = datetime.strptime(date_string,'%d %b %y')
#print(date_object)

#lista = getAllMatchesByTeam('Paris-Saint-Germain-Fc','2020')

#print(lista)

#alineacion_object = getAlineacion('barcelona','betis','2020')
#cambios = 0
#for jugador in alineacion_object:
#    if(jugador.cambio is not "" and jugador.estado == "Titular" and jugador.equipo == 'betis'):
#        cambios = cambios + 1
#
#print(cambios)
#
#teams=getTeamsFromLeague('primera','2020')
#print(teams)
#lista=[]
#for team in teams:
#    for team2 in teams:
#        if team is team2:
#            continue

#alineacion_local,alineacion_visitante = getAlineacion('real-madrid','barcelona','2020')
#lista = getClasificacion('primera','2020','1','1')
#lista = getPartidos('primera','2020','1')
#lista = getPlantilla('betis','2020')

#print(alineacion_local)

#maximo = max(alineacion_local, key=lambda jugador: jugador.asistencia)
#print(maximo)
#writeListOfObjectsToCSV(lista,'output1.csv')