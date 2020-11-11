# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars)
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])

# Print out drives_right value of Morocco
#print(cars)
print(cars.loc[['MOR'], 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'cars_per_cap']])
# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap', 'drives_right']])