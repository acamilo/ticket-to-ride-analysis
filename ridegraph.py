from collections import OrderedDict

tickets = [
("amst","pamp"),("brux","danz"),("kyiv","petr"),("madr","diep"),("pari","madr"),("sofi","kyiv"),
("amst","rost"),("brux","stoc"),("kyiv","soch"),("madr","roma"),("pari","mosk"),("sofi","smyr"),
("amst","vene"),("bucu","erzu"),("lisb","cadi"),("madr","wien"),("pari","roma"),("stoc","wiln"),
("amst","wiln"),("buda","sofi"),("lisb","danz"),("madr","zuri"),("pari","seva"),("vene","cons"),
("athi","anco"),("cadi","fran"),("lond","anco"),("mars","esse"),("pari","wien"),("vene","wars"),
("athi","wiln"),("cadi","stoc"),("lond","athi"),("mosk","anco"),("pari","zagr"),("wars","buda"),
("barc","brux"),("danz","buda"),("lond","berl"),("mosk","athi"),("rica","brin"),("wars","seva"),
("barc","munc"),("diep","kobe"),("lond","madr"),("munc","petr"),("riga","bucu"),("wars","smol"),
("berl","anco"),("diep","mars"),("lond","mosk"),("munc","sara"),("riga","khar"),("wien","anco"),
("berl","athi"),("edin","athi"),("lond","pari"),("pale","cons"),("roma","anco"),("wien","athi"),
("berl","bucu"),("edin","esse"),("lond","roma"),("pale","mosk"),("roma","athi"),("wien","mosk"),
("berl","mosk"),("esse","anco"),("lond","soch"),("pamp","kyiv"),("roma","mosk"),("wien","roma"),
("berl","roma"),("esse","kyiv"),("lond","wien"),("pamp","pale"),("roma","smyr"),("wien","stoc"),
("berl","wien"),("fran","kobe"),("madr","berl"),("pari","anco"),("rost","erzu"),("zagr","brin"),
("bres","mars"),("fran","smol"),("madr","mosk"),("pari","athi"),("sara","seva"),("zuri","brin"),
("bres","petr"),("kobe","erzu"),("madr","anco"),("pari","berl"),("smol","rost"),("zuri","buda"),
("bres","vene"),("kyiv","pete"),("madr","athi"),("pari","edin"),("soch","smyr")
]

stops = {
    "amst" : "Amsterdam", 
    "brux" : "Bruxelles", 
    "kyiv" : "Kyiv", 
    "madr" : "Madrid", 
    "pari" : "Paris", 
    "sofi" : "Sofia", 
    "bucu" : "Bucuresti", 
    "lisb" : "Lisboa", 
    "stoc" : "Stockholm", 
    "buda" : "Budapest", 
    "vene" : "Venezia", 
    "athi" : "Athina", 
    "cadi" : "Cadiz", 
    "lond" : "London", 
    "mars" : "Marseille", 
    "mosk" : "Moskva", 
    "wars" : "Warszawa", 
    "barc" : "Barcelona", 
    "danz" : "Danzig", 
    "rica" : "Rica", 
    "diep" : "Dieppe", 
    "munc" : "Munchen", 
    "riga" : "Riga", 
    "berl" : "Berlin", 
    "wien" : "Wien", 
    "edin" : "Edinburgh", 
    "pale" : "Palermo", 
    "roma" : "Roma", 
    "esse" : "Essen", 
    "pamp" : "Pamplona", 
    "fran" : "Frankfurt",
    "rost" : "Rostov", 
    "zagr" : "Zagrab", 
    "bres" : "Brest", 
    "sara" : "Sarajevo", 
    "zuri" : "Zurich", 
    "kobe" : "Kobenhavn", 
    "smol" : "Smolensk", 
    "soch" : "Sochi",
    "petr" : "Petrograd",
    "smyr" : "Smyrna",
    "erzu" : "Erzurum",
    "wiln" : "Wilno",
    "seva" : "Sevastopol",
    "cons" : "Constantanople",
    "anco" : "Angora",
    "brin" : "Brindisi",
    "khar" : "Kharkov",
    "pete" : "Peterograd"
    }

links = [
    [("edin","lond"),  4, 0,  "black",   False],
    [("edin","lond"),  4, 0,  "orange",  False],
    [("lond","diep"),  2, 1,  "wild",    False],
    [("lond","diep"),  2, 1,  "wild",    False],
    [("lond","amst"),  2, 2,  "wild",    False],
    [("diep","bres"),  2, 0,  "orange",  False],
    [("bres","pari"),  3, 0,  "black",   False],
    [("bres","pamp"),  4, 0,  "pink",    False],
    [("diep","brux"),  2, 0,  "green",   False],
    [("diep","pari"),  1, 0,  "pink",    False],
    [("pari","pamp"),  4, 0,  "blue",    False],
    [("pari","pamp"),  4, 0,  "green",   False],
    [("pari","brux"),  2, 0,  "yellow",  False],
    [("pari","brux"),  2, 0,  "red",     False],
    [("pari","fran"),  3, 0,  "white",   False],
    [("pari","fran"),  3, 0,  "orange",  False],
    [("pari","zuri"),  3, 0,  "wild",    True ],
    [("pari","mars"),  4, 0,  "wild",    False],
    [("mars","pamp"),  4, 0,  "red",     False],
    [("mars","barc"),  4, 0,  "wild",    False],
    [("barc","pamp"),  2, 0,  "wild",    True ],
    [("barc","madr"),  2, 0,  "yellow",  False],
    [("madr","pamp"),  3, 0,  "white",   True ],
    [("madr","pamp"),  1, 0,  "black",   True ],
    [("madr","cadi"),  3, 0,  "orange",  False],
    [("cadi","lisb"),  2, 0,  "blue",    False],
    [("lisb","madr"),  3, 0,  "pink",    False],
    [("mars","zuri"),  2, 0,  "pink",    True ],
    [("mars","roma"),  4, 0,  "wild",    True ],
    [("zuri","vene"),  2, 0,  "green",   True ],
    [("zuri","munc"),  2, 0,  "yellow",  True ],
    [("munc","fran"),  2, 0,  "pink",    False],
    [("fran","brux"),  2, 0,  "blue",    False],
    [("fran","amst"),  2, 0,  "white",   False],
    [("amst","brux"),  1, 0,  "black",   False],
    [("amst","esse"),  3, 0,  "yellow",  False],
    [("esse","fran"),  2, 0,  "green",   False],
    [("fran","berl"),  3, 0,  "black",   False],
    [("fran","berl"),  3, 0,  "red",     False],
    [("berl","esse"),  2, 0,  "blue",    False],
    [("munc","vene"),  2, 0,  "blue",    True ],
    [("vene","roma"),  2, 0,  "black",   False],
    [("vene","zagr"),  2, 0,  "wild",    False],
    [("roma","pale"),  4, 1,  "wild",    False],
    [("roma","brin"),  2, 0,  "white",   False],
    [("brin","pale"),  3, 1,  "wild",    False],
    [("pale","smyr"),  6, 2,  "wild",    False],
    [("brin","athi"),  4, 1,  "wild",    False],
    [("sara","athi"),  4, 0,  "green",   False],
    [("sara","zagr"),  3, 0,  "red",     False],
    [("zagr","wien"),  2, 0,  "wild",    False],
    [("zagr","buda"),  2, 0,  "orange",  False],
    [("buda","wien"),  1, 0,  "white",   False],
    [("buda","wien"),  1, 0,  "red",     False],
    [("wien","munc"),  3, 0,  "orange",  False],
    [("wien","berl"),  3, 0,  "green",   False],
    [("berl","wars"),  4, 0,  "yellow",  False],
    [("berl","wars"),  4, 0,  "pink",    False],
    [("berl","danz"),  4, 0,  "wild",    False],
    [("esse","kobe"),  3, 1,  "wild",    False],
    [("esse","kobe"),  3, 1,  "wild",    False],
    [("kobe","stoc"),  3, 0,  "white",   False],
    [("kobe","stoc"),  3, 0,  "yellow",  False],
    [("stoc","petr"),  8, 0,  "wild",    True ],
    [("rica","danz"),  3, 0,  "black",   False],
    [("danz","wars"),  2, 0,  "wild",    False],
    [("wiln","rica"),  4, 0,  "green",   False],
    [("rica","petr"),  4, 0,  "wild",    False],
    [("petr","wiln"),  4, 0,  "blue",    False], #nice
    [("petr","mosk"),  4, 0,  "white",   False],
    [("smol","wiln"),  3, 0,  "yellow",  False],
    [("wiln","wars"),  3, 0,  "red",     False],
    [("wars","kyiv"),  4, 0,  "wild",    False],
    [("wars","wien"),  4, 0,  "blue",    False],
    [("buda","kyiv"),  6, 0,  "wild",    True ],
    [("buda","bucu"),  4, 0,  "wild",    True ],
    [("buda","sara"),  3, 0,  "pink",    False],
    [("sara","sofi"),  2, 0,  "wild",    True ],
    [("sofi","athi"),  3, 0,  "pink",    False],
    [("athi","smyr"),  2, 1,  "wild",    False],
    [("cons","sofi"),  3, 0,  "blue",    False],
    [("cons","smyr"),  2, 0,  "wild",    True ],
    [("smyr","anco"),  3, 0,  "orange",  True ],
    [("anco","cons"),  2, 0,  "wild",    True ],
    [("anco","erzu"),  3, 0,  "black",   False],
    [("erzu","seva"),  4, 2,  "wild",    False],
    [("seva","cons"),  4, 2,  "wild",    False],
    [("soch","erzu"),  3, 0,  "red",     True ],
    [("soch","seva"),  2, 1,  "wild",    False],
    [("soch","rost"),  2, 0,  "wild",    False],
    [("seva","rost"),  4, 0,  "wild",    False],
    [("rost","khar"),  2, 0,  "green",   False],
    [("seva","bucu"),  4, 0,  "white",   False],
    [("bucu","kyiv"),  4, 0,  "wild",    False],
    [("kyiv","khar"),  4, 0,  "wild",    False],
    [("kyiv","smol"),  3, 0,  "red",     False],
    [("khar","mosk"),  4, 0,  "wild",    False],
    [("mosk","smol"),  2, 0,  "orange",  False],
    [("wiln","kyiv"),  2, 0,  "wild",    False],
    [("bucu","sofi"),  2, 0,  "wild",    True ],

]

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