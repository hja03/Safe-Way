from flask import Blueprint, render_template
from database import *
import folium
import folium.plugins as plugins
import pandas as pd

core = Blueprint('core', __name__, template_folder='templates')


@core.route("/")
def index():

    m = folium.Map(location=[51.37879, -2.32358], tiles='OpenStreetMap', zoom_start=13)

    data = pd.read_csv('Bath_Police_Data.csv')
    locations = zip( data['Latitude'], data['Longitude'] )

    plugins.HeatMap(locations, min_opacity=0.4, max_zoom=13).add_to(m)

    # set the iframe width and height
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template("index.html", iframe=iframe)


