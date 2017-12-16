import matplotlib.pyplot as plt

x_values = list(range(1, 100))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, edgecolor='none', s=10)
#set chart title and label axes
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
#set range for each axis
plt.axis([0, 101, 0, 10001])
plt.show()
