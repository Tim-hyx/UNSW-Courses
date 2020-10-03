// Priority Queue ADO implementation ... COMP9024 20T2

#include "PQueue.h"
#include <assert.h>
#include <stdlib.h>
#include <string.h>
#define VERY_HIGH_VALUE 999999

void PQueueInit()
{
	q = (PQueueT *)malloc(sizeof(PQueueT));
	q->length = 0;
}
void joinPQueue(Vertex v)
{
	q->item[q->length] = v;
	q->length++;
}

// return the vertex has the highest pority
Vertex leavePQueue()
{
	int highest_priority = VERY_HIGH_VALUE + 1;
	Vertex result = *(Vertex *)malloc(sizeof(Vertex));
	for (int i = 0; i < q->length; i++)
	{
		if (q->item[i].cost_to_get_here < highest_priority)
		{
			highest_priority = q->item[i].cost_to_get_here;
		}
	}
	for (int i = 0; i < q->length; i++)
	{
		if (q->item[i].cost_to_get_here == highest_priority)
		{
			result = q->item[i];
			// copy the last elemet to current pos
			q->item[i] = q->item[q->length - 1];
			q->length--;
			break;
		}
	}
	return result;
}
bool PQueueIsEmpty()
{
	return q->length == 0;
}

int getWeight(char v[])
{
	for (int i = 0; i < q->length; i++)
	{

		if (strcmp(v, q->item[i].from) == 0)
		{
			return q->item[i].cost_to_get_here;
		}
	}
	return -1;
}

void updataWeight(char v[], int weight)
{
	for (int i = 0; i < q->length; i++)
	{

		if (strcmp(v, q->item[i].from) == 0)
		{
			q->item[i].cost_to_get_here = weight;
		}
	}
}

void freeQueue()
{
	free(q);
}

