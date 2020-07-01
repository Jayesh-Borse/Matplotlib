import matplotlib.pyplot as plt

y_views = [123,234,456,111,678,567,900]
f_views = [234,456,567,123,345,789,890]
t_views = [456,567,890,900,234,568,458]

days = range(1,8)

plt.plot(days,y_views,label = 'Youtube Views', color = 'r', marker = 'o', linestyle = '--', linewidth = 2)
plt.plot(days,f_views,label = 'Facebook Views', color = 'g', marker = 'o', linestyle = '-.', linewidth = 2)
plt.plot(days,t_views,label = 'Twitter Views', color = 'b', marker = 'o', linewidth = 2)
plt.xlabel("Day No.")
plt.ylabel("Views")
plt.legend(loc = 'upper left')
plt.title('Youtube Views on daily basis')
plt.xlim(1,6)  #see data in particular limit
plt.ylim(100,1000)    #see data in particular limit
plt.grid(True, linewidth = 1, linestyle = '-.', color = 'r')
plt.savefig('D:\PythonC\my_stuff\Matplotlib\plot.png')
plt.show()
