// Weighted Directed Graph ADT
// Adjacency Matrix Representation ... COMP9024 20T2
#include "WGraph.h"
#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct GraphRep
{
    int **edges; // adjacency matrix storing positive weights
        // 0 if nodes not adjacent
    int nV; // #vertices
    int nE; // #edges
} GraphRep;

typedef struct rank //record the i and output
{
    int i;
    double score;
} rank;

int comparator(const void *p, const void *q) //how to sort
{
    // Get the values at given addresses
    rank l = *(const rank *)p;
    rank r = *(const rank *)q;
    if (l.score == r.score)
    {
        return l.i > r.i;
    }
    return l.score < r.score;
}

int main()
{
    int n, from, to;
    Edge e;
    printf("Enter the number of vertices: ");
    scanf("%d", &n);
    Graph g = newGraph(n);
    while (true)
    {
        printf("Enter an edge (from): ");
        if (scanf("%d", &from) != 1)
        {
            break;
        }
        printf("Enter an edge (to): ");
        if (scanf("%d", &to) != 1)
        {
            return 1;
        }
        e.v = from;
        e.w = to;
        e.weight = 1;
        insertEdge(g, e);
    }
    printf("Done.\n");
    printf("\n");
    printf("Popularity ranking:\n");
    double inDegree[n], outDegree[n];
    for (int i = 0; i < n; i++)
    {
        outDegree[i] = 0;
        for (int j = 0; j < n; j++)
        {
            outDegree[i] += g->edges[i][j];
        }

        if (outDegree[i] == 0)
        {

            outDegree[i] = 0.5;
        }
    }
    for (int i = 0; i < n; i++)
    {
        inDegree[i] = 0;
        for (int j = 0; j < n; j++)
        {
            inDegree[i] += g->edges[j][i];
        }
    }
    double output[n];
    rank *r = malloc(n * sizeof(rank));
    assert(r != NULL);
    for (int i = 0; i < n; i++)
    {
        output[i] = inDegree[i] / outDegree[i];
        r[i].i = i;
        r[i].score = output[i];
    }
    qsort((void *)r, n, sizeof(r[0]), comparator); //quicksort
    for (int i = 0; i < n; i++)
    {
        printf("%d %.1f\n", r[i].i, r[i].score);
    }
    freeGraph(g);
    free(r);
    return 0;
}
