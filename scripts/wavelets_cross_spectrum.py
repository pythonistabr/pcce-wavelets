
import numpy as np
import matplotlib.pyplot as plt
import pywt

# Load data
ocean_data = np.loadtxt('ocean_currents.txt')
wind_data = np.loadtxt('wind.txt')

# Define wavelet parameters
dt = 1 # Time step of 1 hour
scales = range(1, 65) # Wavelet scales
wavelet = 'morl' # Mother wavelet function

# Perform wavelet analysis
coefs_ocean, frequencies_ocean = pywt.cwt(ocean_data, scales, wavelet, dt)
coefs_wind, frequencies_wind = pywt.cwt(wind_data, scales, wavelet, dt)

# Calculate wavelet cross spectrum
cross_spectrum = coefs_ocean * np.conj(coefs_wind)

# Plot wavelet cross spectrum
plt.pcolormesh(np.real(cross_spectrum), cmap='jet')
plt.colorbar()
plt.title('Wavelet Cross-Spectrum between Ocean Currents and Wind Velocity')
plt.xlabel('Time (hours)')
plt.ylabel('Wavelet Scale')
plt.show()
