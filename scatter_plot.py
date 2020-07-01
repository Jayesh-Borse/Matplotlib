import matplotlib.pyplot as plt

y_views = [123,234,456,111,678,567,900]

days = range(1,8)

plt.scatter(days,y_views,label = 'Youtube Views', color = 'r', marker = 'o', linestyle = '--', linewidth = 2)
plt.xlabel("Day No.")
plt.ylabel("Views")
plt.legend(loc = 'upper left')
plt.title('Youtube Views on daily basis')
# plt.grid(True, linewidth = 1, linestyle = '-.', color = 'r')
plt.savefig('D:\PythonC\my_stuff\Matplotlib\scatter_plot.png')
plt.show()
