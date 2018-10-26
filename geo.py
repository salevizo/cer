import matplotlib.pyplot as plt
import psycopg2
import numpy as np
import pandas as pd
import geopandas

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


db=('doi105281zenodo1167595')



query="SELECT geom,ST_X(ST_Centroid(geom)), ST_Y(ST_Centroid(geom)) FROM natura2000.spatialfeatures LIMIT 500;"
#SELECT ST_SRID(geom) FROM natura2000.spatialfeatures LIMIT 2;
#3035
#WHERE mmsi=228231800;
#ST_AsText(geom) as geom 


con = psycopg2.connect(database = "doi105281zenodo1167595", user = "postgres", password = "2", host = "127.0.0.1", port = "5432")

with con:
    #geo_data= pd.read_sql_query(query, con)
    df = geopandas.GeoDataFrame.from_postgis(query, con)

print df

print type(df['geom'])
ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')

plt.show()





fig,ax=plt.subplots(figsize=(15,15))

m = Basemap(rsphere=(4620253.3123,6356752.3142),resolution='l',projection='cyl')


m.drawcoastlines()
m.fillcontinents (color='lightgray', lake_color='lightblue')
#m.drawparallels(np.arange(-90.,91.,30.))
#m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='aqua')
m.drawcounties()
ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')

plt.show()
#df.plot()





con.close()

