#import numpy as np
'''
definimos la  función objetivo (FO) que cuenta la cantidad de números repetidos en cada fila, columna y bloque. El objetivo es minimizar esta función, lo que significa reducir al mínimo la cantidad de números repetidos. Se sabe que el mínimo global de la FO es 0, lo que indica que el sudoku está resuelto cuando no hay números repetidos en ninguna fila, columna o bloque

Si quieres saber más acerca de cómo se implementó detalladamente, considera leer el archivo "Técnicas metaheurísticas para la solución del sudoku.pdf".
'''

from collections import Counter
class FO:
  def __init__(self,sudoku,n):
    self.sudoku=sudoku
    self.n=n
  def Chunk(self):
    #esta función nos da el indice de cada bloque
    multiplos=[0]
    for i in range(1,self.n**2):
        if(i%self.n==0):
            multiplos.append(i)
    return multiplos
    
  def Funtion(self):
    # contamos los números repetidos de cada fila y columna
    row=[]
    number_rows=0
    column=[]
    number_columns=0
    for i in range(self.n**2):
      for j in range(self.n**2):
        row.append(self.sudoku[i,j])
        column.append(self.sudoku[j,i])
        if(j==self.n**2-1):
          count_row = Counter(row)
          count_column=Counter(column)
          number_rows+=(self.n**2)-len(count_row)
          number_columns+=(self.n**2)-len(count_column)
          row.clear()
          column.clear() 
    #contamos los números repetidos de cada bloque
    mult=self.Chunk()
    chunks=[]
    number_chunks=0
    k=1
    for u in mult:
        for v in mult:
            for i in range(self.n):
                for j in range(self.n):
                    chunks.append(self.sudoku[i+u,j+v])
                    k+=1
                    if(k==self.n**2+1):
                        count_chunks=Counter(chunks)
                        number_chunks+=(self.n**2)-len(count_chunks)
                        chunks.clear()
                        k=1
    
    return   number_rows+number_columns+number_chunks
     # Ariel flores     