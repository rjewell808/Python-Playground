import json
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

with open('message.json') as file:
    data = json.load(file)

dates = {}

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 1

for x in range(1,7):
    for y in range(1, months[x - 1] + 1):
        dates[str(x).zfill(2)+"-"+str(y).zfill(2)] = 0

for message in data['messages']:
    date = time.strftime('%m-%d', time.localtime(message['timestamp']))

    if date not in dates:
        dates[date] = 1
    else:
        dates[date] += 1

    if "02-" in date and 'content' in message:
        print(date + ": " + message['content'])

def label(x, pos):
    if x % 11 == 0 or x == len(dates) - 1:
        return tuple(dates.keys())[pos]

    return ""

formatter = FuncFormatter(label)

x_range = np.arange(len(dates))

fig, ax = plt.subplots()

plt.bar(x_range, dates.values())
plt.xticks(x_range, tuple(dates.keys()))

ax.get_xaxis().set_major_formatter(formatter)

plt.show()