// Weighted Graph ADT interface ... COMP9024 20T2

typedef struct GraphRep *Graph;

#define MAX_STOP_NAME 31
// vertices are ints
#define VERY_HIGH_VALUE 999999
#define MAX_NODES 1000
typedef struct Vertex
{

	char from[MAX_STOP_NAME];
	int cost_to_get_here;
	char prev[MAX_STOP_NAME];

} Vertex;
typedef struct Edge
{

	int from;
	int to;
	// if arrival_bus_time > start_time
	// skip
	int start_time;
	int arrival_time;

	//weight = arrival_dest_time -arrival_bus_stop_time ;

} Edge;

typedef struct GraphRep
{
	int **edges; // adjacency matrix if two vertex connected
				 // 0 if nodes not adjacent
	int nfrom;	 // #fromertices
	int nE;		 // #edges

	char bus_stop_name[100][MAX_STOP_NAME];

	Edge *all_edges[100];
} GraphRep;

// edges are pairs of vertices (end-points) with a weight

Graph newGraph(int);
// int numOfVertices(Graph);
void insertEdge(Graph g, Edge *e);
// void removeEdge(Graph, Edge);
// int adjacent(Graph, Vertex, Vertex); // returns weight, or 0 if not adjacent
void showGraph(Graph);
void freeGraph(Graph);

int find_index_bus_stop(char arr[][MAX_STOP_NAME], int len, char targe[]);
