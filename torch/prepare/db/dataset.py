# dataset.py

import numpy as np
import pandas as pd
from torch.utils.data import Dataset

class TimeSeriesDataset(Dataset):
    """
    Пользовательский класс Dataset для временных рядов.
    Преобразует входные numpy массивы в PyTorch тензоры.
    """
    def __init__(self, X_tensor, y_tensor):
        self.X = X_tensor
        self.y = y_tensor

    def __len__(self):
        """Возвращает общее количество последовательностей в наборе данных."""
        return len(self.X)

    def __getitem__(self, idx):
        """Возвращает одну пару (последовательность признаков, целевое значение) по индексу."""
        return self.X[idx], self.y[idx]

def create_sequences(features_df: pd.DataFrame, targets_series: pd.Series, seq_length: int):
    """
    Создает последовательности (окна) из DataFrame признаков и Series целевых значений.
    Каждая последовательность имеет длину `seq_length`. Целевое значение берется
    для последней точки в каждой последовательности.
    """
    xs, ys = [], []
    # Цикл начинается с (seq_length - 1), чтобы обеспечить полную первую последовательность.
    # Например, если seq_length=60, первая последовательность будет из индексов 0-59.
    # Соответствующее целевое значение - targets_series.iloc[59].
    for i in range(seq_length - 1, len(features_df)):
        # Выбираем seq_length строк (от i - seq_length + 1 до i включительно)
        x = features_df.iloc[i - seq_length + 1 : i + 1].values
        # Целевое значение для последней точки последовательности
        y = targets_series.iloc[i]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys).reshape(-1, 1) # reshape(-1, 1) для корректного формата y