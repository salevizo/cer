import matplotlib.pyplot as plt
import psycopg2
import numpy as np
import pandas as pd
import geopandas
from numpy import asarray
from pyproj import Proj, transform
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import re
from matplotlib.collections import PatchCollection
import utm
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

db=('doi105281zenodo1167595')
query="SELECT  st_x(st_centroid(geom)) as st_x ,st_y(st_centroid(geom)) as st_y, geom  FROM natura2000.spatialfeatures LIMIT 10;"
#geometry(MultiPolygon,3035) 
#EPSG:3035 to EPSG:4326 (lat/long) python
query2="SELECT lat, lon FROM nari_dynamic WHERE mmsi=228231800 LIMIT 1;"


con = psycopg2.connect(database = "doi105281zenodo1167595", user = "postgres", password = "2", host = "127.0.0.1", port = "5432")
with con:
    df_natura = geopandas.GeoDataFrame.from_postgis(query, con)
   
    df_mmsi= pd.read_sql_query(query2, con)
   
print df_natura;

df_natura['geom']=df_natura['geom'].to_crs(epsg=4326)



print type(df_natura['geom'])
point = Point(df_natura['st_x'][0], df_natura['st_y'][0])
#point2 = Point(df_mmsi['lon'], df_mmsi['lat'])
print(df_natura['geom'].contains(point))



#m.plot(x,y, marker ='o', markersize=6, markerfacecolor='red', linewidth=0)


df_natura['geom'].plot();
plt.show()

###################








