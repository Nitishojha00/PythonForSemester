import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D']
y = [10,14,11,12]
# .barh krdiya to horizontally hojayega
plt.bar(x, y, color='green')

plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Bar Chart: X vs Y")

plt.show()
