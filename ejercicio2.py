from faker import Faker
import numpy as np



fk=Faker()
codigos=np.random.randint(100000, 999999, size=6500)  ##arreglo de los codigos de los estudiantes
nombres=np.empty(6500, dtype='U50')  ##el argumento 'U50' U de unicode y 50 el tamaño de las cadenas
print(type(codigos))
for k in range(0,6500):
    nombres[k]=fk.name()
promedios=np.round(np.random.uniform(0.0,5.0,size=6500),decimals=1)
index=[]
##
for j in range(0,6500):
    if promedios[j]<4.0:
        index.append(j)
##
estudiantes=np.array([codigos,nombres,promedios]) ##Creación de matriz con los datos completos
# print(type(estudiantes[0][1]),estudiantes[1][1],type(estudiantes[2][1]))
# for ind in index:
#         print(estudiantes[0][ind],estudiantes[1][ind],estudiantes[2][ind])
