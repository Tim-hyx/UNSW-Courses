// Graph ADT
// Adjacency Matrix Representation ... COMP9024 20T2
#include "Graph.h"
#include <assert.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct GraphRep
{
    int **edges; // adjacency matrix
    int nV;      // #vertices
    int nE;      // #edges
} GraphRep;

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
    int i, j, min_degree = INT_MAX, max_degree = INT_MIN; //min_degree is a enough small number and max is a enough big number
    for (i = 0; i < n; i++)
    {
        int sum = 0;
        for (j = 0; j < n; j++)
        {
            sum += g->edges[i][j];
        }
        if (sum < min_degree)
        {
            min_degree = sum; //let min = sum
        }
        if (sum > max_degree)
        {
            max_degree = sum; //let max = sum
        }
    }
    printf("Done.\n");
    printf("Minimum degree: %d\n", min_degree);
    printf("Maximum degree: %d\n", max_degree);
    printf("Nodes of minimum degree:\n");
    for (i = 0; i < n; i++)
    {
        int sum = 0;
        for (j = 0; j < n; j++)
        {
            sum += g->edges[i][j];
        }
        if (sum == min_degree) //find the position of value equal to the min
        {
            printf("%d\n", i);
        }
    }
    printf("Nodes of maximum degree:\n");
    for (i = 0; i < n; i++)
    {
        int sum = 0;
        for (j = 0; j < n; j++)
        {
            sum += g->edges[i][j];
        }
        if (sum == max_degree) //find the position of value equal to the max
        {
            printf("%d\n", i);
        }
    }
    printf("Triangles:\n");
    int o, p, q, r;
    for (o = 0; o < n; o++) //all vertices 0,1,2...
    {
        int a[1000], len = 0;
        for (p = 0; p < n; p++) // find all neighbours
        {
            if (p != o)
            {
                if (adjacent(g, o, p))
                {
                    a[len] = p; // record the neighbours,use a set
                    len++;
                }
            }
        }
        // loop through all neigboors
        // q and r are indexs in the set
        for (q = 0; q < len; q++)
        {
            for (r = 0; r < len; r++)
            {
                if (a[q] != a[r])
                {
                    if (adjacent(g, a[q], a[r])) //check neighbours in the set if it's also has the neighbour in the set
                    {
                        if (o < a[q] && a[q] < a[r])
                        {
                            printf("%d-%d-%d\n", o, a[q], a[r]);
                        }
                    }
                }
            }
        }
    }
    freeGraph(g);
}
