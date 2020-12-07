import numpy as np
import pandas as pd
import xarray as xr
import datetime
input_file='E:/TFM_TIG/Scripts/PruebaSPs.csv'
csv = pd.read_csv(input_file,sep = ";", decimal = ",",header=0)
#csv.set_index('FechaInici',inplace=True)  # Para que los índices sean fechas y así se ponen en el eje x de forma predeterminada
Fechas  = pd.to_datetime(csv.FechaInici)
ID = csv.OBJECTID
Year = np.zeros(len(csv),int)
Month = np.zeros(len(csv),int)
Day = np.zeros(len(csv),int)
Hour = csv.Hora
lat = np.zeros(len(csv),float)
lon = np.zeros(len(csv),float)
fecha_format = np.zeros(len(csv),str)
MUCAPE = np.zeros(len(csv),float)
tiempo=np.zeros(len(csv),str)
for i in range(len(csv)):
    Year[i] = Fechas[i].year
    Month[i] = Fechas[i].month
    Day[i] = Fechas[i].day
    if Hour[i]==00:
        tiempo = datetime.datetime(Year[i], Month[i], Day[i]-1, 23, 00)
    else:
        tiempo = datetime.datetime(Year[i], Month[i], Day[i], Hour[i]-1, 00)

    lon[i] = csv.LON[i]
    lat[i] = csv.LAT[i]
    MUCAPE[i]=data.sel(lat=lat[i], lon=lon[i], time=tiempo,method='nearest').values

csv['MUCAPE']=MUCAPE
csv.to_csv("nombre.csv", sep=";", decimal=",",index=False)