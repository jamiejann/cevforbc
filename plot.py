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

del time_list[0]
del remaining_list[0]
del reserved_list[0]
del disbursed_list[0]

plt.plot(time_list, remaining_list)
plt.gcf().autofmt_xdate()
plt.show()

plt.plot(time_list, reserved_list)
plt.gcf().autofmt_xdate()
plt.show()

plt.plot(time_list, disbursed_list)
plt.gcf().autofmt_xdate()
plt.show()

time.sleep(300)
