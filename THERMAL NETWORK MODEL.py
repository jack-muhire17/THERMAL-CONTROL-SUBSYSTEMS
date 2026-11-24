import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Define the thermal nodes
nodes = {
    "N1": {"name": "Aluminium Structure", "C": 450},
    "N2": {"name": "OBC", "C": 80},
    "N3": {"name": "Battery", "C": 450},
    "N4": {"name": "EPS", "C": 120},
    "N5": {"name": "Communication", "C": 100},
    "N6": {"name": "External Panel", "C": 200}
}

# Define node positions
positions = {
    "N1": (0, 0),
    "N2": (-2, 2),
    "N3": (0, 2),
    "N4": (2, 2),
    "N5": (2, -1),
    "N6": (-2, -1)
}

# Conductive connections
conductive_links = [
    ("N1", "N2"),
    ("N1", "N3"),
    ("N1", "N4"),
    ("N1", "N5"),
    ("N1", "N6")
]

# Radiative connections
radiative_links = [
    ("N2", "N3"),
    ("N2", "N4"),
    ("N3", "N5")
]

fig, ax = plt.subplots(figsize=(12, 8))

# Draw conductive connections
for a, b in conductive_links:
    x1, y1 = positions[a]
    x2, y2 = positions[b]

    ax.plot(
        [x1, x2], [y1, y2],
        color="blue", linewidth=2,
        label="Conduction" if a == "N1" and b == "N2"
        else ""
    )

# Draw radiative connections
for a, b in radiative_links:
    x1, y1 = positions[a]
    x2, y2 = positions[b]

    ax.plot(
        [x1, x2], [y1, y2],
        color="red", linestyle="--",
        linewidth=2,
        label="Radiation" if (a, b) == ("N2", "N3")
        else ""
    )

# Draw thermal nodes
for node, data in nodes.items():
    x, y = positions[node]

    box = FancyBboxPatch(
        (x - 0.65, y - 0.3),
        1.3, 0.6,
        boxstyle="round,pad=0.1",
        facecolor="lightblue",
        edgecolor="black"
    )

    ax.add_patch(box)

    ax.text(
        x, y,
        f"{node}\n{data['name']}\nC={data['C']} J/K",
        ha="center", va="center",
        fontsize=8
    )

# External space boundary
ax.text(
    -3.2, -1,
    "SPACE\nRadiative heat loss",
    ha="center", va="center",
    fontsize=10
)

x, y = positions["N6"]

ax.annotate(
    "",
    xy=(x - 0.7, y),
    xytext=(-2.6, y),
    arrowprops=dict(arrowstyle="->", color="red")
)

# Solar input
ax.annotate(
    "Solar input",
    xy=(-2, -0.65),
    xytext=(-3, -0.2),
    arrowprops=dict(arrowstyle="->", color="orange"),
    color="darkorange"
)

ax.set_title("Simplified 3U CubeSat Thermal Network")
ax.set_xlim(-4, 3.5)
ax.set_ylim(-2, 3)
ax.set_aspect("equal")
ax.axis("off")
ax.legend(loc="upper right")

plt.savefig(
    "CubeSat_Thermal_Network.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()