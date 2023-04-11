
import numpy as np
import pywt
import matplotlib.pyplot as plt

# Load ocean data
data = np.loadtxt('ocean_data.txt')

# Define the wavelet function
wavelet = 'morl'

# Perform the continuous wavelet transform
coeffs, freqs = pywt.cwt(data, np.arange(1, 51), wavelet)

# Plot the scaleogram
plt.figure(figsize=(8, 6))
plt.imshow(np.abs(coeffs), extent=[1, len(data), freqs[-1], freqs[0]],
           cmap='jet', aspect='auto', interpolation='nearest')
plt.colorbar()
plt.title('Wavelet Scaleogram of Ocean Data')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()
