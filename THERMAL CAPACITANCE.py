
#CubeSat thermal node identification

# Define thermal nodes
nodes = [
    "Aluminium Enclosure",
    "Battery",
    "OBC",
    "EPS",
    "Internal Radiator"
]

# Mass of each node (kg)
mass = [0.32389184, 0.120, 0.040, 0.050, 0.040]

# Specific heat capacity (J/kg.K)
cp = [960, 900, 800, 850, 900]

# Calculate thermal capacitance
thermal_capacitance = []

for i in range(len(nodes)):
    C = mass[i] * cp[i]
    thermal_capacitance.append(C)

# Display results

print("-----CUBESAT THERMAL NODE PROPERTIES--------------------")


for i in range(len(nodes)):
    print(nodes[i], ":", round(thermal_capacitance[i], 2), "J/K")

print("---------------final RESULTS-----------------")
print("Total thermal capacitance:",
      round(sum(thermal_capacitance), 2), "J/K")
