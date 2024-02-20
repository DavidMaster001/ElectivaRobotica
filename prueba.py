import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 6, 100)
y1 = np.zeros_like(x)
y2 = np.zeros_like(x)
y3 = np.zeros_like(x)
y4 = np.zeros_like(x)
y5 = np.zeros_like(x)

# Draw the letters of the name "DAVID"
for i in range(len(x)):
    if 0.5 <= x[i] <= 1.5:
        y1[i] = 0.5
    elif 1.5 <= x[i] <= 2.5:
        y2[i] = 0.5
    elif 2.5 <= x[i] <= 3.5:
        y3[i] = 0.5
    elif 3.5 <= x[i] <= 4.5:
        y4[i] = 0.5
    elif 4.5 <= x[i] <= 5.5:
        y5[i] = 0.5

# Plot the letters
plt.plot(x, y1, color="blue", linewidth=2, linestyle="-")
plt.plot(x, y2, color="blue", linewidth=2, linestyle="-")
plt.plot(x, y3, color="blue", linewidth=2, linestyle="-")
plt.plot(x, y4, color="blue", linewidth=2, linestyle="-")
plt.plot(x, y5, color="blue", linewidth=2, linestyle="-")

# Add the labels for the letters
plt.text(0.75, 0.6, "D", fontsize=20, ha="center", va="center")
plt.text(2, 0.6, "A", fontsize=20, ha="center", va="center")
plt.text(3.25, 0.6, "V", fontsize=20, ha="center", va="center")
plt.text(4.5, 0.6, "I", fontsize=20, ha="center", va="center")
plt.text(5.75, 0.6, "D", fontsize=20, ha="center", va="center")

# Set the limits of the plot
plt.xlim(-1, 6)
plt.ylim(-0.5, 1.5)

# Remove the spines of the plot
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_position(("outward", 10))
plt.gca().spines["left"].set_position(("outward", 10))

# Add gridlines
plt.grid(True, linestyle="--", linewidth=0.5)

# Add a title
plt.title("Name: DAVID", fontsize=20, y=1.05)

# Show the plot
plt.show()