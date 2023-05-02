from faker import Faker
import numpy as np

def buscardor_index(A:np.ndarray,B:np.ndarray,C:np.ndarray,promedio:float,programa:int,fecha:int)->list:
    """Esta función busca los indices de los estudiantes que cumplen con las condiciones dadas

    :param A: Array de informacion del est 
    :type A: np.ndarray
    :param B: Array de información del est 
    :type B: np.ndarray
    :param promedio: promedio que debe cumplir el estudiante buscado
    :type promedio: float
    :param programa: número del programa a buscar (si es 0 , son todos los programas)
    :type programa: int
    :return: la lista con los estudiantes(indices) que cumplen las condiciones
    :rtype: list
    """
    index=[]
    if programa==0 and fecha==0:
        for j in range(0,6500):
            if A[j]>promedio:
                index.append(j)
    elif fecha>0 and programa==0:
        for j in range(0,6500):
            if A[j]<=promedio and B[j]==programa and C[j]<fecha:
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
fecha_ingreso=np.random.randint(1970,2023,size=6500)
promedios=np.round(np.random.uniform(0.0,5.0,size=6500),decimals=1)
estudiantes=np.array([codigos,nombres,promedios,programas,fecha_ingreso]) ##Creación de matriz con los datos completos

if __name__=='__main__':
    print('Bienvedio al sistema')
    print(f'Desea ver los estudiantes con promedio acumulado destacado (mayor que 4) de un programa en' 
          f'especifico ? \n 1-->Si   /   2-->No')
    des=int(input())
    if des==1:
        prog=int(input('Ingrese el programa (número del 1 al 80):   '))
        index=buscardor_index(promedios,programas,fecha_ingreso,4.0,prog,0)
        print(f'\n Promedios destacados del programa {prog} : ')
        for ind in index:
            print(estudiantes[0][ind],'|',estudiantes[1][ind],'|',estudiantes[2][ind],'|',estudiantes[3][ind],'|',estudiantes[4][ind])
        print(f'En total fueron {len(index)} estudiantes destacados')
    else:
        index=buscardor_index(promedios,programas,fecha_ingreso,4.0,0,0)
        for ind in index:
            print(estudiantes[0][ind],'|',estudiantes[1][ind],'|',estudiantes[2][ind],'|',estudiantes[3][ind],'|',estudiantes[4][ind])
        print('Promedios destacados generales')
        print(f'En total fueron {len(index)} estudiantes destacados')

    inq=[]
    print('\n\n Ahora se mostraran estudiantes en Condicional con ingreso anterior a 1990')
    inq=buscardor_index(promedios,programas,fecha_ingreso,3.2,0,1990)
    if len(inq)==0:
        print('No se encontro ningún estudiante')
    else:
        for ind2 in inq:
            print(estudiantes[0][ind],'|',estudiantes[1][ind],'|',estudiantes[2][ind],'|',estudiantes[3][ind],'|',estudiantes[4][ind])
    