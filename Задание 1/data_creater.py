import pandas as pd
import numpy as np

# Установим начальные параметры
np.random.seed(42)
num_records = 1000

# Генерация дат
dates = pd.date_range(start='2023-01-01', periods=num_records, freq='H')
times = dates.time

# Генерация случайных данных
speeds = np.random.randint(0, 140, num_records)  # скорость от 0 до 140 км/ч
fuel_levels = np.random.uniform(0, 100, num_records)  # уровень топлива от 0 до 100%
ignition_status = np.random.choice(['on', 'off'], num_records)  # статус зажигания

# Создание DataFrame
data = {
    'date': dates.date,
    'time': times,
    'speed': speeds,
    'fuel_level': fuel_levels,
    'ignition_status': ignition_status
}
df = pd.DataFrame(data)

# Вставка дубликатов и ошибок для дальнейшей очистки
df.loc[10:20] = df.loc[0:10].values  # дубликаты
df.loc[30, 'speed'] = 999  # ошибка скорости
df.loc[40, 'fuel_level'] = -10  # ошибка уровня топлива

df.to_csv('data.csv', index=False)
