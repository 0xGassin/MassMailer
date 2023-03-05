import os
import pandas as pd

files = [f for f in os.listdir('.') if os.path.isfile(f)]
csvs = []

log_file = open("dupes.log", "a+")

for file in files:
    if(file.endswith('.csv')):
        csvs.append(file)

for csv in range(0, len(csvs)):
    counter = 0
    df = pd.read_csv(csvs[csv], sep=',', header=0)
    for row in range(0, len(df)):
        for k in range(0, len(df)):
            running = df['Contact'][row]
            comparison = df['Contact'][counter]
            if(running == comparison and row != counter):
                print('Found a Clash!', comparison, 'in row:', row, 'and in row:', counter)
                log_file.write(f"{df['Contact'][row]}\n")
            counter += 1
        counter = 0
    # print(df['Contact'][0])
log_file.close()

log_data = log_file.read()
print(log_data)
listed_data = log_data.split("@")
print(listed_data)