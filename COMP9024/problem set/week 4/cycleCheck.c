// Graph ADT
// Adjacency Matrix Representation ... COMP9024 20T2
#include "Graph.h"
#include <assert.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct GraphRep
{
    int **edges; // adjacency matrix
    int nV;      // #vertices
    int nE;      // #edges
} GraphRep;

int visisted[1000];

bool dfsCycleCheck(Graph g, Vertex v, Vertex from, int nV)
{
    visisted[v] = from;
    for (int i = 0; i < nV; i++)
    {
        if (adjacent(g, v, i))
        {
            if (i == from)
            {
                continue; //should exclude the neighbour of v from which you just came, so as to prevent a single edge w-v from being classified as a cycle.
            }
            if (visisted[i] != -1)
            {
                return true; //find the cycle
            }
            else if (dfsCycleCheck(g, i, v, nV))
            {
                return true; //recrusive to find cycle if this node is not visited,see it as new start
            }
        }
    }
    return false; // no cycle at v
}

bool finished = false;

bool hasCycle(Graph g, int nV)
{
    int nextNode = 0;
    while (finished == false)
    {
        finished = true;
        for (int i = 0; i < nV; i++)
        {
            if (visisted[i] == -1)
            {
                nextNode = i; //find next node which is not visited
                finished = false;
                break;
            }
        }
        if (!finished)
        {
            if (dfsCycleCheck(g, nextNode, INT_MAX, nV))
            {
                return true;
            }
        }
    }
    return false;
}

int main()
{
    int n, TF = 1;
    Edge e;
    printf("Enter the number of vertices: ");
    scanf("%d", &n);
    Graph g = newGraph(n);
    while (TF)
    {
        printf("Enter an edge (from): ");
        TF = scanf("%d", &e.w);
        if (TF)
        {
            printf("Enter an edge (to): ");
            TF = TF && scanf("%d", &e.v);
            insertEdge(g, e);
        }
    }
    printf("Done.\n");
    for (int i = 0; i < n; i++)
    {
        visisted[i] = -1;
    }
    if (hasCycle(g, n))
    {
        printf("The graph has a cycle.\n");
    }
    else
    {
        printf("The graph is acyclic.\n");
    }
}
