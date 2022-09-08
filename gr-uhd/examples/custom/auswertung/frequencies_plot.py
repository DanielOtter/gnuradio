import numpy as np
import matplotlib.pyplot as plt
import math

freq = np.array([2.35, 2.36, 2.37, 2.38, 2.39, 2.40, 2.41, 2.42, 2.43, 2.44, 2.45, 2.46, 2.47, 2.48, 2.49, 2.50, 2.51, 2.52, 2.53, 2.54, 2.55])
att = np.array([-36.32, -8.17, -7.81, -7.46, -7.37, -7.21, -7.10, -7.10, -6.99, -6.99, -6.88, -6.99, -6.99, -7.10, -7.10, -7.28, -7.48, -7.81, -8.14, -8.36, -36.84])

# Plot freq x att
plt.plot(freq, att)
plt.ylim(-40,0)
plt.xlabel("Frequencies in GHz")
plt.ylabel("Attenuation in dB")
plt.savefig('frequencies_plot.png')
plt.show()