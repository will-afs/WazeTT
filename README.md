🗺️ WazeTT
=========
*Research project for calculating off-trail isochrones*

<img src="https://github.com/will-afs/WazeTT/blob/main/doc/img/isochrones_for_gif/gif_isochrone_center.gif" width = 300>

Exemples of use cases :
- ⛑️ Helping rescuers estimating the possible positions of an injured person in the nature
- 👮 Helping police locating fugitives
- 🔥 Helping firefighters estimating the propagation of the fire in a forest
- 🌊 Helping engineers sizing hydraulic structures by estimating flood propagation
- ⛰️ Helping hikers finding their way in the mountain
- 💣 Helping the army finding its way in their intervention missions given dynamic events (e.g. collapse of a bridge, presence of terrorists, etc.)
- ... and many more !

*Note : this solution is made to be executable locally, i.e. without any internet connection*

# ⛰️ Input data
The solution is compatible with cartographic datasets obtained from [GeoServices Open API](https://geoservices.ign.fr/catalogue):
- Altitude datasets can be found as .asc files (raster):
  - [BD alti (25m resolution)](https://geoservices.ign.fr/bdalti)
  - [RGE alti (1m or 5m resolution)](https://geoservices.ign.fr/rgealti)
- Field datasets can be found as .shp files (vectorial):
  - [BD Topo (metric precision)](https://geoservices.ign.fr/bdtopo)
  - [BD Carto (decametric precision)](https://geoservices.ign.fr/bdcarto)

# 🔽 Installation (Linux)
Open a terminal, download the repository :

    git clone https://github.com/will-afs/WazeTT
    
Go into the directory :

    cd WazeTT/

Create a Python virtual environment :

    python3 -m venv .venv
    
Activate the virtual environment :

    source .venv/bin/activate
    
Install the project dependencies :

    pip install -r requirements.txt
  
# ⚙️ Configuration
The project can be configured through the project_config.toml file

# ▶️ Usage
The source code is accessible through the [/src folder](https://github.com/will-afs/WazeTT/tree/main/src)

The different notebooks give a general overview of the solution

# ⚗️ Main steps of the program
1. Importing altitudes as a 2D table
<img src="https://github.com/will-afs/WazeTT/blob/main/doc/img/alti_plot_BDALTIV2_25M_FXX_0875_6550_MNT_LAMB93_IGN69.png" width=300>
2. Importing fields polygons included in altitude data bounding box
<img src="https://github.com/will-afs/WazeTT/blob/main/doc/img/field_polygons_and_study_perimeter_bb.png" width=700>
3. Making fields 2D table from fields polygons
<img src="https://github.com/will-afs/WazeTT/blob/main/doc/img/field_polygons_projection_ZONE_VEGETATION_BDALTIV2_25M_FXX_0875_6550_MNT_LAMB93_IGN69.png" width=300>
4. Calculating off-trail isochrone from altitudes and fields datasets
<img src="https://github.com/will-afs/WazeTT/blob/main/doc/img/isochrones_for_gif/gif_isochrone_center.gif" width = 300>
