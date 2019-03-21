import csv
import matplotlib.pyplot as plt
from matplotlib import ticker
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

len_normalized_xaxis = len(time_list) / 10
len_normalized_yaxis = len(time_list) / 5

# initialize 3 by 1 plots, invert y axis for python misprint
plt.subplot(3, 1, 1)
plt.plot(time_list, remaining_list)
plt.title('Remaining Funds')
plt.gca().invert_yaxis()

# show only 5 y labels
ax = plt.gca()
#ax.yaxis.set_major_locator(ticker.maxNLocator(integer=True))
ax.set_yticks(ax.get_yticks()[::2])
#remaining_list.remove("")
#plt.yticks(max(remaining_list), min(remaining_list))


plt.subplot(3, 1, 2)
plt.plot(time_list, reserved_list)
plt.title('Reserved Funds')

ax = plt.gca()
for label in ax.get_yaxis().get_ticklabels():
    label.set_visible(False)
for label in ax.get_yaxis().get_ticklabels()[::len_normalized_yaxis]:
    label.set_visible(True)

plt.subplot(3, 1, 3)
plt.plot(time_list, disbursed_list)
plt.title('Disbursed Funds')
plt.xlabel('Time')

ax = plt.gca()



# show only 10 x labels
for label in ax.get_xaxis().get_ticklabels():
    label.set_visible(False)
for label in ax.get_xaxis().get_ticklabels()[::len_normalized_xaxis]:
    label.set_visible(True)

plt.gcf().autofmt_xdate()

plt.tight_layout()

plt.show()
