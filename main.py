import pandas as pd

from models.extraction_data import extract_data
from models.selection_colonnes import select_columns
from models.calcul_statistics import calculate_statistics
from models.var_n import calculate_var_n
from models.var_t import calculate_var_t

folder = 'data/'
ext = '.xls'

MASI = folder + 'masi' + ext
MSI20 = folder + 'msi20' + ext
CFG25 = folder + 'cfg25' + ext
ESG10 = folder + 'esg10' + ext

data_frames = [extract_data(MASI), extract_data(MSI20), extract_data(CFG25), extract_data(ESG10)]

colonnes = ['MASI', 'MSI20', 'CFG25', 'ESG10']

# Tableau pour les statistiques récapitulatives
resume_statistique = pd.DataFrame(
    index=[
        'Size',
        'Mean',
        'Standard deviation',
        'Skewness',
        'Excess Kurtosis',
        'Jarque-Bera'
    ]
)

# Tableau pour les valeurs VaR
tableau_var_n = pd.DataFrame(index=[0.05, 0.025, 0.02, 0.015, 0.01, 0.005, 0.001])
tableau_var_t = pd.DataFrame(index=[0.05, 0.025, 0.02, 0.015, 0.01, 0.005, 0.001])

for i, data in enumerate(data_frames):
    # Extraction des données
    DS = select_columns(data)

    # Calcul des statistiques récapitulatives
    statistics = calculate_statistics(DS, colonnes[i])
    resume_statistique[colonnes[i]] = statistics[colonnes[i]]

    # Calcul de VaR
    calculate_var_n(data, colonnes[i], tableau_var_n)
    calculate_var_t(data, colonnes[i], tableau_var_t)

# Affichage des tableaux
print("\nTableau des statistiques récapitulatives:")
print(resume_statistique)

print("\nTableau VaR_N en fonction de alpha:")
print(tableau_var_n)

print("\nTableau VaR_T en fonction de alpha:")
print(tableau_var_t)
