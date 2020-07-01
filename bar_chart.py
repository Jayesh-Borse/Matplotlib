import matplotlib.pyplot as plt

y_views = [123,234,456,111,678,567,900]
f_views = [234,456,567,123,345,789,890]
days = range(1,8)

plt.bar([a-0.25 for a in days],y_views,label = 'Youtube Views',width = 0.25, align = 'edge')
plt.bar([a+0.25 for a in days],f_views,label = 'Facebook Views', width = -0.25, align = 'edge')
plt.xlabel("Day No.")
plt.ylabel("Views")
plt.legend(loc = 'upper left')
plt.title('Youtube Views on daily basis')
# plt.grid(True, linewidth = 1, linestyle = '-.', color = 'r')
plt.savefig('D:\PythonC\my_stuff\Matplotlib\chart.png')
plt.show()
