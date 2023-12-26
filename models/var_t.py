import numpy as np
from scipy.stats import t


def calculate_var_t(data, column_name, tableau_var):
    # Tableau des rendements
    rt = np.zeros(len(data['Dernier']) - 1)

    for i in range(len(data['Dernier']) - 1):
        rt[i] = data['Dernier'][i + 1] / data['Dernier'][i] - 1

    # Calcul de la moyenne des rendements rt
    mu = np.mean(rt)
    rt_std = np.std(rt)
    k = np.mean(((rt - mu) / rt_std) ** 2)

    beta = rt_std ** 2 * (k + 3) / (2 * k + 3)
    n = int(6 / k + 4) + 1

    # Calcul de la VaR_N
    alpha = [0.05, 0.025, 0.02, 0.015, 0.01, 0.005, 0.001]
    var_t = [- np.sqrt(beta) * t.ppf(a, n) for a in alpha]

    # Ajouter les résultats au tableau_var
    tableau_var[column_name] = var_t
