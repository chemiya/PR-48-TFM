#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import csv
import re
import locale
from bs4 import BeautifulSoup
from datetime import *

class Excel:
	liga=""     #hecho
	temporada="" #hecho
	jornada="" #hecho
	equipo="" #hecho
	goles="" #hecho
	resultado="" #hecho
	numero_total_cambios=""
	numero_total_cambios_temporada=""
	numero_cambio_portero=""
	numero_cambio_portero_temporada=""
	numero_cambio_defensa=""
	numero_cambio_defensa_temporada=""
	numero_cambio_centrocampista=""
	numero_cambio_centrocampista_temporada=""
	numero_cambio_delantero=""
	numero_cambio_delantero_temporada=""
	media_minuto_cambios=""
	cambio_jugador_mas_asistencias="" #0/1
	cambio_jugador_mas_goles="" #0/1
	cambio_jugador_lesion=""#0/1
	cambio_jugador_amarilla="" #0/1
	cambio_jugador_roja="" #0/1
	titulares_diferentes_anterior_jornada=""
	cambio_jugador_gol_jornada_anterior="" #0/1
	cambio_jugador_amarilla_jornada_anterior="" #0/1
	cambio_jugador_roja_jornada_anterior="" #0/1
	cambio_jugador_lesion_jornada_anterior="" #0/1
	numero_lesiones=""
	numero_lesiones_temporada=""
	numero_amarillas=""
	numero_amarillas_temporada=""
	numero_rojas=""
	numero_rojas_temporada=""
	posicion_local=""
	puntos_local=""
	posicion_rival=""
	puntos_rival=""
	edad_media=""
	peso_medio=""
	altura_media=""
	partido_entre_semana="" #0/1

class jugador:
	equipo=""
	nombre=""
	posicion=""
	altura=""
	peso=""
	edad=""

class objeto_partido:
	temporada=""
	jornada=""
	fecha=""
	local=""
	visitante=""
	resultado=""

class objeto_alineacion:
	temporada=""
	jornada=""
	equipo=""
	jugador=""
	estado=""
	cambio=""
	gol=""
	amarilla=""
	roja=""
	asistencia=""
	lesion=""

class objeto_clasificacion:
	temporada=""
	jornada=""
	posicion=""
	equipo=""
	puntos=""
	ganados=""
	perdidos=""
	empatados=""
	goles_favor=""
	goles_contra=""

class objeto_competiciones:
	fecha=""
	temporada=""
	local=""
	visitante=""

locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')


############################################################################################################################
############################################################################################################################
#######################################     ALMACENAR DATOS EN LISTAS    ###################################################
############################################################################################################################
############################################################################################################################

champions=[]
with open('calendario_champions.csv') as csvfile:
	reader_champions = csv.DictReader(csvfile)
	for champ in reader_champions:
		c=objeto_competiciones()
		c.fecha=champ['champions_fecha']
		c.temporada=champ['champions_temporada']
		c.local=champ['champions_local']
		c.visitante=champ['champions_visitante']
		champions.append(c)

uefa=[]
with open('calendario_uefa.csv') as csvfile:
	reader_uefa = csv.DictReader(csvfile)
	for ue in reader_uefa:
		u=objeto_competiciones()
		u.fecha=ue['uefa_fecha']
		u.temporada=ue['uefa_temporada']
		u.local=ue['uefa_local']
		u.visitante=ue['uefa_visitante']
		uefa.append(u)

copa_del_rey=[]
with open('calendario_dfb_pokal.csv') as csvfile:
	reader_copa = csv.DictReader(csvfile)
	for copa in reader_copa:
		c=objeto_competiciones()
		c.fecha=copa['copa_fecha']
		c.temporada=copa['copa_temporada']
		c.local=copa['copa_local']
		c.visitante=copa['copa_visitante']
		copa_del_rey.append(c)

plantilla_2019_2020=[]
with open('plantilla_bundesliga_2019_2020.csv') as csvfile:
	reader_plantilla = csv.DictReader(csvfile)
	for plantilla in reader_plantilla:
		j=jugador()
		j.equipo=plantilla['plantilla_equipo']
		j.nombre=plantilla['plantilla_name']
		j.posicion=plantilla['plantilla_posicion']
		j.altura=plantilla['plantilla_altura']
		j.peso=plantilla['plantilla_peso']
		j.edad=plantilla['plantilla_edad']
		plantilla_2019_2020.append(j)


plantilla_2018_2019=[]
with open('plantilla_bundesliga_2018_2019.csv') as csvfile:
	reader_plantilla = csv.DictReader(csvfile)
	for plantilla in reader_plantilla:
		j=jugador()
		j.equipo=plantilla['plantilla_equipo']
		j.nombre=plantilla['plantilla_name']
		j.posicion=plantilla['plantilla_posicion']
		j.altura=plantilla['plantilla_altura']
		j.peso=plantilla['plantilla_peso']
		j.edad=plantilla['plantilla_edad']
		plantilla_2018_2019.append(j)


plantilla_2017_2018=[]
with open('plantilla_bundesliga_2017_2018.csv') as csvfile:
	reader_plantilla = csv.DictReader(csvfile)
	for plantilla in reader_plantilla:
		j=jugador()
		j.equipo=plantilla['plantilla_equipo']
		j.nombre=plantilla['plantilla_name']
		j.posicion=plantilla['plantilla_posicion']
		j.altura=plantilla['plantilla_altura']
		j.peso=plantilla['plantilla_peso']
		j.edad=plantilla['plantilla_edad']
		plantilla_2017_2018.append(j)


plantilla_2016_2017=[]
with open('plantilla_bundesliga_2016_2017.csv') as csvfile:
	reader_plantilla = csv.DictReader(csvfile)
	for plantilla in reader_plantilla:
		j=jugador()
		j.equipo=plantilla['plantilla_equipo']
		j.nombre=plantilla['plantilla_name']
		j.posicion=plantilla['plantilla_posicion']
		j.altura=plantilla['plantilla_altura']
		j.peso=plantilla['plantilla_peso']
		j.edad=plantilla['plantilla_edad']
		plantilla_2016_2017.append(j)

partidos=[]
with open('partidos_bundesliga.csv') as csvfile:
	reader_partido=csv.DictReader(csvfile)
	for partido in reader_partido:
		p=objeto_partido()
		p.temporada=partido['partidos_temporada']
		p.jornada=partido['partidos_jornada']
		p.fecha=partido['partidos_fecha']
		p.local=partido['partidos_equipo_local']
		p.visitante=partido['partidos_equipo_visitante']
		p.resultado=partido['partidos_resultado']
		partidos.append(p)

alineacion_2019_2020=[]
with open('alineacion_bundesliga_2019_2020.csv') as csvfile:
	reader_alineacion = csv.DictReader(csvfile)
	for alineacion in reader_alineacion:
		a=objeto_alineacion()
		a.temporada=alineacion['Temporada']
		a.jornada=alineacion['Jornada']
		a.equipo=alineacion['Equipo']
		a.jugador=alineacion['Jugador']
		a.estado=alineacion['Estado']
		a.cambio=alineacion['Cambio']
		a.amarilla=alineacion['Amarilla']
		a.roja=alineacion['Roja']
		a.asistencia=alineacion['Asistencia']
		a.gol=alineacion['Gol']
		a.lesion=alineacion['Lesion']
		alineacion_2019_2020.append(a)

alineacion_2018_2019=[]
with open('alineacion_bundesliga_2018_2019.csv') as csvfile:
	reader_alineacion = csv.DictReader(csvfile)
	for alineacion in reader_alineacion:
		a=objeto_alineacion()
		a.temporada=alineacion['Temporada']
		a.jornada=alineacion['Jornada']
		a.equipo=alineacion['Equipo']
		a.jugador=alineacion['Jugador']
		a.estado=alineacion['Estado']
		a.cambio=alineacion['Cambio']
		a.amarilla=alineacion['Amarilla']
		a.roja=alineacion['Roja']
		a.asistencia=alineacion['Asistencia']
		a.gol=alineacion['Gol']
		a.lesion=alineacion['Lesion']
		alineacion_2018_2019.append(a)

alineacion_2017_2018=[]
with open('alineacion_bundesliga_2017_2018.csv') as csvfile:
	reader_alineacion = csv.DictReader(csvfile)
	for alineacion in reader_alineacion:
		a=objeto_alineacion()
		a.temporada=alineacion['Temporada']
		a.jornada=alineacion['Jornada']
		a.equipo=alineacion['Equipo']
		a.jugador=alineacion['Jugador']
		a.estado=alineacion['Estado']
		a.cambio=alineacion['Cambio']
		a.amarilla=alineacion['Amarilla']
		a.roja=alineacion['Roja']
		a.asistencia=alineacion['Asistencia']
		a.gol=alineacion['Gol']
		a.lesion=alineacion['Lesion']
		alineacion_2017_2018.append(a)

alineacion_2016_2017=[]
with open('alineacion_bundesliga_2016_2017.csv') as csvfile:
	reader_alineacion = csv.DictReader(csvfile)
	for alineacion in reader_alineacion:
		a=objeto_alineacion()
		a.temporada=alineacion['Temporada']
		a.jornada=alineacion['Jornada']
		a.equipo=alineacion['Equipo']
		a.jugador=alineacion['Jugador']
		a.estado=alineacion['Estado']
		a.cambio=alineacion['Cambio']
		a.amarilla=alineacion['Amarilla']
		a.roja=alineacion['Roja']
		a.asistencia=alineacion['Asistencia']
		a.gol=alineacion['Gol']
		a.lesion=alineacion['Lesion']
		alineacion_2016_2017.append(a)

clasificaciones=[]
with open('clasificacion_bundesliga.csv') as csvfile:
	reader_clasificacion = csv.DictReader(csvfile)
	for clasificacion in reader_clasificacion:
		c=objeto_clasificacion()
		c.temporada=clasificacion['clasificacion_temporada']
		c.jornada=clasificacion['clasificacion_jornada']
		c.puntos=clasificacion['clasificacion_puntos']
		c.equipo=clasificacion['clasificacion_equipo']
		c.posicion=clasificacion['clasificacion_posicion']
		c.ganados=clasificacion['clasificacion_ganados']
		c.empatados=clasificacion['clasificacion_empatados']
		c.perdidos=clasificacion['clasificacion_perdidos']
		c.goles_favor=clasificacion['clasificacion_goles_favor']
		c.goles_contra=clasificacion['clasificacion_goles_contra']
		clasificaciones.append(c)

#############################################################################################################################
#############################################################################################################################
##########################################   RECORREMOS ARRAY CLASIFICACION   ###############################################
#############################################################################################################################
#############################################################################################################################


csvfile="/home/gonzalo/Escritorio/TFG/DATOS-ALVARO/BUNDESLIGA/DATOS/datos_natalia.csv"
with open(csvfile,"w")as output:
	writer=csv.writer(output,lineterminator='\n')

	writer.writerow(["Liga", "Temporada", "Jornada", "Equipo", "Posicion", "Puntos", "Goles a Favor", "Goles en Contra",
		"Local/Visitante", "Resultado", "Goles en Partido", "Cambios realizados partido", "Cambios realizados acumulados",
		"Cambios realizados portero partido", "Cambios realizados portero acumulados", "Cambios realizados defensa partido", 
		"Cambios realizados defensa acumulados","Cambios realizados centrocampista partido", "Cambios realizados centrocampista acumulados",
		"Cambios realizados delantero partido", "Cambios realizados delantero acumulados", "Media minuto cambio partido", 
		"Media minuto cambio acumulado", "Cambio jugador más asistencias partido", "Cambio jugador más goles partido",
		"Cambio jugador lesion partido", "Cambio jugador amarilla partido", "Cambio jugador roja partido", "Titulares cambiados respecto jornada anterior",
		"Cambio goleador jornada anterior", "Cambio amarilla jornada anterior", "Cambio roja jornada anterior", 
		"Cambio lesion jornada anterior", "Lesiones en partido", "Lesiones acumuladas", "Amarillas partido", "Amarillas acumuladas",
		"Rojas partido", "Rojas acumuladas", "Posicion Local prepartido", "Puntos local prepartido",
		"Rival", "Posicion rival", "Puntos rival", "Edad media", "Peso medio",
		"Altura media", "Jornada intermedia"])

	for equipo in clasificaciones:
		dato_liga="Bundesliga"
		dato_equipo=equipo.equipo
		dato_temporada=equipo.temporada
		dato_jornada=equipo.jornada
		dato_posicion=equipo.posicion
		dato_puntos=equipo.puntos
		dato_goles_favor_acumulados=equipo.goles_favor
		dato_goles_contra_acumulados=equipo.goles_contra

		dato_local_visitante=""
		dato_resultado=""
		dato_goles=""

		#print(dato_jornada+" "+dato_equipo)

		for part in partidos:
			if(part.temporada==equipo.temporada and part.jornada==equipo.jornada):
				if(equipo.equipo==part.local):
					dato_local_visitante="LOCAL"
					dato_resultado=part.resultado
					if dato_resultado.split('-'):
						dato_goles=dato_resultado.split('-')
						try:
							dato_goles=dato_goles[0]
						except Exception as e:
							print("Error")
						#print(dato_resultado+" "+str(dato_goles))
						break
					else:
						dato_goles="false"
				
				if(equipo.equipo==part.visitante):
					dato_local_visitante="VISITANTE"
					dato_resultado=part.resultado
					if dato_resultado.split('-'):
						dato_goles=dato_resultado.split('-')
						try:
							dato_goles=dato_goles[1]
						except Exception as e:
							print("Error")
						#print(dato_resultado+" "+str(dato_goles))
						break 
					else:
						dato_goles="false"

		if dato_goles=="false":
			break

		jor=dato_jornada.split(" ")
		jor=int(jor[1])

		jornada_anterior=jor-1
		alineacion_anterior=[]
		alineacion_actual=[]
		alineacion_equipo=[]
		alineaciones_pasadas=[]

		copia_alineaciones=[]

		if jor>34:
			continue
		##########################################################################################################################
		####################################################  CASO JORNADA 1  ####################################################
		##########################################################################################################################

		if(jor==1):
			if(dato_temporada=="Temporada2020"):
				copia_alineaciones=alineacion_2019_2020
			elif(dato_temporada=="Temporada2019"):
				copia_alineaciones=alineacion_2018_2019
			elif(dato_temporada=="Temporada2018"):
				copia_alineaciones=alineacion_2017_2018
			else:
				copia_alineaciones=alineacion_2016_2017

			for iter_alineacion in copia_alineaciones:
				jorna=iter_alineacion.jornada.split(" ")
				jorna=int(jorna[1])
				if(iter_alineacion.equipo==dato_equipo and jorna==jor):
					alineacion_actual.append(iter_alineacion)

		########################################################################################################################
		################################## RESTO JORNADAS ######################################################################
		########################################################################################################################
		if (jor>1):
			if(dato_temporada=="Temporada2020"):
				copia_alineaciones=alineacion_2019_2020
			elif(dato_temporada=="Temporada2019"):
				copia_alineaciones=alineacion_2018_2019
			elif(dato_temporada=="Temporada2018"):
				copia_alineaciones=alineacion_2017_2018
			else:
				copia_alineaciones=alineacion_2016_2017

			for iter_alineacion in copia_alineaciones:
				jorna=iter_alineacion.jornada.split(" ")
				jorna=int(jorna[1])
				if(iter_alineacion.equipo==dato_equipo and jorna==jornada_anterior):
					alineacion_anterior.append(iter_alineacion)
				if(iter_alineacion.equipo==dato_equipo and jorna==jor):
					alineacion_actual.append(iter_alineacion)
				if(iter_alineacion.equipo==dato_equipo and jorna<jor):
					alineaciones_pasadas.append(iter_alineacion)


		############################################################################################################################
		##############################################CAMBIOS REALIZADOS EN UN PARTIDO  Y ACUMULADOS ###############################
		############################################## MEDIA CAMBIO PARTIDO Y MEDIA TEMPORADA ######################################
		############################################################################################################################
		############################################################################################################################
		######################################### NUMERO DE LESIONES, AMARILLAS, ROJAS #############################################
		############################################################################################################################
		############################################################################################################################
		########################################### CAMBIO DE JUGADORES LESIONADOS, AMARILLA, ROJA #################################
		############################################################################################################################
		############################################################################################################################
		############################################ MÁXIMO GOLEADOR Y ASISTENTE Y SI HA SIDO CAMBIADO #############################
		############################################################################################################################

		dato_cambios_partido=0
		dato_media_cambio=0
		dato_lesion_partido=0
		dato_amarilla_partido=0
		dato_roja_partido=0

		dato_dictomico_amarilla=0
		dato_dictomico_roja=0
		dato_dictomico_lesion=0
		max_goles=0
		max_asistencias=0

		titulares_actual=[]

		for p in alineacion_actual:
			if p.estado=="Titular":
				titulares_actual.append(p)
			if p.gol!="0":
				g=int(p.gol)
				if g>max_goles:
					max_goles=g
			if p.asistencia!="0":
				asis=int(p.asistencia)
				if asis>max_asistencias:
					max_asistencias=asis
			if p.lesion=="1" and p.cambio!="":
				dato_dictomico_lesion=1
			if p.amarilla=="1" and p.cambio!="":
				dato_dictomico_amarilla=1
			if p.roja=="1" and p.cambio!="":
				dato_dictomico_roja=1
			if p.lesion=="1":
				dato_lesion_partido=dato_lesion_partido+1
			if p.amarilla=="1":
				dato_amarilla_partido=dato_amarilla_partido+1
			if p.roja=="1":
				dato_roja_partido=dato_roja_partido+1
			if p.estado=="Titular" and p.cambio!="":
				dato_cambios_partido=dato_cambios_partido+1
				try:
					dato_media_cambio=dato_media_cambio+int(p.cambio)
				except Exception as e:
					m=int(p.cambio[0])
					dato_media_cambio=dato_media_cambio+m

		if dato_cambios_partido==0:
			dato_media_cambio=0
		else:	
			dato_media_cambio=dato_media_cambio/dato_cambios_partido
		#print(dato_equipo+" "+str(dato_cambios_partido))

		dato_cambios_acumulados_temporada=0
		dato_media_cambio_acumulado=0
		dato_lesion_acumulados_temporada=0
		dato_amarilla_acumulados_temporada=0
		dato_roja_acumulados_temporada=0
		for l in alineaciones_pasadas:
			if l.lesion=="1":
				dato_lesion_acumulados_temporada=dato_lesion_acumulados_temporada+1
			if l.amarilla=="1":
				dato_amarilla_acumulados_temporada=dato_amarilla_acumulados_temporada+1
			if l.roja=="1":
				dato_roja_acumulados_temporada=dato_roja_acumulados_temporada+1
			if l.estado=="Titular" and l.cambio!="":
				dato_cambios_acumulados_temporada=dato_cambios_acumulados_temporada+1
				try:
					dato_media_cambio_acumulado=dato_media_cambio_acumulado+int(l.cambio)
				except Exception as e:
					m=int(l.cambio[0])
					dato_media_cambio_acumulado=dato_media_cambio_acumulado+m

		if jor>1:
			try:
				dato_media_cambio_acumulado=dato_media_cambio_acumulado/dato_cambios_acumulados_temporada
			except Exception as e:
				dato_media_cambio_acumulado=dato_media_cambio_acumulado
		else:
			dato_media_cambio_acumulado=0

		dato_dictomico_cambio_max_goleador=0
		dato_dictomico_cambio_max_asistente=0

		for p in alineacion_actual:
			if int(p.gol)==max_goles and p.cambio!="":
				dato_dictomico_cambio_max_goleador=1
			if int(p.asistencia)==max_asistencias and p.cambio!="":
				dato_dictomico_cambio_max_asistente=1


		#print(dato_equipo+" "+str(dato_lesion_partido)+" "+str(dato_lesion_acumulados_temporada)+" "+str(dato_amarilla_partido)+" "+
		#	str(dato_amarilla_acumulados_temporada)+" "+str(dato_roja_partido)+" "+str(dato_roja_acumulados_temporada))

	######################################################################################################################################
	############################################ VARIABLES RESPECTO JORNADA ANTERIOR #####################################################
	######################################################################################################################################
		
		jugadores_gol_jornada_anterior=[]
		jugadores_amarilla_jornada_anterior=[]
		jugadores_roja_jornada_anterior=[]
		jugadores_lesion_jornada_anterior=[]

		for p in alineacion_anterior:
			if p.lesion=="1" and p.estado=="Titular":
				jugadores_lesion_jornada_anterior.append(p)
			if p.amarilla=="1" and p.estado=="Titular":
				jugadores_amarilla_jornada_anterior.append(p)
			if p.gol!="" and p.estado=="Titular":
				jugadores_gol_jornada_anterior.append(p)
			if p.roja=="1" and p.estado=="Titular":
				jugadores_roja_jornada_anterior.append(p)

		dato_dictomico_goleador_jornada_anterior=0
		for juga_gol in jugadores_gol_jornada_anterior:
			entra=0
			for l in alineacion_actual:
				if l.jugador==juga_gol.jugador:
					entra=1
			if entra==0:
				print('ENTRAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
				dato_dictomico_goleador_jornada_anterior=1
				break

		dato_dictomico_amarilla_jornada_anterior=0
		for juga_ama in jugadores_amarilla_jornada_anterior:
			entra=0
			for l in alineacion_actual:
				if l.jugador==juga_ama.jugador:
					entra=1
			if entra==0:
				dato_dictomico_amarilla_jornada_anterior=1
				break

		dato_dictomico_roja_jornada_anterior=0
		for juga_roj in jugadores_roja_jornada_anterior:
			entra=0
			for l in alineacion_actual:
				if l.jugador==juga_roj.jugador:
					entra=1
			if entra==0:
				dato_dictomico_roja_jornada_anterior=1
				break

		dato_dictomico_lesion_jornada_anterior=0
		for juga_les in jugadores_lesion_jornada_anterior:
			entra=0
			for l in alineacion_actual:
				if l.jugador==juga_les.jugador:
					entra=1
			if entra==0:
				dato_dictomico_lesion_jornada_anterior=1
				break

		numero_titulares_cambiados=0
		for p in alineacion_anterior:
			if p.estado=="Titular":
				entra=0
				for actual in titulares_actual:
					if actual.jugador==p.jugador:
						entra=1
				if entra==0:
					numero_titulares_cambiados=numero_titulares_cambiados+1

		##print(dato_equipo+" "+str(numero_titulares_cambiados))

		##############################################################################################################################
		###################################### EQUIPO RIVAL, POSICION, PUNTOS ########################################################
		##############################################################################################################################

		dato_rival=""
		fecha_jornada_actual=""
		fecha_jornada_pasada=""
		jornada_pasada="Jornada "+str(jornada_anterior)

		for parti in partidos:
			if parti.jornada==jornada_pasada and parti.temporada==dato_temporada:
				if parti.local==dato_equipo:
					fecha_jornada_pasada=parti.fecha
				if parti.visitante==dato_equipo:
					fecha_jornada_pasada=parti.fecha
			if parti.jornada==dato_jornada and parti.temporada==dato_temporada:
				if parti.local==dato_equipo:
					fecha_jornada_actual=parti.fecha
					dato_rival=parti.visitante
				if parti.visitante==dato_equipo:
					fecha_jornada_actual=parti.fecha
					dato_rival=parti.local

		##print(dato_equipo+" "+dato_rival+" "+fecha_jornada_actual+" "+fecha_jornada_pasada)
		dato_rival_puesto=""
		dato_rival_puntos=""
		dato_local_puesto=""
		dato_local_puntos=""
		for clasif in clasificaciones:
			if clasif.jornada==jornada_pasada and clasif.temporada==dato_temporada and clasif.equipo==dato_rival:
				dato_rival_puesto=clasif.posicion
				dato_rival_puntos=clasif.puntos
			if clasif.jornada==jornada_pasada and clasif.temporada==dato_temporada and clasif.equipo==dato_equipo:
				dato_local_puesto=clasif.posicion
				dato_local_puntos=clasif.puntos

		##############################################################################################################################
		################################# CAMBIOS PORTERO,DEFENSA, CENTROCAMPISTA, DELANTERO #########################################
		##############################################################################################################################
		##############################################################################################################################
		#################################  MEDIA EDAD, PESO, ALTURA ##################################################################
		##############################################################################################################################

		dato_cambios_portero=0
		dato_cambios_defensa=0
		dato_cambios_centrocampista=0
		dato_cambios_delantero=0

		copia_plantillas=[]

		if(dato_temporada=="Temporada2020"):
			copia_plantillas=plantilla_2019_2020
		elif(dato_temporada=="Temporada2019"):
			copia_plantillas=plantilla_2018_2019
		elif(dato_temporada=="Temporada2018"):
			copia_plantillas=plantilla_2017_2018
		else:
			copia_plantillas=plantilla_2016_2017


		edad=0
		peso=0
		altura=0
		cont1=0
		cont2=0
		cont3=0

		for p in alineacion_actual:
			for planti in copia_plantillas:
				if p.jugador==planti.nombre and p.equipo==planti.equipo:
					if p.estado=="Titular":
						if planti.edad!="-":
							edad=edad+int(planti.edad)
							cont1=cont1+1
						if planti.peso!="-":
							peso=peso+int(planti.peso)
							cont2=cont2+1
						if planti.peso!="-":
							altura=altura+int(planti.altura)
							cont3=cont3+1
					if planti.posicion=="Portero" and p.estado=="Titular" and p.cambio!="":
						dato_cambios_portero=dato_cambios_portero+1
					if planti.posicion=="Defensa" and p.estado=="Titular" and p.cambio!="":
						dato_cambios_defensa=dato_cambios_defensa+1
					if planti.posicion=="Centrocampista" and p.estado=="Titular" and p.cambio!="":
						dato_cambios_centrocampista=dato_cambios_centrocampista+1
					if planti.posicion=="Delantero" and p.estado=="Titular" and p.cambio!="":
						dato_cambios_delantero=dato_cambios_delantero+1


		try:
			dato_edad=edad/cont1
			dato_peso=peso/cont2
			dato_altura=altura/cont3
		except Exception as e:
			dato_edad=""
			dato_peso=""
			dato_altura=""
		#print(dato_equipo+" "+str(dato_edad)+" "+str(dato_peso)+" "+str(dato_altura))
		##print(str(dato_cambios_portero)+" "+str(dato_cambios_defensa)+" "+str(dato_cambios_centrocampista)+" "+str(dato_cambios_delantero))

		dato_cambios_portero_acumulados=0
		dato_cambios_defensa_acumulados=0
		dato_cambios_centrocampista_acumulados=0
		dato_cambios_delantero_acumulados=0

		for l in alineaciones_pasadas:
			for plantil in copia_plantillas:
				if l.jugador==plantil.nombre and l.equipo==plantil.equipo:
					if plantil.posicion=="Portero" and l.estado=="Titular" and l.cambio!="":
						dato_cambios_portero_acumulados=dato_cambios_portero_acumulados+1
					if plantil.posicion=="Defensa" and l.estado=="Titular" and l.cambio!="":
						dato_cambios_defensa_acumulados=dato_cambios_defensa_acumulados+1
					if plantil.posicion=="Centrocampista" and l.estado=="Titular" and l.cambio!="":
						dato_cambios_centrocampista_acumulados=dato_cambios_centrocampista_acumulados+1
					if plantil.posicion=="Delantero" and l.estado=="Titular" and l.cambio!="":
						dato_cambios_delantero_acumulados=dato_cambios_delantero_acumulados+1
		#print(dato_equipo+" Actuales "+str(dato_cambios_portero)+" "+str(dato_cambios_defensa)+" "+str(dato_cambios_centrocampista)+" "
		#	+str(dato_cambios_delantero)+" Acumulados "+str(dato_cambios_portero_acumulados)+" "+str(dato_cambios_defensa_acumulados)+" "+
		#	str(dato_cambios_centrocampista_acumulados)+" "
		#	+str(dato_cambios_delantero_acumulados))	


	###################################################################################################################################
	################################################# PARTIDOS ENTRE JORNADA ##########################################################
	###################################################################################################################################

		dato_dictomico_jornada_intermedia=0
		print(dato_temporada+" "+dato_jornada+" "+dato_equipo)
		if jor>1:
			objeto_fecha_actual=datetime.strptime(fecha_jornada_actual,'%d %b %y')
			objeto_fecha_pasada=datetime.strptime(fecha_jornada_pasada,'%d %b %y')
			dias_descanso=abs(objeto_fecha_actual-objeto_fecha_pasada).days
			
			nuevo_descanso=0

			for x in champions:
				if x.temporada==dato_temporada:
					if x.local==dato_equipo or x.visitante==dato_equipo:
						objeto_fecha=datetime.strptime(x.fecha,'%d %b %y')
						if objeto_fecha<objeto_fecha_actual:
							nuevo_descanso=abs(objeto_fecha_actual-objeto_fecha).days
							if nuevo_descanso<dias_descanso:
								dato_dictomico_jornada_intermedia=1

			for x in uefa:
				if x.temporada==dato_temporada:
					if x.local==dato_equipo or x.visitante==dato_equipo:
						objeto_fecha=datetime.strptime(x.fecha,'%d %b %y')
						if objeto_fecha<objeto_fecha_actual:
							nuevo_descanso=abs(objeto_fecha_actual-objeto_fecha).days
							if nuevo_descanso<dias_descanso:
								dato_dictomico_jornada_intermedia=1

			for x in copa_del_rey:
				if x.temporada==dato_temporada:
					if x.local==dato_equipo or x.visitante==dato_equipo:
						objeto_fecha=datetime.strptime(x.fecha,'%d %b %y')
						if objeto_fecha<objeto_fecha_actual:
							nuevo_descanso=abs(objeto_fecha_actual-objeto_fecha).days
							if nuevo_descanso<dias_descanso:
								dato_dictomico_jornada_intermedia=1

##############################################################################################################################
################################################ ESCRIBIR DATOS ##############################################################
##############################################################################################################################

		if dato_resultado=="x - x":
			dato_resultado=""
			dato_goles=""
		if dato_resultado=="Aplazado":
			dato_resultado=""
			dato_goles=""

		writer.writerow([dato_liga, dato_temporada, dato_jornada, dato_equipo, dato_posicion, dato_puntos, dato_goles_favor_acumulados, 
		dato_goles_contra_acumulados,
		dato_local_visitante, dato_resultado, dato_goles, dato_cambios_partido, dato_cambios_acumulados_temporada,
		dato_cambios_portero, dato_cambios_portero_acumulados, dato_cambios_defensa, 
		dato_cambios_defensa_acumulados,dato_cambios_centrocampista,dato_cambios_centrocampista_acumulados,
		dato_cambios_delantero,dato_cambios_delantero_acumulados, dato_media_cambio, 
		dato_media_cambio_acumulado, dato_dictomico_cambio_max_asistente, dato_dictomico_cambio_max_goleador,
		dato_dictomico_lesion, dato_dictomico_amarilla, dato_dictomico_roja, numero_titulares_cambiados,
		dato_dictomico_goleador_jornada_anterior, dato_dictomico_amarilla_jornada_anterior, dato_dictomico_roja_jornada_anterior, 
		dato_dictomico_lesion_jornada_anterior, dato_lesion_partido, dato_lesion_acumulados_temporada, 
		dato_amarilla_partido,dato_amarilla_acumulados_temporada,
		dato_roja_partido, dato_roja_acumulados_temporada, dato_local_puesto, dato_local_puntos,
		dato_rival, dato_rival_puesto, dato_rival_puntos, dato_edad, dato_peso,
		dato_altura, dato_dictomico_jornada_intermedia])

		#print(dato_equipo+" "+str(dato_dictomico_jornada_intermedia))


		
