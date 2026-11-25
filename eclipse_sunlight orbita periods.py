import numpy as np

#orbital parameters
mu = 3.986e14 # m^3/s^2
Re = 6371e3 # m
R = Re + 500e3 # m
Beta = 0 # deg                                                   (assuming equatorial orbit/circular orbit)

#ORBITAL PERIOD CALCULATION
T = 2 * np.pi * np.sqrt(R**3 / mu)                               # seconds

#ECLIPSE/SUNLIGHT DURATION CALCULATION
#calculate the critical angle for eclipse
theta = np.arcsin(Re / R)                                       # radians       eclipse angle
theta_deg = np.degrees(theta)                                   # degrees       eclipse angle in degrees

#calculate the eclipse duration
t_eclipse = (2 * theta / (2 * np.pi)) * T                        # seconds       eclipse duration

#calculate the sunlight duration
t_sunlight = T - t_eclipse                                      # seconds       sunlight duration

#minutes conversion

eclipse_duration = t_eclipse / 60                                 # minutes       eclipse duration
sunlight_duration = t_sunlight / 60                               # minutes       sunlight duration


#DISPLAYING RESULTS

print("ORBITAL PERIOD (T): ", round(T, 2), "seconds")
print("ECLIPSE DURATION: ", round(eclipse_duration, 2), "minutes")
print("SUNLIGHT DURATION: ", round(sunlight_duration, 2), "minutes")



# ********* S I M U L A T I O N   C O N D I T I O N S ************

#time step for simulation
#dt = 10 # seconds

#number of orbits to simulate
#orbits = 5
#Total_time = T * orbits # seconds