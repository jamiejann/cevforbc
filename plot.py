import csv
import time
import matplotlib.pyplot as plt

time_list = []
remaining_list = []
reserved_list = []
disbursed_list = []

with open(r'data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
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

plt.subplot(3, 1, 1)
plt.plot(time_list, remaining_list)
plt.title('Remaining Funds')
plt.gca().invert_yaxis()

plt.subplot(3, 1, 2)
plt.plot(time_list, reserved_list)
plt.title('Reserved Funds')

plt.subplot(3, 1, 3)
plt.plot(time_list, disbursed_list)
plt.title('Disbursed Funds')
plt.xlabel('time')

len_normalized = len(time_list) / 10
ax = plt.gca()

# showing only 10 x labels
for label in ax.get_xaxis().get_ticklabels():
    label.set_visible(False)
for label in ax.get_xaxis().get_ticklabels()[::len_normalized]:
    label.set_visible(True)

plt.gcf().autofmt_xdate()

plt.tight_layout()

plt.show()
