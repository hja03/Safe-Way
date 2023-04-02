from flask import Blueprint, render_template, request
import folium
import folium.plugins as plugins
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

month_year = []
all_data = []

for year in range (2020, 2024):
    for month in range(1, 13):

        year = str(year)
        month = str(month)

        data = pd.read_csv('Bath_Police_Data.csv')
        search = '01'+'/'+month.zfill(2)+'/'+year
        applicable_rows = data.loc[data['Month'] == search]

        locations = zip( applicable_rows['Latitude'], applicable_rows['Longitude'] )

        buckets = np.zeros((50,50))

        tl = (51.41, -2.428)
        br = (51.35, -2.329)

        density = 50

        lat_step = np.abs( tl[0] - br[0] ) / density
        lon_step = np.abs( br[1] - tl[1] ) / density

        for lat, lon in locations:

            lat_box = ( tl[0] - lat ) // lat_step

            if lat_box < 0 or lat_box > 49:
                continue

            lon_box = ( lon - tl[1] ) // lon_step

            if lon_box < 0 or lon_box > 49:
                continue

            buckets[int(lat_box), int(lon_box)] += 1

        month_year.append([int(month), int(year)    ])
        all_data.append(buckets)

month_year = np.array(month_year)
all_data = np.array(all_data)

# print([np.amax(a) for a in all_data])

# normalise
for a_d in all_data:
    max_value = np.amax(a_d)
    a_d /= max_value

print(month_year.shape)
print(all_data.shape)

month_year = month_year[2:-10]
all_data = all_data[2:-10]

# print(month_year[0])

# plt.imshow(all_data[0])
# plt.show()

np.save("month_year", month_year)
np.save("all_data", all_data)

