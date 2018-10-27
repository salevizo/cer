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

db=('doi105281zenodo1167595')



query="SELECT geom,ST_X(ST_Centroid(geom)), ST_Y(ST_Centroid(geom)) FROM natura2000.spatialfeatures LIMIT 10;"
#query="SELECT geom FROM natura2000.spatialfeatures LIMIT 5;"
#SELECT ST_SRID(geom) FROM natura2000.spatialfeatures LIMIT 2;
#3035
#WHERE mmsi=228231800;
#ST_AsText(geom) as geom 


con = psycopg2.connect(database = "doi105281zenodo1167595", user = "postgres", password = "2", host = "127.0.0.1", port = "5432")

with con:
    #geo_data= pd.read_sql_query(query, con)
    df = geopandas.GeoDataFrame.from_postgis(query, con)

print df

###################
print type(df['geom'])
#ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
#plt.show()
############



#################################3
fig,ax=plt.subplots(figsize=(15,15))
m = Basemap(rsphere=(4620253.3123,6356752.3142),resolution='l',projection='cyl')
#m(np.array(ais_data['lon']),np.array(ais_data['lat']))
m.drawcoastlines()
m.fillcontinents (color='lightgray', lake_color='lightblue')
m.drawmapboundary(fill_color='aqua')
m.drawcounties()
ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
plt.show()

####################################3





##################
#patches=[]
#for polygon in df['geom']:
#       
#        pat = re.compile(r'''(-*\d+\.\d+ -*\d+\.\d+);*''')
#        s = str(polygon)
#        matches = pat.findall(s)
#        if matches:
#            lst = [tuple(map(float, m.split())) for m in matches]
#          
#        a = asarray(lst)
#        print a
#        print a[:,0]
#        #x,y = map(a[:,0], a[:,1])
#        a = zip(a[:,0],a[:,1])
#        p = Polygon(a,fc='r',ec='k',zorder=2, lw=.1)
#        patches.append(p)
#
#print patches
#fig = plt.figure(num=None, figsize=(11.3,7.00))
#ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
#map = Basemap(rsphere=(4620253.3123,6356752.3142),resolution='l',projection='cyl')
#map.fillcontinents(color='0.7',zorder=0)
#ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
#ax.add_collection(PatchCollection(patches,match_original=True))
#plt.show()
################################3


con.close()

