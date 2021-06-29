
import sys

class Field:
    def __init__(self,dataset):
        stops,links,tickets = dataset
        self.stops = stops
        # Build List of stops
        self.stop_list=[]
        print("Loading dataset. {stops} stops, {links} links, and {tickets} tickets."
            .format(
                stops=len(stops),
                links = len(links),
                tickets = len(tickets)
                ))
        for s in stops:
            st = Stop(s,self.stops[s])
            #print("Adding stop {stop}".format(stop=st))
            self.stop_list.append(st)

        # Build List of Links
        self.link_list=[]
        for l in links:
            stid,cars,engs,color,mountain = l
            st = (self.getStopbySTID(stid[0]),self.getStopbySTID(stid[1]))
            self.link_list.append(Link((st,cars,engs,color,mountain)))

        # Populate Stops with Links
        for l in self.link_list:
            for st in l.stops:
                #print("Adding {link} to {stop}".format(link=l,stop=st))
                st.addLink(l)
        num_stat = len(self.stop_list)
        self.graph = [[0 for column in range(num_stat)] for row in range(num_stat)] 

    def getStopbySTID(self,stid):
        for s in self.stop_list:
            if s.stid==stid:
                return s

    def getStopbyNumber(self,num):
        return self.stop_list[num]

    def getStopbyName(self,name):
        for s in self.stop_list:
            if s.name == name:
                return s

    # Take 2 stops
    # return array of links
    def getShortPath(self,source,dest):
        v_stops = []
        u_stops = self.stop_list[:] # copy the array, not the objects

        #build hashmap of all verticies
        verts = {}
        for s in u_stops:
            if source==s:
                #print("SRC")
                verts[s.getSTID()]=[0,None]
            else:
                # 
                verts[s.getSTID()]=[10000,None]
        
        

        # loop until all verticies have been visited
        while len(u_stops) !=0:
            # fint verts with smallest known distance from start.
            small_vrt_dst = 10000
            small_vrt = None
            for v in verts:
                cv = self.getStopbySTID(v)
                if cv in u_stops:
                    dist,prev=verts[cv.getSTID()]
                    #print("{cv}, {d}".format(cv=cv,d=dist))
                    if dist<small_vrt_dst:
                        #print("New station with smallest distace from start {v}".format(v=cv))
                        small_vrt_dst=dist
                        small_vrt=cv
            #print("Unvisited  Vertex with shortest distance is {vert} with distance {dist}".format(vert=small_vrt,dist=small_vrt_dst))
            
            neighbors = small_vrt.getLinkedStopswithLink()
            #print("It has {n} neighbors".format(n=len(neighbors)))

            #Iterate through neighbors
            for n in neighbors:
                vert,link=n
                #Only check unvisited verts
                if vert in u_stops:
                    lcost = link.calculateLinkCost()
                    lcost += small_vrt_dst
                    #print(" {vert} is {cost} from start".format(vert=vert,cost=lcost))
                    if verts[vert.getSTID()][0]>lcost:
                        #print("Cost of {cost} is lower then {table}".format(cost=lcost,table=verts[vert.getSTID()][0]))
                        verts[vert.getSTID()][0]=lcost
                        verts[vert.getSTID()][1]=small_vrt
            #print("Removing {vrt} from unvisited stations.".format(vrt=small_vrt))
            u_stops.remove(small_vrt)
            v_stops.append(small_vrt)
            #print("{viz} stationes visited, {uviz} stations left".format(viz=len(v_stops),uviz=len(u_stops)))
        # We return the cost and breadcrumbs.
        breadcrumbs=[]
        crumbs_curr = dest
        cars_cost = verts[dest.getSTID()][0]
        while crumbs_curr != source:
            cost,via = verts[crumbs_curr.getSTID()]
            for n in crumbs_curr.getLinkedStopswithLink():
                stop,link = n
                if stop==via:
                    breadcrumbs.append(link)
                    crumbs_curr=stop
                    break
                
        return (cars_cost,breadcrumbs)

    def __repr__(self):
        return "<Field with {stops} stops and {links} links>".format(stops=len(self.stop_list), links=len(self.link_list))

class Stop:
    def __init__(self,stid,name):
        self.links=[]
        self.stid = stid
        self.name = name
        pass
    def getLinkedStops(self):
        stations = []
        for l in self.links:
            for s in l.stops:
                if s.getSTID()!=self.getSTID():
                    stations.append(s)
        return stations

    def getLinkedStopswithLink(self):
        station_links = []
        for l in self.links:
            for s in l.stops:
                if s.getSTID()!=self.getSTID():
                    station_links.append((s,l))
        return station_links
    
    def addLink(self,l):
        #print("Adding {link} to {station}".format(link=l,station=self))
        if l in self.links:
            pass
            #print("Link Exists")
        else:
            self.links.append(l)

    def getName(self):
        return self.name

    def getSTID(self):
        return self.stid

    def getLinks(self):
        return self.links

    def __repr__(self):
        return "<Stop '{self.name}' with {links} links>".format(self=self, links=len(self.links))

class Link:
    def __init__(self,l):
        stops,cars,engines,color,mountain = l
        self.stops = stops
        self.cars = cars
        self.engines = engines
        self.color = color
        self.mountain = mountain
        
    def getStops(self):
        return self.stops

    def getCars(self):
        return self.cars

    def getEngines(self):
        return self.engines

    def getColor(self):
        return self.color

    def getMountain(self):
        return self.mountain

    def calculateLinkCost(self):
        cost = self.getCars()
        if self.getMountain():
            cost +=2
        return cost
    
    def __repr__(self):
        engines=""
        if self.engines>0:
            engines=" with {engines} engines".format(engines=self.engines)
        
        mountains=""
        if self.mountain:
            mountains=" Through Mountains"
        return "<{color} Route from {start} to {end} {cars} cars long{engines}{mountains}>".format(
            engines=engines,
            mountains=mountains,
            color=self.color.capitalize(),
            cars=self.cars,
            start=self.stops[0].getName(),
            end=self.stops[1].getName())


#f = Field(stops,links)

#c_gen = []
#for t in tickets:
#    c_gen.append(t[0])
#    c_gen.append(t[1])

#c_gen = list(dict.fromkeys(c_gen))

#for c in c_gen:
#    print(stops[c])