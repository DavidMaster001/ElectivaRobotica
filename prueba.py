import matplotlib.pyplot as plt

# Create a new figure
fig, ax = plt.subplots()

# Set the size of the figure
fig.set_size_inches(5, 2)

# Remove the spines (i.e., the lines around the edges) of the plot
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Set the x and y limits of the plot
ax.set_xlim(-1, 9)
ax.set_ylim(-2, 5)

# Draw the letters of the name "DAVID"
ax.text(1, 1, "D", ha='center', va='center')
ax.text(2, 1, "A", ha='center', va='center')
ax.text(3, 1, "V", ha='center', va='center')
ax.text(4, 1, "I", ha='center', va='center')
ax.text(5, 1, "D", ha='center', va='center')

ax.text(1, 2, "D", ha='center', va='center')
ax.text(2, 2, "I", ha='center', va='center')
ax.text(3, 2, "L", ha='center', va='center')
ax.text(4, 2, "A", ha='center', va='center')
ax.text(5, 2, "N", ha='center', va='center')

ax.text(1, 3, "A", ha='center', va='center')
ax.text(2, 3, "D", ha='center', va='center')
ax.text(3, 3, "R", ha='center', va='center')
ax.text(4, 3, "I", ha='center', va='center')
ax.text(5, 3, "A", ha='center', va='center')
ax.text(6, 3, "N", ha='center', va='center')
ax.text(7, 3, "A", ha='center', va='center')

# Remove the tick marks from the plot
ax.set_xticks([])
ax.set_yticks([])

# Show the plot
plt.show()
