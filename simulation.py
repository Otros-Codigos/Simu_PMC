
# Importar la informanción de necesaria
# _______________________________________

import data_cities as ct
import data_persons as pt

from math import radians, sin, cos, acos
from datetime import datetime
import random as rd
import pulp as lp

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

trip_cities = ct.trip_cities()
user_cities = ct.user_cities()
persons = pt.combinations("names.txt")

def mip_simulation(report, NUM_VIAJEROS, NUM_USUARIOS, iter, NUM_SIMULATIONS):

    # Simulador de escenario
    # _______________________

    # I. Conjuntos
    Viajeros = []
    Usuarios = []

    # II.Parametros no indexados
    dist_max = 150

    # III. Parametros indexados
    dataViajeros = {}

    for _ in range(NUM_VIAJEROS):

        pos_person = rd.randint(0, len(persons)-1)
        name_trip = persons[pos_person]

        if name_trip not in list(dataViajeros.keys()):

            Viajeros.append(name_trip)

            objects = round(rd.random()*50, 2)
            price = round(rd.random()*1000, 2)

            cities_name = list(trip_cities.keys())
            city = rd.randint(0, len(cities_name)-1)

            dataViajeros[name_trip] = [ct.adjust_coordinate(trip_cities[cities_name[city]][0]), ct.adjust_coordinate(trip_cities[cities_name[city]][1]), objects, price]

        else:
            _ -= 1

    dataUsuarios = {}

    for _ in range(NUM_USUARIOS):

        pos_person = rd.randint(0, len(persons)-1)
        name_trip = persons[pos_person]

        if name_trip not in list(dataUsuarios.keys()):

            Usuarios.append(name_trip)

            ask = round(rd.random()*5, 2)

            cities_name = list(user_cities.keys())
            city = rd.randint(0, len(cities_name)-1)

            dataUsuarios[name_trip] = [ct.adjust_coordinate(user_cities[cities_name[city]][0]), ct.adjust_coordinate(user_cities[cities_name[city]][1]), ask]

        else:
            _ -= 1

    # IV: Espacio estado
    Viajeros_x_Usuarios = [(v,u) for v in Viajeros for u in Usuarios]

    # Parametrización del Modelo
    # _______________________

    (lat_v, lon_v, objetos, precio) = lp.splitDict(dataViajeros)
    (lat_u, lon_u, pedidos) = lp.splitDict(dataUsuarios)

    distancias = {}

    for i in Viajeros: 
        lat_x, lon_x = radians(lat_v[i]), radians(lon_v[i])
        for j in Usuarios:
            lat_y, lon_y = radians(lat_u[j]), radians(lon_u[j])
            distancias[i,j] = 6371 * acos(sin(lat_x)*sin(lat_y) + cos(lat_x)*cos(lat_y)*cos(lon_x - lon_y))

    # Modelo
    # _______________________

    start = datetime.now()

    #-------------------------------------
    # Creación del objeto problema en PuLP
    #-------------------------------------
    problema = lp.LpProblem("Packa", lp.LpMinimize)

    #-----------------------------
    #    Variables de Decisión
    #-----------------------------

    activar = lp.LpVariable.dicts('Activar', Viajeros, 0, 1, lp.LpBinary)
    atender = lp.LpVariable.dicts('Atender', Viajeros_x_Usuarios, 0, 1, lp.LpBinary)

    #-----------------------------
    #    Función objetivo
    #-----------------------------

    # MAX cobertura 
    problema += -lp.lpSum([pedidos[u]*atender[v,u] for v,u in Viajeros_x_Usuarios if distancias[v,u] <= dist_max]), "Satisfacción total"

    #-----------------------------
    #    Restricciones
    #-----------------------------

    # 1.	Se deben atender todos los usuarios
    for u in Usuarios:
        problema += lp.lpSum([atender[v,u] for v in Viajeros]) == 1, "Atender centro " + u

    # 2.	Capacidad limitada en los viajeros.
    for v in Viajeros:
        problema += lp.lpSum([pedidos[u]*atender[v,u] for u in Usuarios]) <= objetos[v]*activar[v], 'Respetar capacidades de ' + v

    #-----------------------------
    #    Invocar el optimizador
    #-----------------------------
    solver = lp.PULP_CBC_CMD(msg=0, timeLimit = 60)
    problema.solve(solver)

    #-----------------------------
    #    Guardar los resultados
    #-----------------------------

    coverture = round(
        sum(
            pedidos[u] * atender[v, u].value()
            for v, u in Viajeros_x_Usuarios
            if distancias[v, u] <= dist_max
        ),
        1,
    ) / sum(pedidos[u] for u in Usuarios)


    #-----------------------------
    #    Imprimir resultados
    #-----------------------------

    print(iter, "Tiempo de solucion:",datetime.now()-start)

    if report:
        print("\n=============")
        print("     Packa   ")
        print("=============\n")

        print("Cobertura:\t",str(round(coverture*100))+"%")
        print("Viajeros:\t",sum(activar[v].value() for v in Viajeros))

        print("\n======================================")

    if iter == NUM_SIMULATIONS:

        # ----------------------------
        #     RED DE DISTRIBUCIÓN
        # ---------------------------

        mapbox_token = 'pk.eyJ1Ijoic2FudGlhZ28tYm9iYWRpbGxhIiwiYSI6ImNrc3U5azRwYzExZ3gyb2pzbWNvOWtlaDIifQ.5z_sIL0KCQaJukiy018UJw'

        red = [(v,u) for v,u in Viajeros_x_Usuarios if atender[v,u].value() > 0]

        map = []
        viajes = []
        destino = []

        for i,j in red:
                      # Nombre, Lat, Long
            inicio = [i, i, dataViajeros[i][0], dataViajeros[i][1]]
            parada = [i, j, dataUsuarios[j][0], dataUsuarios[j][1]]

            map.append(inicio)
            map.append(parada)

            if i not in viajes:
              viaj = [i, dataViajeros[i][0], dataViajeros[i][1]]
              viajes.append(viaj)

            if j not in destino:
              dest = [j, dataUsuarios[j][0], dataUsuarios[j][1]]
              destino.append(dest)

        map_info = pd.DataFrame(map, columns = ['Viaje', 'Destino', 'lat', 'lon'])
        viajes_info = pd.DataFrame(viajes, columns = ['Viaje', 'lat', 'lon'])
        destino_info = pd.DataFrame(destino, columns = ['Destino', 'lat', 'lon'])

        fig = px.line_mapbox(map_info, lat="lat", lon="lon", color="Viaje", text = "Destino", zoom=5, height=1000)

        viaje_lat = viajes_info.lat
        viaje_lon = viajes_info.lon
        viaje_name = viajes_info.Viaje

        fig.add_trace(go.Scattermapbox(lat=viaje_lat, lon=viaje_lon, mode='markers',
                                        marker=dict(size=7, symbol = 'triangle', color= 'blue', opacity = 0.7),
                                        text=viaje_name, hoverinfo='text'
                                      )
                      )

        destino_lat = destino_info.lat
        destino_lon = destino_info.lon
        destino_name = destino_info.Destino

        fig.add_trace(go.Scattermapbox(lat=destino_lat, lon=destino_lon, mode='markers',
                                        marker=dict(size=7, symbol = 'square', color= 'red', opacity = 0.7),
                                        text=destino_name, hoverinfo='text'
                                      )
                      )

        fig.update_layout(mapbox_style="dark", mapbox_accesstoken=mapbox_token)
        fig.show()



    # Resultados
    return coverture, sum(activar[v].value() for v in Viajeros)