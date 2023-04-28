import pandas as pd

csv_file = pd.read_csv('sample_data/california_housing_test.csv')
print(csv_file[csv_file['population'] <= 500] ['median_house_value'])

print(f"Mаксимальная households в зоне минимального значения population равна: {csv_file[csv_file['population'] == csv_file['population'].min()] ['households'].min()}")