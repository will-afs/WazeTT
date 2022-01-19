from pyproj import Proj, transform

inProj = Proj(init='epsg:2154')
outProj = Proj(init='epsg:4326')
x1,y1 = 882408.3,6543019.6
x2,y2 = transform(inProj,outProj,x1,y1)
print(x2,y2)