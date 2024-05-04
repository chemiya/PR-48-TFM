from bs4 import BeautifulSoup
import requests
URL_BASE="https://www.resultados-futbol.com/"

url = URL_BASE + 'plantilla/' + "Atletico-Madrid" + '/' + str(2022)
lista = []

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



        equipo="Atletico-Madrid"

 
        temporada="2022"
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

    

