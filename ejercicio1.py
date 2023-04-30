'''1. En la universidad se efectuó la elección del representante de los estudiantes 
 ante el Consejo Superior. Se presentaron 30 candidatos y cada uno se identificó 
 con un número del 1 al 30. Asumiendo que los 5000 estudiantes de la universidad votaron, 
 elabore un programa donde: Imprima un listado de mayor a menor, según el número de votos obtenidos 
 por cada candidato'''
 
import numpy as np

def ordenar_burbuja(x:list)->list:
    for j in range(len(x)):
        for i in range(0,len(x)-j-1):
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
    return x

if __name__=="__main__":
    candidatos=np.arange(1,31,1)
    # print(candidatos)
    votos=np.random.randint(1,500,size=30)
    # print(type(votos),votos)
    # print(np.sum(votos))
    eleccion={candidato : votos[i] for i,candidato in enumerate(candidatos)}
    print(eleccion)
    