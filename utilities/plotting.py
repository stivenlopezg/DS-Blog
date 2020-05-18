import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def barplot(df: pd.DataFrame, col: str):
    """
    Take a dataframe and graph the barchart of the variable of interest
    :param df: dataframe
    :param col: column of interest
    :return:
    """
    aux = df[col].value_counts().sort_values(ascending=True)
    bars = tuple(aux.index.tolist())
    values = aux.values.tolist()
    y_pos = np.arange(len(bars))
    colors = ['lightblue'] * len(bars)
    colors[-1] = 'blue'
    plt.figure(figsize=(16, 10))
    plt.barh(y_pos, values, color=colors)
    plt.title(f'{col} bar chart')
    plt.yticks(y_pos, bars)
    return plt.show()

