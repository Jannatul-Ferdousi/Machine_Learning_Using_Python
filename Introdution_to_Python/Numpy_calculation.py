height_in = [71, 74, 72, 73, 76,  70, 75, 70, 72, 77, 79, 78, 74, 75, 75, 78, 76, 75, 69, 75, 72, 75, 73, 74, 75, 75, 73]
weight_lb = [195, 219, 190, 197, 200, 195, 210, 177, 220, 235, 180, 195, 195, 190, 230, 190, 200, 190, 190, 200, 200, 184,
             200, 180, 219, 187, 200]
# height and weight are available as regular lists
print(len(height_in))
print(len(weight_lb))
# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = 0.453592*np.array(weight_lb)

# Calculate the BMI: bmi
bmi = np_weight_kg/np_height_m**2

# Print out bmi
print(bmi)

# Create the light array
light = bmi<21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# Print out the weight at index 50
print(np_weight_kg[5])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_m[20:])

