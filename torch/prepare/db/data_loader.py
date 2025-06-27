#data_loader.py

import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader

from .dataset import TimeSeriesDataset, create_sequences

TEST_SIZE = 0.2  # 20% для тестовой выборки
RANDOM_SEED = 42
VALIDATION_SPLIT_RATIO = 0.15
SEQUENCE_LENGTH = 16
BATCH_SIZE = 32

def get_data_loaders(X: pd.DataFrame, y: pd.Series):
    """
    Разделяет данные на train/validation/test,
    создает временные последовательности и возвращает DataLoader'ы.
    """
    # 1. Разделение исходных данных на обучающую и тестовую выборки (хронологически)
    # Используем меньший test_size для сохранения большего количества данных для обучения/валидации
    X_train_val_df, X_test_df, y_train_val_series, y_test_series = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_SEED, shuffle=False
    )

    print(f"Train/Validation X_df shape: {X_train_val_df.shape}, y_series shape: {y_train_val_series.shape}")
    print(f"Test X_df shape: {X_test_df.shape}, y_series shape: {y_test_series.shape}")

    # 2. Разделение Train+Validation на Train и Validation (хронологически!)
    # Валидационная выборка - это последние X% от train_val_series
    val_size = int(len(X_train_val_df) * VALIDATION_SPLIT_RATIO)
    # Убедимся, что val_size хотя бы 1, чтобы избежать пустых выборок
    val_size = max(1, val_size)

    X_train_df = X_train_val_df.iloc[:-val_size]
    y_train_series = y_train_val_series.iloc[:-val_size]
    X_val_df = X_train_val_df.iloc[-val_size:]
    y_val_series = y_train_val_series.iloc[-val_size:]

    print(f"\nTrain X_df shape: {X_train_df.shape}, y_series shape: {y_train_series.shape}")
    print(f"Validation X_df shape: {X_val_df.shape}, y_series shape: {y_val_series.shape}")
    
    # Очень важно: Проверить количество единиц в val и test наборах!
    print(f"Classes in y_train_series:\n{y_train_series.value_counts()}")
    print(f"Classes in y_val_series:\n{y_val_series.value_counts()}")
    print(f"Classes in y_test_series:\n{y_test_series.value_counts()}")


    # 3. Создание временных последовательностей
    X_train_sequences, y_train_sequences = create_sequences(X_train_df, y_train_series, SEQUENCE_LENGTH)
    X_val_sequences, y_val_sequences = create_sequences(X_val_df, y_val_series, SEQUENCE_LENGTH)
    X_test_sequences, y_test_sequences = create_sequences(X_test_df, y_test_series, SEQUENCE_LENGTH)

    print(f"\nShapes of generated sequences:")
    print(f"X_train_sequences: {X_train_sequences.shape}, y_train_sequences: {y_train_sequences.shape}")
    print(f"X_val_sequences: {X_val_sequences.shape}, y_val_sequences: {y_val_sequences.shape}")
    print(f"X_test_sequences: {X_test_sequences.shape}, y_test_sequences: {y_test_sequences.shape}")

    # 4. Преобразование в PyTorch тензоры
    X_train_tensor = torch.tensor(X_train_sequences, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train_sequences, dtype=torch.float32)
    X_val_tensor = torch.tensor(X_val_sequences, dtype=torch.float32)
    y_val_tensor = torch.tensor(y_val_sequences, dtype=torch.float32)
    X_test_tensor = torch.tensor(X_test_sequences, dtype=torch.float32)
    y_test_tensor = torch.tensor(y_test_sequences, dtype=torch.float32)

    # 5. Создание DataLoader'ов
    train_dataset = TimeSeriesDataset(X_train_tensor, y_train_tensor)
    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)

    val_dataset = TimeSeriesDataset(X_val_tensor, y_val_tensor)
    val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)

    test_dataset = TimeSeriesDataset(X_test_tensor, y_test_tensor)
    test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

    return train_loader, val_loader, test_loader, y_train_series # y_train_series нужен для расчета pos_weight