import geopy
from geopy.geocoders import Nominatim
from geopy import distance
import gmplot

def dijkstra(source,locations):
    global dist,adj,places
    visited=[]
    path=[]
    prev=[]
    for i in range(locations):
        visited.append(False)
        path.append(99999999)
        prev.append(source)
    path[source]=0
    for i in range(locations):
        visited[i]=True
        for j in range(locations):
            if adj[i][j] and (visited[j]==False) and path[j]>path[i]+ dist[i][j]:
                prev[j]=i
                path[j]=path[i] +dist[i][j]

    route=[locations-1]
    j=locations-1
    while j != source:
        j = prev[j]
        route.append(j)
    route=route[::-1]
    cost = path[locations-1] * 5
    print(f"\nThe fare of the journey is {cost} for travelling a distance of {path[locations-1]} km")
    return route


geolocator=Nominatim(user_agent="geoapiExercises")
print("\t\t\t----------------------------------\n")
print("\t\t\t\t\t\tBook My Ticket\t\t\t\t\n")
print("\t\t\t----------------------------------\n\n")

locations=int(input("Enter number of locations : "))
places=[]
for i in range(locations):
    places.append(input("Enter place : "))

print("Enter adjacency matrix where 1 represents direct flight between two places and 0 represents no direct flight")

adj=[]
for i in range(locations):
    l=list( map(int,input().split()))
    adj.append(l)

dist=[]
for i in range(locations):
    l=[]
    place1 = geolocator.geocode(places[i])
    location1= (place1.latitude,place1.longitude)
    for j in range(locations):
        if adj[i][j] == 1:
            place2 = geolocator.geocode(places[j])
            location2=(place2.latitude,place2.longitude)
            d = distance.distance(location1,location2).km
            l.append(d)
        else:
            l.append(99999999)
    dist.append(l)

route = dijkstra(0,locations)
print("\nThe shortest path is\n")
for i in range(len(route) - 1):
    print(places[i] + "==>", end="")
print(places[locations - 1])

gmapOne= gmplot.GoogleMapPlotter(22.3511148,78.6677428,14)
latitude_list = []
longitude_list = []
for index in route:
    place=geolocator.geocode(places[index])
    latitude_list.append(place.latitude)
    longitude_list.append(place.longitude)

gmapOne.scatter(latitude_list, longitude_list, '#ff0000', size=40, marker=False)
gmapOne.plot(latitude_list, longitude_list,'cornflowerblue', edge_width=2.5)
gmapOne.draw("map.html")


