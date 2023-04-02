from flask import Blueprint, render_template, request
import folium
import folium.plugins as plugins
import pandas as pd
import numpy as np

core = Blueprint('core', __name__, template_folder='templates')

def format_date(month, year):
    months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'Novemeber', 'December']
    return months[int(month)-1] + ', ' + year

def random_range(lower, upper):
    absolute_range = np.abs(upper - lower)
    return (np.random.rand() * absolute_range) - absolute_range/2

@core.route("/historical", methods=['GET', 'POST'])

def historical():

    if request.method == "POST":
        print(request.form)

    m = folium.Map(location=[51.38, -2.3785], tiles='OpenStreetMap', zoom_start=13)

    month, year = request.args.values()

    data = pd.read_csv('Bath_Police_Data.csv')
    search = '01'+'/'+month.zfill(2)+'/'+year
    applicable_rows = data.loc[data['Month'] == search]

    tl = (51.41, -2.428)
    br = (51.35, -2.329)
    folium.Rectangle([tl, br]).add_to(m)

    locations = zip( applicable_rows['Latitude'], applicable_rows['Longitude'] )
    plugins.HeatMap(locations, min_opacity=0.4, max_zoom=13).add_to(m)

    iframe = m.get_root()._repr_html_()
    return render_template("index.html", iframe=iframe, date=format_date(month, year), mode="Historical")


@core.route("/ml", methods=['GET', 'POST'])

def ml():

    if request.method == "POST":
        print(request.form)

    m = folium.Map(location=[51.38, -2.3785], tiles='OpenStreetMap', zoom_start=13)

    month, year = request.args.values()

    month_year = np.load("month_year.npy")
    all_data = np.load("all_data.npy")

    # print(month_year)

    index = np.where(month_year == [int(month), int(year)])[0][0]
    data = all_data[index]
    # print(data)

    locations = []

    tl = (51.41, -2.428)
    br = (51.35, -2.329)
    density = 50

    lat_step = ( tl[0] - br[0] ) / density
    lon_step = ( br[1] - tl[1] ) / density

    for r, row in enumerate(data):
        for p, pixel in enumerate(row):
            lat = tl[0] - (lat_step * r)
            lon = tl[1] + (lon_step * p)
            count = int(np.ceil( 27 * pixel ))
            for _ in range(count):
                lat_noise = random_range(-0.5 * lat_step, 0.5 * lat_step)
                lon_noise = random_range(-0.5 * lon_step, 0.5 * lon_step)
                locations.append([lat + lat_noise, lon + lon_noise])

    tl = (51.41, -2.428)
    br = (51.35, -2.329)
    folium.Rectangle([tl, br]).add_to(m)

    plugins.HeatMap(locations, min_opacity=0.4, max_zoom=13).add_to(m)

    iframe = m.get_root()._repr_html_()
    return render_template("index.html", iframe=iframe, date=format_date(month, year), mode="ML")


