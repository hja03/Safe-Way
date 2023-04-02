from flask import Blueprint, render_template
from database import *
import folium
import folium.plugins as plugins
import pandas as pd
from folium.plugins import PolyLineTextPath

core = Blueprint('core', __name__, template_folder='templates')


@core.route("/")
def index():

    m = folium.Map(location=[51.37879, -2.32358], tiles='OpenStreetMap', zoom_start=13)

    data = pd.read_csv('Bath_Police_Data.csv')
    locations = zip( data['Latitude'], data['Longitude'] )
    # gradient = {0.1: 'pink', 1: 'red'}
    # plugins.HeatMap(locations, min_opacity=0.1, max_opactiy=0.4, gradient=gradient, control=True, scale_radius=True, radius=40, blur=25, overlay=True, max_zoom=13).add_to(m)

    # Destination = folium.Marker(location=[51.3804147, -2.3815838], popup="64 Brook Rd, Bath BA2 3RR, UK")
    # # Location = folium.Marker(location=[51.3782228, -2.3263987], popup="University of Bath, UK")
    # Labyrinth = folium.Marker(location=[51.380679, -2.3567243], popup="University of Bath, UK")
    # Destination.add_to(m)
    # Labyrinth.add_to(m)

    starting_location = [51.380679, -2.3567243]
    ending_location = [51.3804147, -2.3815838]
    route = [[-2.381428, 51.380438], [-2.38143, 51.380442], [-2.381321, 51.380443], [-2.380219, 51.380377], [-2.379809, 51.380327], [-2.379739, 51.380613], [-2.379681, 51.380715], [-2.37834, 51.380617], [-2.378301, 51.380641], [-2.378253, 51.380694], [-2.37821, 51.380747], [-2.378156, 51.380818], [-2.377985, 51.380846], [-2.377698, 51.380896], [-2.377379, 51.381571], [-2.377032, 51.381523], [-2.376876, 51.381504], [-2.376788, 51.382114], [-2.376719, 51.382545], [-2.376515, 51.382515], [-2.376282, 51.382477], [-2.375656, 51.382379], [-2.374997, 51.382276], [-2.374738, 51.382235], [-2.374298, 51.382172], [-2.373886, 51.382119], [-2.373791, 51.382102], [-2.373762, 51.382185], [-2.373384, 51.382146], [-2.373253, 51.382151], [-2.371278, 51.382218], [-2.371281, 51.38218], [-2.371269, 51.382139], [-2.371173, 51.382103], [-2.37111, 51.382094], [-2.371024, 51.382067], [-2.370784, 51.381933], [-2.370217, 51.381578], [-2.37014, 51.381505], [-2.370124, 51.381396], [-2.370094, 51.38139], [-2.369349, 51.381412], [-2.36918, 51.381428], [-2.369149, 51.38141], [-2.369106, 51.381419], [-2.368686, 51.381436], [-2.368441, 51.38145], [-2.368383, 51.381455], [-2.368259, 51.381477], [-2.368233, 51.381479], [-2.368184, 51.381483], [-2.368182, 51.381453], [-2.368127, 51.38145], [-2.368035, 51.381421], [-2.36783, 51.38143], [-2.367789, 51.381373], [-2.367693, 51.381373], [-2.367678, 51.381373], [-2.366242, 51.381413], [-2.366225, 51.381414], [-2.366178, 51.381425], [-2.366024, 51.38149], [-2.365912, 51.381459], [-2.365899, 51.381475], [-2.365869, 51.381513], [-2.365824, 51.38156], [-2.365582, 51.381484], [-2.365093, 51.3813], [-2.364939, 51.381245], [-2.364335, 51.380998], [-2.364008, 51.380857], [-2.363895, 51.380808], [-2.363788, 51.380913], [-2.363746, 51.380975], [-2.363676, 51.381049], [-2.363639, 51.381114], [-2.363584, 51.381194], [-2.363536, 51.381229], [-2.363226, 51.381391], [-2.363168, 51.381395], [-2.363147, 51.381389], [-2.362954, 51.381323], [-2.362923, 51.381296], [-2.36288, 51.381318], [-2.362864, 51.381301], [-2.362857, 51.381219], [-2.362826, 51.381215], [-2.362816, 51.381251], [-2.362769, 51.38127], [-2.362542, 51.381268], [-2.362558, 51.381289], [-2.362714, 51.381353], [-2.362653, 51.381357], [-2.362574, 51.381359], [-2.362465, 51.38136], [-2.36235, 51.381371], [-2.361628, 51.38143], [-2.361586, 51.381201], [-2.361582, 51.381007], [-2.361571, 51.380905], [-2.361507, 51.380908], [-2.36143, 51.380901], [-2.361349, 51.380873], [-2.361222, 51.380807], [-2.361188, 51.380776], [-2.360767, 51.380836], [-2.360382, 51.380895], [-2.360356, 51.380865], [-2.360263, 51.380813], [-2.360185, 51.380793], [-2.360142, 51.380793], [-2.360111, 51.380719], [-2.359958, 51.380746], [-2.359765, 51.380782], [-2.359219, 51.38089], [-2.359161, 51.3809], [-2.359138, 51.380906], [-2.358828, 51.38096], [-2.358795, 51.380965], [-2.358589, 51.380983], [-2.357869, 51.381026], [-2.35775, 51.381003], [-2.357745, 51.380965], [-2.357723, 51.38094], [-2.357686, 51.380915], [-2.357475, 51.380871], [-2.35733, 51.380844], [-2.357202, 51.380816], [-2.357017, 51.380818], [-2.356944, 51.380818], [-2.356731, 51.380822]]
    newRoute = []
    for r in route:
        r.reverse()
        newRoute.append(r)

    m = folium.Map(location=starting_location, zoom_start=12)
    polyline = folium.PolyLine(locations=newRoute, weight=5, color='blue')
    polyline.add_to(m)

    folium.Marker(location=starting_location, popup='Start').add_to(m)
    folium.Marker(location=ending_location, popup='End').add_to(m)
    text = 'Route'
    text_path = PolyLineTextPath(polyline, text)
    text_path.add_to(m)

    gradient = {0.1: 'pink', 1: 'red'}
    plugins.HeatMap(locations, min_opacity=0.1, max_opactiy=0.4, gradient=gradient, control=True, scale_radius=True, radius=40, blur=25, overlay=True, max_zoom=13).add_to(m)

    # set the iframe width and height
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template("index.html", iframe=iframe)


