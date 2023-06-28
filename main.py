import numpy as np 
from Simulated_Annealing import SA
from Evolutionary_Algorithm import EA
'''
Si quieres saber más acerca de cómo se implementó detalladamente, considera leer el archivo "Técnicas metaheurísticas para la solución del sudoku.pdf".
nota: n es el n
'''
sudoku1=np.array([[0,0,0,2],
                  [2,4,0,3],
                  [0,0,0,0],
                  [0,1,0,0]])
#para el sudoku1 n=2 ya que n^2=4

sudoku2=np.array([[5,3,0,0,7,0,0,0,0],
                  [6,0,0,1,9,5,0,0,0],
                  [0,9,8,0,0,0,0,6,0],
                  [8,0,0,0,6,0,0,0,3],
                  [4,0,0,8,0,3,0,0,1],
                  [7,0,0,0,2,0,0,0,6],
                  [0,6,0,0,0,0,2,8,0],
                  [0,0,0,4,1,9,0,0,5],  
                  [0,0,0,0,8,0,0,7,9]])
#para el sudoku2 n=3 ya que n^2=9
#Recodico simulado
print("recocido primer sudoku")
S1=SA(sudoku1,2)
print(S1.Recocido_Simulado(3,0.001,0.95,10))
#S2=SA(sudoku2,3)
#print(S2.Recocido_Simulado(80,0.001,0.95,300))

#Algoritmo evulutivo
#S11=EA(sudoku1,2)
#print(S11.evolutivo(5,20,0.5,0.5))
print("\nevolutivo segundo sudoku")
S22=EA(sudoku2,3)
print(S22.evolutivo(100,40,0.5,0.5))


'''
intenta ver que sale con un sudoku más grandes:

    sudoku de 16x 16 donde n=4
sudoku16=np.genfromtxt('mega_sudoku16x16.csv', delimiter=',',dtype=int)
S16=SA(sudoku16,4)
print(S16.Recocido_Simulado(5,0.0001,0.95,5))

    sudoku de 250x250 donde n=50
sudoku2500=np.genfromtxt('mega_sudoku2500x2500.csv', delimiter=',',dtype=int)
S2500=EA(sudoku16,50)
print(S2500.Revolutivo(5,10,0.5,0.5))

'''
