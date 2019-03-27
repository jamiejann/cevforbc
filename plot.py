import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

time_list = []
remaining_list = []
reserved_list = []
disbursed_list = []

with open(r'data.csv', 'r') as data:
    plots = csv.reader(data, delimiter=',')
    for row in plots:
        time_list.append(row[0])
        remaining_list.append(row[1])
        reserved_list.append(row[2])
        disbursed_list.append(row[3])

# delete headers from csv file, can be more efficient?
del time_list[0]
del remaining_list[0]
del reserved_list[0]
del disbursed_list[0]

# initialize 3 by 1 plots, invert y axis for python misprint
plt.subplot(3, 1, 1)
plt.plot(time_list, remaining_list)
plt.title('Remaining Funds')
plt.gca().invert_yaxis()

# y-axis normalization
ax = plt.gca()
ylocator = MaxNLocator(prune="both", nbins=5)
ax.yaxis.set_major_locator(ylocator)

plt.subplot(3, 1, 2)
plt.plot(time_list, reserved_list)
plt.title('Reserved Funds')

ax = plt.gca()
ylocator = MaxNLocator(prune="both", nbins=5)
ax.yaxis.set_major_locator(ylocator)

plt.subplot(3, 1, 3)
plt.plot(time_list, disbursed_list)
plt.title('Disbursed Funds')
plt.xlabel('Time')

# y-axis normalization
ax = plt.gca()
ylocator = MaxNLocator(prune="both", nbins=5)
ax.yaxis.set_major_locator(ylocator)


# x-axis normalization
xlocator = MaxNLocator(prune = "both", nbins=10)
ax.xaxis.set_major_locator(xlocator)

# prettify dates
plt.gcf().autofmt_xdate()
plt.tight_layout()

plt.show()
