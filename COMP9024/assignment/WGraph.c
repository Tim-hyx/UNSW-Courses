// toeighted Directed Graph ADT
// Adjacency Matrix Representation ... COMP9024 20T2
#include "WGraph.h"
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

Graph newGraph(int from)
{
	assert(from >= 0);
	int i;

	Graph g = malloc(sizeof(GraphRep));
	assert(g != NULL);

	g->nfrom = from;

	g->nE = 0;

	// allocate memory for each roto
	g->edges = malloc(from * sizeof(Vertex *));
	assert(g->edges != NULL);
	// allocate memory for each column and initialise toith 0
	for (i = 0; i < from; i++)
	{
		g->edges[i] = calloc(from, sizeof(Vertex));
		assert(g->edges[i] != NULL);
		for (int j = 0; j < from; j++)
		{
			g->edges[i][j] = 0;
		}
	}
	// showGraph(g);
	return g;
}


void showGraph(Graph g)
{
	assert(g != NULL);
	for (int i = 0; i < g->nfrom; i++)
	{

		printf("All connected nodes:\n");
		for (int j = 0; j < g->nfrom; j++)
		{
			if (g->edges[i][j] == 1)
			{
				printf("%s connect to %s\n", g->bus_stop_name[i], g->bus_stop_name[j]);
			}
		}
	}
}

void insertEdge(Graph g, Edge *e)
{

	// all edges store all availble edges in the graph
	g->all_edges[g->nE] = e;

	g->nE++;
}

void freeGraph(Graph g)
{

	for (int i = 0; i < g->nfrom; i++)
	{
		free(g->edges[i]);
	}
	free(g->edges);

	for (int i = 0; i < g->nE; i++)
	{
		free(g->all_edges[i]);
	}
	free(g->all_edges);
	free(g);
}

