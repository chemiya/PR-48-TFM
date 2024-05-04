#buscar todos los equipos de la liga
#   para cada uno buscar su plantilla
#buscar todos los partidos de la liga
#   para cada uno buscar sus datos


#Host: http://t4t.infor.uva.es
#Usuario: usuario
#Pass: tfm2024




from bs4 import BeautifulSoup
import requests
URL_BASE="https://www.resultados-futbol.com/"







#equipos de la liga-----------------------------------------------------------

url = URL_BASE + "primera" + str(2021)
response = requests.get(url)

if response.status_code == 200:
    print("entra if")
    soup=BeautifulSoup(response.content,'html.parser')


    teams = dict()
    

    teamList = soup.find_all('li',class_='shield')

    for team in teamList:
        clave = team.find('a').attrs['href']
        clave = clave.strip('/')
    
        valor = team.find('img').attrs['title']


        print("Equipo:"+str(clave)+"/"+str(valor)+"----------------------------------")
        teams[clave] = valor
        
        













#plantillas de cada equipo--------------------------------- 
'''
    teamsKeys = teams.keys()

    for team in teamsKeys:
            print("Jugadores de "+str(team)+"-------------------------------------")
            url = URL_BASE + 'plantilla/' + team + '/' + str(2021)

            response = requests.get(url)

            if response.status_code == 200:
                print("entra if")
                soup=BeautifulSoup(response.content,'html.parser')

                results=soup.find(class_='sdata_table')
                if results is None:
                    print("Nada")
                
                tabla=results.find('tbody')
                if tabla is None:
                    print("Nada")
                
                filas=tabla.find_all('tr')
                if filas is None:
                    print("Nada")

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

                    
                    temporada="2021"
                    nombre=nombre.find('span').string
                    edad=edad.string

                    if goles.string == '-':
                        goles='0'
                    else:
                        goles=goles.string

                    if rojas.string == '-':
                        rojas='0'
                    else:
                        rojas=rojas.string

                    if amarillas.string == '-':
                        amarillas='0'
                    else:
                        amarillas=amarillas.string

                    dorsal=numero.string
                    altura=altura.string
                    peso=peso.string
                    posicion=posicion

                    print(nombre)
                    print(goles)
                    print(amarillas)
                    print(posicion)
'''







#partidos de la liga-----------------------------------------------------
url = URL_BASE + "primera" + str(2021) + '/grupo' + str(1) + '/calendario'
response = requests.get(url)

if response.status_code == 200:
    print("entra if")
    soup=BeautifulSoup(response.content,'html.parser')

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
            
            
            temporada = "2021"
            jornada = jor
            fecha=fecha.string
            local=local
            visitante=  visitante
            foto_local= foto_local
            foto_visitante= foto_visitante
            if resultado is None:
                resultado="Aplazado"
            else:
                resultado=resultado.string.strip(' ')
                resultado=resultado.split("-")
                resultado_local=int(resultado[0])
                resultado_visitante=int(resultado[1])
            

            print("Obtenido: "+str(temporada)+"/"+str(jornada)+"/"+str(fecha)+"/"+str(local)+"/"+str(visitante)+"/"+str(resultado_local)+"/"+str(resultado_visitante))







'''
            url = URL_BASE + "partido/" + local + '/' + visitante + '/' + str(2021)
            response = requests.get(url)

            if response.status_code == 200:
                alineacion_local = []
                alineacion_visitante =[]

                soup=BeautifulSoup(response.content,'html.parser')

                jornada=soup.find('div',class_='jornada')
                
                if None is jornada:
                    print("nada")
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

                    
                    temporada="2021"
                    jugador=nombre
                    if cambio!="":
                        if cambio[1]=="'":
                            cambio=cambio[:1]
                        else:
                            cambio=cambio[:2]
                    else: 
                        cambio=cambio
                    roja=roja     
                    equipo=local

                    print(equipo)
                    print(nombre)
                    print(amarilla)
                    print(roja)
                    print(cambio)
                    print(asistencia)
                    print(lesion)
                    print(gol)
                    print("\n")


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

                    
                    temporada="2021"
                    jugador=nombre
                    if cambio!="":
                        if cambio[1]=="'":
                            cambio=cambio[:1]
                        else:
                            cambio=cambio[:2]
                    else: 
                        cambio=cambio
                    equipo=visitante

                    print(equipo)
                    print(nombre)
                    print(amarilla)
                    print(roja)
                    print(cambio)
                    print(asistencia)
                    print(lesion)
                    print(gol)
                    print("\n")
                    
                
     '''       
    
