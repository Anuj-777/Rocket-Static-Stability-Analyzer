import matplotlib.pyplot as plt


def draw_rocket(length, cg, cp, margin, status):
    plt.figure(figsize=(10, 2))
    plt.text(
    length/2,
    0.22,
    f"Static Margin = {margin:.2f} calibers",
    ha="center",
    fontsize=10
    )  
    plt.text(
    length/2,
    -0.18,
    f"Status : {status}",
    color="green",
    fontsize=14,
    ha="center",
    fontweight="bold"
)
    # Rocket body
    plt.plot([0, length], [0, 0],
         linewidth=8,
         color="dimgray")

    # Nose
    plt.plot([length, length + 0.08], [0, 0.05], linewidth=3)
    plt.plot([length, length + 0.08], [0, -0.05], linewidth=3)
    plt.text(length + 0.04, 0.07, "Nose", ha="center", fontsize=10)
    
    # Tail fins
    plt.plot([0, -0.06], [0, 0.05], linewidth=3)
    plt.plot([0, -0.06], [0, -0.05], linewidth=3)
    plt.text(-0.08, 0.07, "Tail Fins", ha="center", fontsize=10)

    # Center of Gravity
    plt.scatter(cg, 0, s=180, color="blue", zorder=5,label="Center of Gravity (CG)")
    
  
    # Center of Pressure
    plt.scatter(cp, 0, s=180, color="red", zorder=5,label="Center of Pressure (CP)")
    

    plt.title(
    "Rocket Stability Visualization",
    fontsize=20,
    fontweight="bold",
    pad=20
)

    plt.xlim(-0.3,length+0.3)
    plt.ylim(-0.15,0.25)

    plt.axis("off")

    plt.grid(False)

    plt.savefig("screenshots/rocket_visualization.png", dpi=300)
    plt.legend(loc="upper right")
    plt.show()