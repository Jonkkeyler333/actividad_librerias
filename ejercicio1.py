import numpy as np

def show(A:dict)->None:
    print('candidato  |  # votos ')
    for e1,e2 in A.items():
        print(f'     {e1}     |       {e2}')

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
    votos_ordenados.sort(reverse=True)
    ##ordenar votación y ganador
    for voto in votos_ordenados:
        for candidato in candidatos:
            if resultado.get(candidato)==voto:
                eleccion[candidato]=voto
    ##
    print('Elecciones Consejo Superior \n')
    print(f'el ganador de las elecciones al consejo superior es el candidato {(list(eleccion.keys()))[0]} con un total'
          f' de {eleccion[(list(eleccion.keys()))[0]]} votos')
    print('A continuacíon los resultados completos : ')
    show(eleccion)
    print('jonk keyler sanchez pabob-2221551')