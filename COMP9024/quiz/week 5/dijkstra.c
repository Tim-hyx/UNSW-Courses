// Starting code for Dijkstra's algorithm ... COMP9024 20T2

#include "PQueue.h"
#include <stdbool.h>
#include <stdio.h>

#define VERY_HIGH_VALUE 999999

typedef struct GraphRep
{
    int **edges; // adjacency matrix storing positive weights
        // 0 if nodes not adjacent
    int nV; // #vertices
    int nE; // #edges
} GraphRep;

void print_path(Vertex v, int pred[]) //an example: 0->1->2
{
    if (pred[v] == -1)
    {
        printf("%d", v); //first print the last node 0
        return;
    }
    else
    {
        print_path(pred[v], pred);
    }
    printf("-%d", v); //print 1 print 2
}

void dijkstraSSSP(Graph g, Vertex source)
{
    int dist[MAX_NODES];
    int pred[MAX_NODES];
    bool vSet[MAX_NODES]; // vSet[v] = true <=> v has not been processed
    int s;

    PQueueInit();
    int nV = numOfVertices(g);
    for (s = 0; s < nV; s++)
    {
        joinPQueue(s);
        dist[s] = VERY_HIGH_VALUE;
        pred[s] = -1;
        vSet[s] = true;
    }
    dist[source] = 0;

    /* NEEDS TO BE COMPLETED */
    while (!PQueueIsEmpty())
    {
        Vertex v = leavePQueue(dist);
        for (int j = 0; j < g->nV; j++)
        {
            if (adjacent(g, v, j) != 0)
            {
                // all neighboor
                int alt = g->edges[v][j] + dist[v];
                if (alt < dist[j])
                {
                    dist[j] = alt;
                    pred[j] = v;
                }
            }
        }
    }
    //Pseudocode Dijkstra from wiki
    //while Q is not empty:
    //          u ← vertex in Q with min dist[u]
    //          remove u from Q
    //          for each neighbor v of u:           // only v that are still in Q
    //              alt ← dist[u] + length(u, v)
    //              if alt < dist[v]:
    //                  dist[v] ← alt
    //                  prev[v] ← u
    //
    //      return dist[], prev[]

    (void)vSet;
    for (int i = 0; i < g->nV; i++)
    {
        if (dist[i] == VERY_HIGH_VALUE)
        {
            printf("%d: no path\n", i);
        }
        else
        {
            printf("%d: distance = %d, shortest path: ", i, dist[i]);
            print_path(i, pred);
            printf("\n");
        }
    }
}

void reverseEdge(Edge *e)
{
    Vertex temp = e->v;
    e->v = e->w;
    e->w = temp;
}

int main(void)
{
    Edge e;
    int n, source;

    printf("Enter the number of vertices: ");
    scanf("%d", &n);
    Graph g = newGraph(n);

    printf("Enter the source node: ");
    scanf("%d", &source);
    printf("Enter an edge (from): ");
    while (scanf("%d", &e.v) == 1)
    {
        printf("Enter an edge (to): ");
        scanf("%d", &e.w);
        printf("Enter the weight: ");
        scanf("%d", &e.weight);
        insertEdge(g, e);
        reverseEdge(&e); // ensure to add edge in both directions
        insertEdge(g, e);
        printf("Enter an edge (from): ");
    }
    printf("Done.\n");

    dijkstraSSSP(g, source);
    freeGraph(g);
    return 0;
}