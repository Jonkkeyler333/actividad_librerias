from faker import Faker
import numpy as np

def buscardor_index(A:np.ndarray,B:np.ndarray,promedio:float,programa:int)->list:
    index=[]
    if programa == None or programa==0:
        for j in range(0,6500):
            if A[j]>promedio:
                index.append(j)
    else:
        for j in range(0,6500):
            if A[j]>promedio and B[j]==programa:
                index.append(j)
    return index

fk=Faker()
codigos=np.random.randint(100000, 999999, size=6500)  ##arreglo de los codigos de los estudiantes
nombres=np.empty(6500, dtype='U50')  ##el argumento 'U50' U de unicode y 50 el tamaño de las cadenas
for k in range(0,6500):
    nombres[k]=fk.name()
programas=np.random.randint(1,80,size=6500)
promedios=np.round(np.random.uniform(0.0,5.0,size=6500),decimals=1)
estudiantes=np.array([codigos,nombres,promedios,programas]) ##Creación de matriz con los datos completos

if __name__=='__main__':
    print('Bienvedio al sistema')
    print(f'Desea ver los estudiantes con promedio acumulado destacado (mayor que 4) de un programa en' 
          f'especifico ? \n 1-->Si   /   2-->No')
    des=int(input())
    if des==1:
        prog=int(input('Ingrese el programa (número del 1 al 80):   '))
        index=buscardor_index(promedios,programas,4.0,prog)
        print(f'\n Promedios destacados del programa {prog}')
        for ind in index:
            print(estudiantes[0][ind],estudiantes[1][ind],estudiantes[2][ind],estudiantes[3][ind])
    else:
        index=buscardor_index(promedios,programas,4.0,0)
        for ind in index:
            print(estudiantes[0][ind],estudiantes[1][ind],estudiantes[2][ind],estudiantes[3][ind])
        print('Promedios destacados generales')