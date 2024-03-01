import xmltodict
from haversine import haversine
import time
import numpy as np
from sklearn.neighbors import KDTree

s = time.time()
doc = {}
with open('data/map.graphml','r', encoding='utf-8') as fd:
    doc = xmltodict.parse(fd.read())
print(doc)


def getLatLon(OSMId):
    lat, lon = 0, 0
    nodes = doc['graphml']['graph']['node']
    for eachNode in range(len(nodes)):
        if(nodes[eachNode]["@id"] == str(OSMId)):
            lat = float(nodes[eachNode]["data"][0]["#text"])
            lon = float(nodes[eachNode]["data"][1]["#text"])
            print("lat",lat,"lon",lon)
    return (lat, lon)


def getOSMId(lat, lon):
    OSMId = 0
    nodes = doc['graphml']['graph']['node']
    for eachNode in range(len(nodes)):
        if(nodes[eachNode]["data"][0]["#text"]==str(lat)):
            if(nodes[eachNode]["data"][1]["#text"]==str(lon)):
                OSMId = nodes[eachNode]["data"][2]["#text"]
            # print("osmid",OSMId)
    return OSMId


def calculateHeuristic(curr, destination):
    return haversine(curr, destination)


def getNeighbours(OSMId, destinationLetLon):
    neighbourDict = {}
    tempList = []
    edges = doc['graphml']['graph']['edge']
    
    for eachEdge in range(len(edges)):
        if edges[eachEdge]["@source"] == str(OSMId) or edges[eachEdge]["@target"] == str(OSMId):
            temp_nbr = {}
            
            neighbourCost = 0
            neighbourId = edges[eachEdge]["@source"] if edges[eachEdge]["@target"] == str(OSMId) else edges[eachEdge]["@target"]
            neighbourLatLon = getLatLon(neighbourId) 
            
            dataPoints = edges[eachEdge]["data"]
            for eachData in range(len(dataPoints)):
                if dataPoints[eachData]["@key"] == "d14":
                    neighbourCost = dataPoints[eachData]["#text"]
            
            neighborHeuristic = calculateHeuristic(neighbourLatLon, destinationLetLon)
            
            temp_nbr[neighbourId] = [neighbourLatLon, neighbourCost, neighborHeuristic]
            tempList.append(temp_nbr)
            
    neighbourDict[OSMId] = tempList
    
    return neighbourDict



def getNeighbourInfo(neighbourDict):
    neighbourId = 0
    neighbourHeuristic = 0
    neighbourCost = 0
    for key, value in neighbourDict.items():
        
        neighbourId = key
        neighbourHeuristic = float(value[2])
        neighbourCost = float(value[1])/1000
        neighbourLatLon = value[0]
    return neighbourId, neighbourHeuristic, neighbourCost, neighbourLatLon

#Argument should be tuple

def getKNN(pointLocation):
    nodes = doc["graphml"]["graph"]["node"]
    locations = []
    for eachNode in range(len(nodes)):
        locations.append((nodes[eachNode]["data"][0]["#text"],nodes[eachNode]["data"][1]["#text"]))

    locations_arr = np.asarray(locations, dtype=np.float32)
    point = np.asarray(pointLocation, dtype=np.float32)

    tree = KDTree(locations_arr, leaf_size=2)
    dist, ind = tree.query(point.reshape(1,-1), k=3) 
    
    nearestNeighbourLoc = (float(locations[ind[0][0]][0]), float(locations[ind[0][0]][1]))
    return nearestNeighbourLoc
    
def getResponsePathDict(paths, source, destination):
    finalPath = []
    child = destination
    parent = ()
    cost = 0
    while(parent!=source):
        tempDict = {}
        cost = cost + float(paths[str(child)]["cost"])
        parent = paths[str(child)]["parent"]
        parent = tuple(float(x) for x in parent.strip('()').split(','))
        tempDict["lat"] = parent[0]
        tempDict["lng"] = parent[1]
        
        finalPath.append(tempDict)
        child = parent
   
    return finalPath, cost

