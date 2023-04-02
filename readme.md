# The Safe Way

Harvey, Jem and Josh's 2023 Bath Hack project, lovingly created in 24 hours ☕️

> It is unacceptable that people in Bath feel threatened and unsafe when walking home late at night. Our application combines cutting-edge ML crime prediction to help users find a safer route home.

### What it does

We have leveraged cutting-edge ML to predict crime patterns within Bath to help users navigate home finding the saftest routes. It is a website that provides the user with a heat map which-represents crime hotspots within the area. The application will also calculate a safe route home the user can go when prompted.

### How we built it

Dataset:

- data.police.uk: (provided us with details about all the crimes in Bath and Bristol in addition to their location)

### Screenshot

<img src="screen.png" alt="drawing" width="200"/>

### Installation

1. `git clone` this repo
2. `pip install` 
    - folium
    - numpy
    - pandas
    - matplotlib
    - flask
3. Run `app.py`

### References

[data.police.uk](https://data.police.uk/)

[wiki.openstreetmap.org](https://wiki.openstreetmap.org/wiki/Routing)

[openrouteservice.org](https://openrouteservice.org/)