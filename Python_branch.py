#Se crea este archivo para practicar New Branch
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
scores = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/exam_scores.csv", sep=",")
scores.describe(include = 'object')
