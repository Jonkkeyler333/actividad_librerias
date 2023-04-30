'''1. En la universidad se efectuó la elección del representante de los estudiantes 
 ante el Consejo Superior. Se presentaron 30 candidatos y cada uno se identificó 
 con un número del 1 al 30. Asumiendo que los 5000 estudiantes de la universidad votaron, 
 elabore un programa donde: Imprima un listado de mayor a menor, según el número de votos obtenidos 
 por cada candidato'''
 
import numpy as np


if __name__=="__main__":
    candidatos=np.arange(1,31,1)
    votos=np.zeros(30,dtype=int)
    total_votos=0
    i=0
    ##algoritmo para llenar votos
    while total_votos<5000:
        candidato=np.random.randint(0,30)
        votos[candidato]+=1
        total_votos+=1
    ##
    resultado={candidato : votos[i] for i,candidato in enumerate(candidatos)} ##resultados de la elección
    eleccion={} ##Resultados ordenados y finales de la elección
    votos_ordenados=list(resultado.values())
    votos_ordenados.sort()
    print(votos_ordenados)
    for voto in votos_ordenados:
        for candidado in resultado:
            if resultado.get(candidato)==voto:
                pass
                # print(voto)
    # print(resultado)
    # print(eleccion)
            
    