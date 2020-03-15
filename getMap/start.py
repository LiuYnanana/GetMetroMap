import os
from get_map import Map
from get_subway_station import Subway
from get_river import River

def start(place, x, y, z):
     beijingMap = Map(place, x, y, z, "E:/MiniMetro/Picture/{name}/Map".format(name = place))   
     beijingMap.get_map()

     beijingSubway = Subway("E:/MiniMetro/Picture/{name}/Map".format(name = place), 
           "E:/MiniMetro/Picture/{name}/Grayscale".format(name = place), 
           "E:/MiniMetro/Picture/{name}/Circle".format(name = place))
     beijingSubway.get_subway_station()

     beijingRiver = River(place, "E:/MiniMetro/Picture/{name}/Map/{name}.png".format(name = place), 
                          "E:/MiniMetro/Picture/{name}/River".format(name = place))
     beijingRiver.get_river()

def main():
    place = "Beijing"
    x = [3162, 3163, 3164, 3165]
    y = [1177, 1178, 1179]
    z = 14
    start(place, x, y, z)


if __name__ == "__main__":
    main()
