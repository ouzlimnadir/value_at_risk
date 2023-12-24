# Dans le fichier calcul_var.py

import numpy as np
from scipy.stats import norm


def calculate_var_n(data, column_name, tableau_var):
    # Tableau des rendements
    rt = np.zeros(len(data['Dernier']) - 1)

    for i in range(len(data['Dernier']) - 1):
        rt[i] = data['Dernier'][i + 1] / data['Dernier'][i] - 1

    # Calcul de la moyenne, la variance et l'écart-type du rendement rt
    rt_std = np.std(rt)

    # Calcul de la VaR
    alpha = [0.05, 0.025, 0.02, 0.015, 0.01, 0.005, 0.001]
    var_n = [- rt_std * norm.ppf(a) for a in alpha]

    # Ajouter les résultats au tableau_var
    tableau_var[column_name] = var_n
