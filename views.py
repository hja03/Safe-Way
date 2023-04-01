from flask import Blueprint, render_template, redirect, url_for, request, make_response, flash
from database import *
import folium
import folium.plugins as plugins
import pandas as pd

core = Blueprint('core', __name__, template_folder='templates')

# @core.route("/")

# def index():
#     return render_template('index.html')



### Simple example of a fullscreen map.

@core.route("/")

def fullscreen():

    data = pd.read_csv('Bath_Police_Data.csv')
    locations = zip( data['Latitude'], data['Longitude'] )

    m = folium.Map(location=[51.37879, -2.32358], tiles='OpenStreetMap', zoom_start=13)

    plugins.HeatMap(locations, min_opacity=0.4, max_zoom=13).add_to(m)


    return m.get_root().render()

@core.route("/iframe")
def iframe():
    """Embed a map as an iframe on a page."""
    m = folium.Map()

    # set the iframe width and height
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>Using an iframe</h1>
                    {{ iframe|safe }}
                </body>
            </html>
        """,
        iframe=iframe,
    )


@core.route("/components")
def components():
    """Extract map components and put those on a page."""
    m = folium.Map(
        width=800,
        height=600,
    )

    m.get_root().render()
    header = m.get_root().header.render()
    body_html = m.get_root().html.render()
    script = m.get_root().script.render()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head>
                    {{ header|safe }}
                </head>
                <body>
                    <h1>Using components</h1>
                    {{ body_html|safe }}
                    <script>
                        {{ script|safe }}
                    </script>
                </body>
            </html>
        """,
        header=header,
        body_html=body_html,
        script=script,
    )