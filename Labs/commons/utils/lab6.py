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
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.datasets import load_digits
import warnings
import sklearn   
warnings.filterwarnings('ignore')


def generate_data(is_class = False, cols = 2):
    yy = np.random.choice(3, 30) if is_class else 2*np.random.rand(60).reshape((int(60/cols),cols))
    xx = np.vstack([np.random.rand(15, 3), 2*np.random.rand(15, 3)])
    return (xx, yy)

def part_1 ():
    GRADER = Grader("lab6_part1", num_questions = 4)
    db = np.loadtxt('DB_Fetal_Cardiotocograms.txt',delimiter='\t')  # Assuming tab
    X = db[:,0:22]
    #Solo para dar formato a algunas variables
    for i in range(1,7):
        X[:,i] = X[:,i]*1000
    X = X
    Y = db[:,22]
    Y_l = []
    for i in Y:
        Y_l.append(int(i))
    Y = np.asarray(Y_l)
    return(GRADER, X, Y)

def part_2 ():
    GRADER = Grader("lab6_part2", num_questions = 4)
    db = np.loadtxt('DB_Fetal_Cardiotocograms.txt',delimiter='\t')  # Assuming tab
    X = db[:,0:22]
    #Solo para dar formato a algunas variables
    for i in range(1,7):
        X[:,i] = X[:,i]*1000
    X = X
    Y = db[:,22]
    Y_l = []
    for i in Y:
        Y_l.append(int(i))
    Y = np.asarray(Y_l)

    return(GRADER, X, Y)
