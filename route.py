from ticketmap.ticketmap import Field
from ticketmap.europedata import dataset as europedata

f = Field(europedata)
a = f.getStopbyName("Edinburgh")
b = f.getStopbyName("Erzurum")

cost,links=f.getShortPath(a,b)

print("Cost is {cost} cars".format(cost=cost))
for l in links:
    print(l)
