import numpy as np
import matplotlib.pyplot as plt

# Nominal parameters
VT0 = 0.40  # V, nominal threshold voltage
L0 = 45  # nm, nominal channel length
tox0 = 1.2  # nm, nominal oxide thickness

# Process variations (1-sigma)
sigma_L = 2  # nm
sigma_tox = 0.1  # nm
sigma_RDF = 0.03  # V

# Sensitivity coefficients
k_L = -0.005  # V/nm (DIBL effect) Drain-induced barrier lowering
k_ox = 0.08  # V/nm

# Monte Carlo samples
N = 100_000

# Random sampling
L = np.random.normal(L0, sigma_L, N)
tox = np.random.normal(tox0, sigma_tox, N)
RDF = np.random.normal(0, sigma_RDF, N)  # Random dopand fluctuation

# VT computation
VT = VT0 + k_L * (L - L0) + k_ox * (tox - tox0) + RDF

# Statistics
print("Mean VT =", np.mean(VT))
print("Std VT  =", np.std(VT))

# Visualization
plt.hist(VT, bins=100, density=True)
plt.xlabel("VT (V)")
plt.ylabel("Probability Density Function")
plt.title("Monte Carlo Threshold Voltage Variation")
plt.show()