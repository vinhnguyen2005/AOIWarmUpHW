import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import folium

df = pd.read_csv('Day41/world_countries_population_2020.csv', sep=';')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

df['Population'] = df['Population'].str.replace(',', '') 
df['Land Area (km2)'] = df['Land Area (km2)'].str.replace(',', '') 
convert_dict = {
    'Population': int,
    'Land Area (km2)': float
}
df = df.astype(convert_dict)

india_lat = 20.5937
india_lon = 78.9629
india_map = folium.Map(location=[india_lat, india_lon], zoom_start=4, tiles='cartodbpositron')

map_population = folium.Map(location=[india_lat, india_lon], zoom_start=4, tiles='cartodbpositron')
state_geo = 'Day41/world-countries.json'
choropleth = folium.Choropleth(
    geo_data=state_geo,
    data=df,
    columns=['Country',	'Population'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Bản đồ thể hiện dân số quốc gia'
).add_to(map_population)

choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['name'], labels=False)
)

map_population.save('Day41/population_map.html')