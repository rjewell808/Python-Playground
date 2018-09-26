import json
import time

with open('message.json') as file:
    data = json.load(file)

dates = {}

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 1

for x in range(2,9+1):
    for y in range(1, months[x - 1] + 1):
        dates[str(x).zfill(2) + "-" + str(y).zfill(2)] = 0

print(len(dates))

for message in data['messages']:
    date = time.strftime('%m-%d', time.localtime(message['timestamp_ms'] / 1000))

    if date not in dates:
        dates[date] = 1
    else:
        dates[date] += 1


f = open("file.txt", "w")
for x in dates.values():
    f.write(str(x) + "\n")
f.close()