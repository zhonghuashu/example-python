import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    dates, highs = [], []
    for row in reader: 
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

# OSError: 'seaborn' is not a valid package style, path of style file, URL of style file, or library style name (library styles are listed in `style.available`).
# plt.style.use('seaborn')
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red')
plt.title("Daily high temperaturs - 2018", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

# UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown plt.show()
# plt.show()
plt.savefig('data/myplot.png')