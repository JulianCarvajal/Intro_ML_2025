"""
Este archivo es generado automaticamente.

###### NO MODIFICAR #########

# cualquier alteración del archivo
# puede generar una mala calficacion o configuracion
# que puede repercutir negativamente en la 
# calificacion del laboratorio!!!!!

"""
from .imports import *
from scipy.stats import mode
from sklearn.model_selection import train_test_split, StratifiedKFold, KFold
from numpy import random
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cdist
from sklearn.datasets import fetch_california_housing

def part_1 ():
#cargamos la bd iris desde el dataset de sklearn
    from sklearn import datasets
    iris = datasets.load_iris()
    x, y = iris.data, iris.target
    GRADER = Grader("lab2_part1")
    
    return(GRADER, x,y)

def part_2 ():
#cargamos la bd iris desde el dataset de sklearn
    #from sklearn.datasets import load_boston
    #x, y = load_boston(return_X_y=True)
    data = fetch_california_housing()
    x, y = data.data, data.target

    GRADER = Grader("lab2_part2")
    
    return(GRADER, x,y)
