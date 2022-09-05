from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

def avgGui(lat, lon):
    now = datetime.now() 
    current = now.year 

    start = datetime(2010, 1, 1)
    end = datetime(current-1, 12, 31)

    city = Point(lat, lon)

    data = Daily(city, start, end)
    data = data.fetch()

    data.plot(y=['tavg'])
    data.plot(y=['prcp'])
    plt.show()

def avg(lat, lon):
    now = datetime.now() 
    current = now.year 

    start = datetime(2010, 1, 1)
    end = datetime(current-1, 12, 31)

    city = Point(lat, lon)

    data = Daily(city, start, end)
    data = data.fetch()

    avgs = data.mean(axis=0)

    return(avgs)