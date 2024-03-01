import convertJSON as cj
import heapq as heap
import time
import math 
def aStar(source, destination):


    open_list = []
    g_values = {}
    
    path = {}
    closed_list = {}
    
    sourceID = cj.getOSMId(source[0], source[1])
    destID = cj.getOSMId(destination[0], destination[1])
    
    
    g_values[sourceID] = 0
    h_source = cj.calculateHeuristic(source, destination)
    
    open_list.append((h_source,sourceID))
    s = time.time()
    while(len(open_list)>0):
        curr_state = open_list[0][1]
        #print(curr_state)
        heap.heappop(open_list)
        closed_list[curr_state] = ""
        if(curr_state==destID):
            print("Đã đạt được mục tiêu")
            break 
        nbrs = cj.getNeighbours(curr_state, destination)
        values = nbrs[curr_state]
        for eachNeighbour in values:
            neighbourId, neighbourHeuristic, neighbourCost, neighbourLatLon = cj.getNeighbourInfo(eachNeighbour)
            current_inherited_cost = g_values[curr_state] + neighbourCost
            if(neighbourId in closed_list):
               
                continue
            else:
                g_values[neighbourId] = current_inherited_cost
                neighbourFvalue = neighbourHeuristic + current_inherited_cost
                
                open_list.append((neighbourFvalue, neighbourId))
            
            path[str(neighbourLatLon)] = {"parent":str(cj.getLatLon(curr_state)), "cost":neighbourCost}
        #print('path',path,'neighbourLatLon',neighbourLatLon,'curr_state',curr_state,'neighbourCost',neighbourCost)
            
        open_list = list(set(open_list))
        heap.heapify(open_list)
    
    print("Thời gian cần thiết để tìm đường đi (tính bằng giây): "+str(time.time()-s))

    
    print("source",source)
    print("destination",destination)
    #khoảng cách giữa các cặp kinh độ vĩ độ 
    lat1, lon1 = source
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    # a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
    * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    

    print("khoảng cách từ",source,"đến",destination,"là(km):",radius * c)
    
    return path


