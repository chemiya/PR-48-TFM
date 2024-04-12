from bs4 import BeautifulSoup
import requests
URL_BASE="https://www.resultados-futbol.com/"

url = URL_BASE + "primera" + str(2022) + '/grupo' + str(1) + '/jornada' + str(36)
lista = []

response = requests.get(url)

if response.status_code == 200:
    print("entra if")
    soup=BeautifulSoup(response.content,'html.parser')

    results=soup.find('table',id='tabla2')
    results=results.find('tbody')

    equipos=results.find_all('tr')
    jor='Jornada '+str(36)

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

