import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# -----------------------------------
# 1. Define thermal network parameters
# -----------------------------------

# Thermal capacitances (J/K)
C1 = 1200.0
C2 = 5000.0

# Thermal conductance between nodes (W/K)
K12 = 2.0

# Heat generated at each node (W)
Q1 = 8.0
Q2 = 0.0

# Radiating surface properties
epsilon1 = 0.8
epsilon2 = 0.8

A1 = 0.02  # m^2
A2 = 0.10  # m^2

# Stefan-Boltzmann constant
sigma = 5.67e-8  # W/(m^2 K^4)

# Space temperature (K)
T_space = 3.0

# -----------------------------------
# 2. Define the mathematical equations
# -----------------------------------

def thermal_model(t, T):

    # Temperatures of the two nodes
    T1 = T[0]
    T2 = T[1]

    # Heat conducted between nodes
    Q12 = K12 * (T2 - T1)

    # Radiation heat transfer
    Qrad1 = epsilon1 * sigma * A1 * (
        T1**4 - T_space**4
    )

    Qrad2 = epsilon2 * sigma * A2 * (
        T2**4 - T_space**4
    )

    # Energy balance for Node 1
    dT1_dt = (Q1 + Q12 - Qrad1) / C1

    # Energy balance for Node 2
    dT2_dt = (Q2 - Q12 - Qrad2) / C2

    # Return temperature rates
    return [dT1_dt, dT2_dt]

# -----------------------------------
# 3. Initial conditions
# -----------------------------------

T_initial = [293.0, 293.0]  # K

# Time: 0 to 10 hours
t_start = 0
t_end = 10 * 3600

time_points = np.linspace(
    t_start, t_end, 500
)

# -----------------------------------
# 4. Solve the differential equations
# -----------------------------------

solution = solve_ivp(
    thermal_model,
    (t_start, t_end),
    T_initial,
    t_eval=time_points
)

# -----------------------------------
# 5. Extract results
# -----------------------------------

time_hours = solution.t / 3600

T1 = solution.y[0]
T2 = solution.y[1]

# Convert Kelvin to Celsius
T1_C = T1 - 273.15
T2_C = T2 - 273.15

# -----------------------------------
# 6. Display final temperatures
# -----------------------------------

print("Final temperature of Node 1:",
      round(T1_C[-1], 2), "°C")

print("Final temperature of Node 2:",
      round(T2_C[-1], 2), "°C")

# -----------------------------------
# 7. Plot temperature versus time
# -----------------------------------

plt.figure(figsize=(9, 5))

plt.plot(time_hours, T1_C,
         label="Node 1 - Electronics")

plt.plot(time_hours, T2_C,
         label="Node 2 - Structure")

plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.title("Two-Node Thermal Network")

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()