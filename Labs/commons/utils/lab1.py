"""
Este archivo es generado automaticamente.

###### NO MODIFICAR #########

# cualquier alteración del archivo
# puede generar una mala calificación o configuracion
# que puede repercutir negativamente en la 
# calificación del laboratorio!!!!!

###### NO MODIFICAR #########
"""
from imports import *

def potenciaPolinomio(X,grado):
    """calcula la potencia del polinomio
    X: los valores que corresponden a las caractersiticas
    grado: esl grado para realizar la potencia al polinomio
    """
    X2 = X.copy()
    
    if grado != 1:
        for i in range(2,grado+1):
            Xadd = X**i
            X2 = np.concatenate((X2, Xadd), axis=1)
    
    return X2

def part_1():
    print("cargando librerias y variables al ambiente")
    GRADER_LAB_1_P1 = Grader("lab1_part1")
    
    data_path = os.path.join(os.getcwd(),'Labs','commons','utils','data', 'AirQuality.data')
    db = np.loadtxt(data_path,delimiter='\t') 
    x = db[:,0:12]
    y = db[:,12]
    return (GRADER_LAB_1_P1, db, x, y)

#
# parte 2
#
def part_2():
    print("cargando librerias y variables al ambiente")
    GRADER = Grader("lab1_part2")
    data_path = os.path.join(os.getcwd(),'Labs','commons','utils','data', 'DatosClases.mat')
    mat = scipy.io.loadmat(data_path)
    x = mat['X'] # Matriz X de muestras con las características
    y = mat['Y'] # Variable de salida
    return (GRADER, x, y)