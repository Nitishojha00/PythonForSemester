import matplotlib.pyplot as plt  # ✅ required import

x = [ 2, 3, 4]
y = [ 2, 3, 4]

plt.fill_between(x, y) # fill_between ✅
# labels and title
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line Plot: Relationship between X and Y")
# grid

plt.grid(True)
# show plot
plt.show()
