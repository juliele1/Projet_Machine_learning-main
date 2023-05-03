import pandas as pd
import numpy as np

data_x = pd.read_csv('Data_X.csv')
data_y = pd.read_csv('Data_Y.csv')
data_new_x = pd.read_csv('DataNew_X.csv')

"""
# Avant suppression des lignes ayant des valeurs nulles
print(data_x)
print(data_new_x)
# Recherche des valeurs nulles
print(data_x.isnull())
print(data_new_x.isnull())
# Suppression des lignes ayant des valeurs nulles
data_x.dropna(inplace=True)
data_new_x.dropna(inplace=True)
print(data_x)
print(data_new_x)


# On remplace les valeurs manquantes par des 0.0

#data_x = data_x.fillna(0.0)
print(data_x.isnull())
print(data_x.loc[:,'DE_RAIN'])
df.loc[:,'SalePrice']

"""

# remplacement des valeurs null par la moyenne de la colonne
for col in data_x.columns[data_x.isnull().any()]:
    data_x[col].fillna(data_x[col].mean(), inplace=True)
print(data_x)

# fusion de data_x et data_y
merged_X_Y = pd.merge(data_x, data_y, on='ID', how='inner')

# triage des données
merged_X_Y = merged_X_Y.sort_values(by=['DAY_ID', 'COUNTRY'])
print(merged_X_Y)

# création de deux datas pour la France et l'Allemagne
data_FR = merged_X_Y.loc[merged_X_Y['COUNTRY'] == 'FR']
data_DE = merged_X_Y.loc[merged_X_Y['COUNTRY'] == 'DE']

# triage des deux datas avec leurs valeurs correspondantes
data_FR = data_FR.filter(regex='FR|GAS_RET|COAL_RET', axis=1)
print(data_FR)

data_DE = data_DE.filter(regex='DE|GAS_RET|COAL_RET', axis=1)
print(data_DE)

# affiche le type de chaque colonnes et si elles sont nulles ou non
data_x.info()

# affiche la distribution, la plage de valeurs et la signification de chaque colonne
data_x.describe()