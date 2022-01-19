import folium
import webbrowser

coords = [47.05713580833242, -0.88353970175474]         # Centre de la carte
zoom_start = 17                                         # valeur de la variable élevée  <=> zoom élevé
center = coords
#message = popup='length: {} <br> area: {}'.format(r['Shape_Leng'], r['Shape_Area'])

my_map = folium.Map(location = center, zoom_start = zoom_start)
folium.Marker([47.05713580833242, -0.88353970175474],
              popup='Maison de Bertrand').add_to(my_map)


isochrone = [(47.05780395359865, -0.8828685644120506),
            (47.05549457485691, -0.8852907347578964),
            (47.0546123287138, -0.8829414587471869),
            (47.057045717116885, -0.8817169374159551),
            (47.05779254249591, -0.8828728515883316)]
folium.PolyLine(isochrone, color='blue', weight=2.5, opacity=0.8).add_to(my_map)

my_map.save("map.html")
webbrowser.open("map.html")

map = Map(center = coords, zoom_start = 13)
map.showMap()
