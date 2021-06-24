# Book_my_ticket

Book My ticket is an application which allows users to take a plane to reach destination from source via shortest path and plot the route map.

Algorithm used:
This application is a Design and Analysis of Algorithms (DAA) mini project which uses Dijkstra's Single source shortest path algorithm( Greedy approach )

Objectives:
1. Determining shortest path
2. Computing total distance travelled and travel fare
3. Plotting the route map from source to destination using imported modules

Modules imported:
1. geopy - used in calculation of distance in km using latitude and longitude
2. gmplot - used to plot route

Input provided:
1. User needs to provide the number of locations
2. Names of locations
3. Adjacency matrix which indicates whether there is a direct plane between 2 places or not. If there is direct plane the element is 1 else it is 0.
