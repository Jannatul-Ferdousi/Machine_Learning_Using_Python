# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = str(row['country'].upper())
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)
