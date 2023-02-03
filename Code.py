import matplotlib.pyplot as plt
import numpy as np
Crop = ("Wheat", "Barley", "Rice", "Corn", "Soybean")
Production = [103, 122, 185, 118, 145]
fig, ax = plt.subplots()
ax.set_title('Crops production')
ax.set_ylabel('Production')
y_pos = np.arange(len(Crop))
plt.xticks(y_pos, Crop, rotation=45)
plt.bar(y_pos, Production)
plt.show()
