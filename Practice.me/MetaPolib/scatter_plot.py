import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 1, 4, 3, 5]

plt.scatter(x, y, color='red', marker='*')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Scatter Plot: X vs Y")


plt.show()
