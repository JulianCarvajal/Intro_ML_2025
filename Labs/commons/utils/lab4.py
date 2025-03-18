"""
Este archivo es generado automaticamente.

###### NO MODIFICAR #########

# cualquier alteración del archivo
# puede generar una mala calificación o configuracion
# que puede repercutir negativamente en la 
# calificación del laboratorio!!!!!

###### NO MODIFICAR #########
"""

from .imports import *
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import mean_absolute_error, accuracy_score, mean_absolute_percentage_error,classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.datasets import load_digits, load_iris, load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')


def generate_data(is_class = False, deter = False):
    yy = np.random.choice(2, 30) if is_class else 2*np.random.rand(60).reshape((30,2))
    xx = np.vstack([np.random.rand(15, 3), 2*np.random.rand(15, 3)])

    if deter:
        yy = np.array([1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1])
    return (xx, yy)

def part_1 ():
    GRADER = Grader("lab4_part1", num_questions = 4)
    return(GRADER)

def generate_data2():
    xx = np.array([[1,2,2], [2,2,3], [1,1,3], [1,2,3]])
    yy = np.array([1,1,2,2])

    xxt = np.array([[0,1,2], [1,1,2]])
    yyt = np.array([1,2])
    return(xx, yy, xxt, yyt)

def part_2():
    GRADER = Grader("lab4_part2", num_questions = 5)
    return(GRADER)
