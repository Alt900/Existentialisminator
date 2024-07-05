import matplotlib.pyplot as plt
import numpy as np
print("What is your current age in years?")
CurrentWeek=int(int(input(">>> "))*52.1429)#year * weeks in a year
#based off a 90 year lifespan
Left = np.full(shape=(4624-CurrentWeek), fill_value=255)
Used = np.full(shape=(CurrentWeek), fill_value=0)
Total = np.concatenate((Used,Left))
Total = Total.reshape(68,68)
plt.imshow(Total,cmap='gray')
plt.title(f"{CurrentWeek} weeks out of 4624\n{4624-CurrentWeek} weeks left.")
plt.show()