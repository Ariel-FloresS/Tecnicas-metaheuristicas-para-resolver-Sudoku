import numpy as np
import random
import math as mt
from Objetive_Function import FO
from Initial_Solution import IS
'''
Es una técnica de búsqueda local que utiliza una estrategia probabilística para aceptar soluciones subóptimas y escapar de mínimos locales. El proceso de Recocido Simulado imita el proceso físico de enfriamiento y calentamiento de un material para mejorar su estructura interna, pseudocodigo:

    Input: instacia (S,t) y N (neighbors) una función de vecindad, una temperatura inicial (tmin>0), un programa de enfriamento (alpha), un numero de iteraciones (NI) por temperatura maxima (tmax) y un criterio de paro.
    
    Generar una solucion inicial S0
    Mientras tmax>=tmin hacer
      selecionar aleatoriamente una solución S ∈ N(S0)
      calcular alpha=f(S)-f(S0)
      si alpha<=0 entonces S0<-SA
      de lo contrario
        generar aleatoriamente u~U(0,1)
        si u<exp(-alpha/tmax) entonces S0<-SA
    actualizar la temperatura   
    Si quieres saber más acerca de cómo se implementó detalladamente, considera leer el archivo "Técnicas metaheurísticas para la solución del sudoku.pdf".
'''
class SA:
  def __init__(self,sudoku,n):
    self.sudoku=sudoku
    self.n=n
  def neighbors(self,sol_inicial):
    nuevo=np.copy(sol_inicial)
    k=random.randint(0, self.n**2-1)
    l=random.randint(0,self.n**2-1)
    p=random.randint(0,self.n**2-1)
    q=random.randint(0,self.n**2-1)
    for e in range(self.n):
        while(self.sudoku[k][l]!=0 or self.sudoku[p][q]!=0):
            k=random.randint(0, self.n**2-1)
            l=random.randint(0, self.n**2-1)
            p=random.randint(0, self.n**2-1)
            q=random.randint(0,self.n**2-1)    
        nuevo[k][l]=sol_inicial[p][q]
        nuevo[p][q]=sol_inicial[k][l]
    return nuevo 
    
  def OF(self,array):
    f=FO(array,self.n)
    return f.Funtion()
    
  def  Recocido_Simulado(self,tmax,tmin,alpha,NI):
    delta=0
    sol_inicial=IS(self.sudoku,self.n)
    sol_actual=np.copy(sol_inicial.Solucion_inicial())
    while(tmax>=tmin):
        for i in range(NI):
            sol_vecina=self.neighbors(sol_actual)
            delta=self.OF(sol_vecina)-self.OF(sol_actual)
            if(delta<=0):
                sol_actual=sol_vecina
            else:
                if(random.random()<mt.exp(-delta/tmax)):
                    sol_actual=sol_vecina
        tmax=tmax*alpha
        if(self.OF(sol_actual)==0):
            break
    print("FO: ",self.OF(sol_actual), ",la temperatura: ",tmax,"la solución es: \n" )
    return(sol_actual) 