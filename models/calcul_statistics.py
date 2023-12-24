import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, jarque_bera


def calculate_statistics(data, column_name):
    statistics = pd.DataFrame(
        index=['Size', 'Mean', 'Standard deviation', 'Skewness', 'Excess Kurtosis', 'Jarque-Bera'])

    statistics[column_name] = [
        len(data),
        np.mean(data['Dernier']),
        np.std(data['Dernier']),
        skew(data['Dernier']),
        kurtosis(data['Dernier'], fisher=False),
        jarque_bera(data['Dernier'])[0]
    ]

    return statistics
