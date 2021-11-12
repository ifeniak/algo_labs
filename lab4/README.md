# algo_labs
####my algo labs on IoT program


##Search in a weighted column

Your task will be to implement the Bellman-Ford algorithm and construct a tree of the shortest paths from a given vertex s for an oriented, weighted graph. The solution is the average path length from a given vertex to all other vertices that can be reached with s.


Incoming data:
    The first line contains the numbers N - the number of edges and s - the initial vertex. The next N lines contain pairs of vertices connected by an edge and the weight of that edge.
 
Output data:
    Average path length

Limitation:
    0 <N <= 10000
Examples:
In:

8 5
0 3 8
1 4 9
4 2 4
5 0 9
5 4 6
5 1 7
1 2 1
3 1 0

Out:
    9.4
    (Path lengths - 0: 9, 4: 6, 1: 7, 2: 8, 3: 17, (9 + 6 + 7 + 8 + 17) / 5 == 9.4)
)