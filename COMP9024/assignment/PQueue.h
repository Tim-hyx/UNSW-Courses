// Priority Queue ADO header ... COMP9024 20T2

#include "WGraph.h"
#include <stdbool.h>

#define MAX_NODES 1000

typedef struct
{
	Vertex item[MAX_NODES]; // array of vertices currently in queue
	int length;				// #values currently stored in item[] array
} PQueueT;
static PQueueT *q;
void PQueueInit();
void joinPQueue(Vertex);
Vertex leavePQueue();
bool PQueueIsEmpty();
int getWeight(char v[]);
void updataWeight(char v[], int weight);
void freeQueue();
