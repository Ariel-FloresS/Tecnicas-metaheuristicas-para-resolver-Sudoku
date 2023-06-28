import random
import numpy as np
'''
Aquí describimos cómo planteamos las soluciones iniciales en nuestras metaheurísticas.

 Si quieres saber más acerca de cómo se implementó detalladamente, considera leer el archivo "Técnicas metaheurísticas para la solución del sudoku.pdf".
'''
class IS:
  def __init__(self,sudoku,n):
    self.sudoku=sudoku
    self.n=n

  def Solucion_inicial(self):
    #solucion inicial del recocido simulado, llena cada fina sin repetir números
    lista=[i for i in range(1,self.n**2+1)]
    random.shuffle(lista)
    newsudoku=np.copy(self.sudoku)
    for i in range(self.n**2):
        for j in range(self.n**2):
            if newsudoku[i][j]==0:
                random.shuffle(lista)
                for k in lista:
                  if k not in newsudoku[i]:
                      newsudoku[i][j] = k
    return newsudoku