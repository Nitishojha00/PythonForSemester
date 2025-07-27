import matplotlib.pyplot as plt

x = [1,2,3]
y = [1,2,3]

plt.plot(x,y,color='red', marker="*

")

# labeling
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graph")
# grid
plt.grid(True)
# show
plt.show()
