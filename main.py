import csv
import pandas as pd

csv_file = pd.read_csv('sample_data/california_housing_test.csv')
print(csv_file['median_house_value'].mean())

