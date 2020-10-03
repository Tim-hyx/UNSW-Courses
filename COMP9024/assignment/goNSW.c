/* The time complexity of the program is O(m*n), if assume that
1. the number of stops, n
2. the number of schedules, m
3. the maximum number k of stops on a single train, bus or light rail line.
because there are two for loop in the main code. */

#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "PQueue.h"
void dijkstraSSSP(Graph g, char source[], char prev[][MAX_STOP_NAME], char target[], int prev_arrive_time[]);

int time_current[100];
int main()
{
	printf("Enter the total number of stops on the network: ");
	int total_nb_stops;
	scanf("%d", &total_nb_stops);
	Graph g = newGraph(total_nb_stops);
	for (int i = 0; i < total_nb_stops; i++)
	{
		scanf("%s", g->bus_stop_name[i]);
	}
	printf("Enter the number of schedules: ");
	int nb_schedules;
	scanf("%d", &nb_schedules);
	for (int j = 0; j < nb_schedules; j++)
	{
		printf("Enter the number of stops: ");
		int nb_stops;
		scanf("%d", &nb_stops);
		int first_time = true;
		int prev_to_time;
		char prev_stop_to[MAX_STOP_NAME];
		int prev_to_index;
		for (int n = 0; n < nb_stops - 1; n++)
		{
			// in the first time, read first four data to make from and to (time and stop names)
			if (first_time)
			{
				int time1, time2;
				char stop_from[MAX_STOP_NAME];
				char stop_to[MAX_STOP_NAME];
				scanf("%d%s%d%s", &time1, stop_from, &time2, stop_to);
				Edge *e = (Edge *)malloc(sizeof(Edge));
				assert(e != NULL);
				// find the index of from and to stops
				int i = find_index_bus_stop(g->bus_stop_name, total_nb_stops, stop_from);
				int j = find_index_bus_stop(g->bus_stop_name, total_nb_stops, stop_to);
				g->edges[i][j] = 1;
				// start time is just use to filter out schedule
				// when u miss the bus
				e->start_time = time1;
				e->from = i;
				e->to = j;
				e->arrival_time = time2;
				// insert into graph
				insertEdge(g, e);
				// copy value for next loop
				strcpy(prev_stop_to, stop_to);
				prev_to_time = time2;
				prev_to_index = j;
				first_time = false;
			}
			else
			{
				//except the first time, just read two data because the from is the pervious stop and
				// to is the data to read
				int time2;
				char stop_to[MAX_STOP_NAME];
				Edge *e = (Edge *)malloc(sizeof(Edge));
				assert(e != NULL);
				scanf("%d%s", &time2, stop_to);
				int i = prev_to_index;
				int j = find_index_bus_stop(g->bus_stop_name, total_nb_stops, stop_to);
				g->edges[i][j] = 1;
				e->start_time = prev_to_time;
				e->arrival_time = time2;
				e->from = i;
				e->to = j;
				insertEdge(g, e);
				// start copy in prev
				strcpy(prev_stop_to, stop_to);
				prev_to_time = time2;
				prev_to_index = j;
			}
		}
	}
	while (true)
	{
		char from[31], to[31];
		int depart;
		printf("\n");
		printf("From: ");
		scanf("%s", from);
		if (strcmp(from, "done") == 0)
		{
			printf("Thank you for using goNSW.\n");
			return 0;
		}
		printf("To: ");
		scanf("%s", to);
		printf("Depart at: ");
		scanf("%d", &depart);
		printf("\n");
		char prev[100][MAX_STOP_NAME];
		int prev_arrive_time[100];
		for (int i = 0; i < g->nfrom; i++)
		{
			// make all the stops as a large number
			strcpy(prev[i], "UNDEFINED");
			prev_arrive_time[i] = 0;
		}
		// make the last arrive time as depart time
		prev_arrive_time[find_index_bus_stop(g->bus_stop_name, g->nfrom, from)] = depart;
		//use dijkstra algorithm to find the shortest path
		dijkstraSSSP(g, from, prev, to, prev_arrive_time);
		int current = find_index_bus_stop(g->bus_stop_name, g->nfrom, from);
		// if is large number, there's no path
		if (strcmp("UNDEFINED", prev[current]) == 0)
		{
			printf("No connection found.\n");
		}
		else
		{
			// print the path
			for (int i = 0; i < g->nE; i++)
			{
				if (strcmp(g->bus_stop_name[g->all_edges[i]->from], from) == 0)
				{
					printf("%04d", g->all_edges[i]->start_time);
					break;
				}
			}
			printf(" %s\n", from);
			while (strcmp("UNDEFINED", prev[current]) != 0)
			{
				printf("%04d %s\n", time_current[current], prev[current]);
				current = find_index_bus_stop(g->bus_stop_name, g->nfrom, prev[current]);
			}
		}
	}
	freeGraph(g);
	return 0;
}

int find_index_bus_stop(char arr[][MAX_STOP_NAME], int len, char target[])
{
	for (int i = 0; i < len; i++)
	{
		if (strcmp(target, arr[i]) == 0)
		{
			return i;
		}
	}
	return -1;
}
// Vertex source
void dijkstraSSSP(Graph g, char source[], char prev[][MAX_STOP_NAME], char target[], int prev_arrive_time[])
{

	PQueueInit();
	for (int i = 0; i < g->nfrom; i++)
	{
		Vertex *v = (Vertex *)malloc(sizeof(Vertex));
		assert(v != NULL);
		if (strcmp(source, g->bus_stop_name[i]) == 0)
		{
			v->cost_to_get_here = 0;
		}
		else
		{
			v->cost_to_get_here = VERY_HIGH_VALUE;
		}
		strcpy(v->from, g->bus_stop_name[i]);
		joinPQueue(*v);
	}
	while (!PQueueIsEmpty())
	{
		Vertex v = leavePQueue();
		if (strcmp(v.from, target) == 0)
		{
			return;
		}
		for (int i = 0; i < g->nfrom; i++)
		{
			int index_from = find_index_bus_stop(g->bus_stop_name, g->nfrom, v.from);
			if (g->edges[index_from][i] == 1)
			{
				// connected
				// need to find that edge
				Edge e;
				bool find_edge = false;
				for (int j = 0; j < g->nE; j++)
				{
					if (g->all_edges[j]->from == index_from && g->all_edges[j]->to == i)
					{
						e = *g->all_edges[j];
						find_edge = true;
						break;
					}
				}
				if (find_edge)
				{
					if (prev_arrive_time[index_from] <= e.start_time)
					{
						// Relaxation of an edge in Dijkstra's algorithm
						int alt = v.cost_to_get_here + e.arrival_time - prev_arrive_time[e.from];
						// get distance at a node in q
						// updata distance at a node at q
						if (alt < getWeight(g->bus_stop_name[i]))
						{
							updataWeight(g->bus_stop_name[i], alt);
							// store in the previous array for find the path in the future
							strcpy(prev[index_from], g->bus_stop_name[i]);
							time_current[e.from] = e.arrival_time;
							prev_arrive_time[e.to] = e.arrival_time;
						}
					}
				}
			}
		}
	}
}


