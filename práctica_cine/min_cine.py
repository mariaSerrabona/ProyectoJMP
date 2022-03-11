import pandas as pnd
import JMPEstadisticas as jmp
import numpy as np

#--- CREACION DE UN DATAFRAME ----
lista_valores=[0,1,2,3,4,5]
lista_veces=[40,96,133,145,99,40]

lista_final=[]



for valor in lista_valores:

    for vez in lista_veces:

        contador=0

        while contador < vez:

            lista_final.append(valor)
            contador+=1

observaciones = pnd.DataFrame({'CINE':np.list(lista_final)})

#--- ANALISIS DE UNA CARACTERISTICA ---
stats = jmp.JMPEstadisticas(observaciones['CINE'])
stats.analisisCaracteristica()