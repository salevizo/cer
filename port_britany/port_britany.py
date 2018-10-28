from fiona import collection
import matplotlib.pyplot as plt
from descartes import PolygonPatch
from matplotlib.collections import PatchCollection
from itertools import imap
from matplotlib.cm import get_cmap
import matplotlib.pyplot as plt
import psycopg2
import numpy as np
import pandas as pd
import geopandas
from numpy import asarray

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import re
from matplotlib.collections import PatchCollection
import utm
from matplotlib import pyplot
from descartes import PolygonPatch
import shapefile as shp
from fiona import collection

db=('doi105281zenodo1167595')
query="SELECT  st_x(st_centroid(geom)) as st_x ,st_y(st_centroid(geom)) as st_y, geom FROM ports.ports_of_brittany;"




con = psycopg2.connect(database = "doi105281zenodo1167595", user = "postgres", password = "2", host = "127.0.0.1", port = "5432")

with con:
    df = geopandas.GeoDataFrame.from_postgis(query, con)


sf = shp.Reader("port.shp")

minlon = max(-180,df['st_x'].min()-5)
minlat = max(-90,df['st_y'].min()-5)
maxlon = min(180,df['st_x'].max()+5)
maxlat = min(90,df['st_y'].max()+5)
lat0 = (maxlat+minlat)/2
lon0 = (maxlon+minlon)/2
lat1 = (maxlat+minlat)/2-20


m = Basemap(llcrnrlon=minlon,llcrnrlat=minlat,urcrnrlon=maxlon,urcrnrlat=maxlat,rsphere=(6378137.00,6356752.3142),resolution='l',projection='cyl',lat_0=lat0,lon_0=lon0,lat_ts = lat1)
#,llcrnrlat =min_lat,llcrnrlon =min_lon,urcrnrlat =max_lat, urcrnrlon =max_lon
m.drawcoastlines()
m.fillcontinents (color='lightgray', lake_color='lightblue')

m.drawmapboundary(fill_color='aqua')

x_cor=[]
y_cor=[]


for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    x_cor.append(x)
    y_cor.append(y)

xx=[]
for element in x_cor:
    for el in element:
        xx.append(el)

yy=[]
for element in y_cor:
    for el in element:
        yy.append(el)


m.plot(xx,yy,marker ='o',markersize=10, markerfacecolor='red',linewidth=0)


plt.show()


