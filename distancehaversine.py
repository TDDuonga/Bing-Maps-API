import convertJSON as cj
import heapq as heap
import math


def distancehaversine(source, destination):
   #khoảng cách giữa các cặp kinh độ vĩ độ 
    lat1, lon1 = source
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)

    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
    * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    print("khoảng cách từ",source,"đến",destination,"là(km):",d)
    return d

    