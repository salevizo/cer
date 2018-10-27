import sqlite3 as lite
import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import psycopg2

db=('doi105281zenodo1167595')
query="SELECT lat, lon FROM nari_dynamic WHERE mmsi=228231800;"
#WHERE mmsi=228231800;

con = psycopg2.connect(database = "doi105281zenodo1167595", user = "postgres", password = "2", host = "127.0.0.1", port = "5432")

#con=lite.connect(db)
with con:
    ais_data= pd.read_sql_query(query, con)
con.close()


print ais_data.tail(5)


minlon = max(-180,min(ais_data['lon'])-5)
minlat = max(-90,min(ais_data['lat'])-5)
maxlon = min(180,max(ais_data['lon'])+5)
maxlat = min(90,max(ais_data['lat'])+5)
lat0 = (maxlat+minlat)/2
lon0 = (maxlon+minlon)/2
lat1 = (maxlat+minlat)/2-20


fig,ax=plt.subplots(figsize=(15,15))

m = Basemap(llcrnrlon=minlon,llcrnrlat=minlat,urcrnrlon=maxlon,urcrnrlat=maxlat,rsphere=(6378137.00,6356752.3142),resolution='l',projection='cyl',lat_0=lat0,lon_0=lon0,lat_ts = lat1)


m.drawcoastlines()
m.fillcontinents (color='lightgray', lake_color='lightblue')
#m.drawparallels(np.arange(-90.,91.,30.))
#m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='aqua')

#m.drawcounties()

x, y = m(np.array(ais_data['lon']),np.array(ais_data['lat']))
m.plot(x,y, marker ='o', markersize=6, markerfacecolor='red', linewidth=0)

plt.title('Mercator Projection')
plt.show()

