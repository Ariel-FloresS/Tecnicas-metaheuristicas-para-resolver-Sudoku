
import numpy as np
import random
from Objetive_Function import FO
from Initial_Solution import IS
'''
se basa en la evolución biológica y busca encontrar soluciones óptimas a problemas de optimización, la construccion del algoritmo es:
1.diseñar una representación (EN forma de matriz)
2.Decidir como se inicializa una poblacion (Initial_solution.py)
3.diseñar una forma de evaluar a los indiviuos (FO Y fitness)
4.Diseñar un operador de mutacion adecuado 
5.Diseñar un operador de cruce adecuado (de un punto)
6.DIseñar un paso extintivo (por torneo)

Si quieres saber más acerca de cómo se implementó detalladamente, considera leer el archivo "Técnicas metaheurísticas para la solución del sudoku.pdf".
'''

class EA:

  def __init__(self,sudoku,n):
    self.sudoku=sudoku
    self.n=n
    self.OF=FO(sudoku,n)

  def escoge_fila(self):
    k=0
    filas=[]
    for i in range (self.n**2):
        for j in range (self.n**2):
            if self.sudoku[i][j]==0:
                k+=1
        if k>=3:
            filas.append(i)
        k=0
    return filas  
    
  def fitness(self,array):
    f=FO(array,self.n)
    return(1/(1+f.Funtion()))
    
  def cruza(self,tasa_cruza,padre1,padre2):
    hijo1=np.copy(padre1)
    hijo2=np.copy(padre2)
    if random.random()<tasa_cruza:
        if self.n**2%2==0:
            for i in range (int(self.n**2/2)):
                hijo1[i]=padre2[i]
                hijo2[i]=padre1[i]
        else:        
            indice=self.OF.Chunk()
            mitad=int(len(indice)/2)
            for i in range(indice[mitad],indice[mitad]+self.n):
                hijo1[i]=padre2[i]
                hijo2[i]=padre1[i]        
    return hijo1,hijo2
    
  def genera_cruza(self,tasa_cruza,poblacion):
    newpoblacion=[]
    p=poblacion.copy()
    while(len(p)!=0):
        random.shuffle(p)
        h1,h2=self.cruza(tasa_cruza,p[0],p[1])
        newpoblacion.append(h1)
        newpoblacion.append(h2)
        p.pop(0)
        p.pop(0)
    return newpoblacion

  def mutacion(self,tasa_mutacion,hijo):
    mutado=np.copy(hijo)
    if random.random()<=tasa_mutacion:
        filas=self.escoge_fila()
        for e in range(self.n):
            i=random.choice(filas)
            p=random.randint(0, self.n**2-1)
            q=random.randint(0, self.n**2-1)
            while(self.sudoku[i][p]!=0 or self.sudoku[i][q]!=0):
                p=random.randint(0, self.n**2-1)
                q=random.randint(0, self.n**2-1)
            mutado[i][p]=hijo[i][q]
            mutado[i][q]=hijo[i][p] 
            hijo=np.copy(mutado)
    return mutado 
  def genera_mutacion(self,newpoblacion,tasa_mutacion):
    mutados=[]
    for hijo in newpoblacion:
        mutados.append(self.mutacion(tasa_mutacion,hijo))
    return mutados
  
  def genera_poblacion(self,tam_poblacion):
    Poblacion=[]
    for i in range(tam_poblacion):
            sol_inicial=IS(self.sudoku,self.n)
            Poblacion.append(sol_inicial.Solucion_inicial())
    return Poblacion 
    
  def extincion(self,poblacion,mutados,tam_poblacion):
    todos=poblacion+mutados
    fitness_lista=[]
    nextpoblacion=[]
    for i in todos:
        fitness_lista.append(self.fitness(i))
    mejor=max(fitness_lista) 
    indice=fitness_lista.index(mejor)
    nextpoblacion.append(todos[indice])
    P=[f/sum(fitness_lista) for f in fitness_lista]
    indices=list(range(int(len(todos))))
    individuo_seleccionado=np.random.choice(indices,size=tam_poblacion-1,replace=False,p=P)
    contador=0
    for p in range(tam_poblacion-1):
        nextpoblacion.append(todos[individuo_seleccionado[contador]])
        contador+=1
    return nextpoblacion

  def evolutivo(self,generaciones,tam_poblacion,tasa_cruza,tasa_mutacion):
    generacion=0
    
    poblacion=self.genera_poblacion(tam_poblacion)
    while(generacion<=generaciones):
        hijos=self.genera_cruza(tasa_cruza,poblacion)
        mutados=self.genera_mutacion(hijos,tasa_mutacion)
        poblacion=self.extincion(poblacion,mutados,tam_poblacion)
        generacion+=1
  
    valormax=[]    
    for i in poblacion:
        valormax.append(self.fitness(i))
    valor= max(valormax)
    i=valormax.index(valor)

    funcion=FO(poblacion[i],self.n)
    print( "FO: ",funcion.Funtion(),", generaciones: ",generacion-1,", tamaño de la población: ", tam_poblacion, ", tasa de cruza: ",tasa_cruza," y una tasa de mutacion de: ", tasa_mutacion, "\n Solución")   
    return poblacion[i]
  