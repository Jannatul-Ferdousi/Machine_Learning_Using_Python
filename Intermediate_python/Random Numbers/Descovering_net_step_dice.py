# Numpy is imported, seed is set
import numpy as np
np.random.seed(123)
# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)
print(dice)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif 3<=dice<=5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)