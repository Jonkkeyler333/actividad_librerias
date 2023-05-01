from faker import Faker
import numpy as np

fk=Faker()
codigos=np.random.randint(100000, 999999, size=6500)  ##arreglo de los codigos de los estudiantes
nombres=np.empty(6500, dtype='U50')  ##el argumento 'U50' U de unicode y 50 el tamaño de las cadenas
for k in range(0,6500):
    nombres[k]=fk.name()
promedios=np.round(np.random.uniform(0.0,5.0,size=6500))





