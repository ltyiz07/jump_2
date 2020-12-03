import folium

home = 37.20725869675730, 127.097478957376880
m = folium.Map(location = home, zoom_start = 18, tiles="OpenStreetMap")
tooltip = "Click here!"
folium.Marker(location=home, popup='<i>up</i>', tooltip=tooltip).add_to(m)
folium.Marker(location=[37.2070, 127.0960], popup='<i>up</i>', tooltip=tooltip, icon=folium.Icon(icon="cog", color = "darkblue")).add_to(m)
folium.Marker(location=[37.2070, 127.0975], popup='<i>up</i>', tooltip=tooltip, icon=folium.Icon(icon="star", color = "green")).add_to(m)


