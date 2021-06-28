from .europedata import links, stops, tickets

def codeToCityName(abvr):
    return stops[abvr]

class Field:
    def __init__(self,stops,links):
        # Build List of stops
        self.stop_list=[]
        for s in stops:
            self.stop_list.append(Stop(s))

        # Build List of Links
        self.link_list=[]
        for l in links:
            stid,cars,engs,color,mountain = l
            st = (self.getStopbySTID(stid[0]),self.getStopbySTID(stid[1]))
            self.link_list.append(Link((st,cars,engs,color,mountain)))

        # Populate Stops with Links
        for l in self.link_list:
            for st in l.stops:
                print("Adding {link} to {stop}".format(link=l,stop=st))
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

    def __repr__(self):
        return "<Field with {stops} stops and {links} links>".format(stops=len(self.stop_list), links=len(self.link_list))

class Stop:
    def __init__(self,stid):
        self.links=[]
        self.stid = stid
        self.name = codeToCityName(stid)
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
        print("Adding {link} to {station}".format(link=l,station=self))
        if l in self.links:
            print("Link Exists")
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
#         stops          len eng  color      tunnel
#Link( ("",""),  1, 0,  "",    False),


#f = Field(stops,links)

#c_gen = []
#for t in tickets:
#    c_gen.append(t[0])
#    c_gen.append(t[1])

#c_gen = list(dict.fromkeys(c_gen))

#for c in c_gen:
#    print(stops[c])