import matplotlib.pyplot as plt

y_views = [123,234,456,111,678,567,900,850,342]
days = range(1,10)
bins = [100,200,300,400,500,600,700,800,900,1000]

plt.hist(y_views,bins,label = 'Youtube Views')

plt.xlabel("Day No.")
plt.ylabel("Views")
plt.legend(loc = 'upper left')
plt.title('Youtube Views on daily basis')
plt.grid(True, linewidth = 1, linestyle = '-.')
plt.xticks(bins)
plt.savefig('D:\PythonC\my_stuff\Matplotlib\histogram.png')
plt.show()
