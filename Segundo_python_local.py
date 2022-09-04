#Se crea este archivo para practicar carga de archivo local
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

sma_data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv", sep=",")

sma_data.describe(include = 'all')
