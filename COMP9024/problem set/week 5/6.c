#include "queue.h"

int shortestPath(int source, int target, int forbidden[], int n) {
   int visited[10000];

   int i;
   for (i = 0; i <= 9999; i++)
      visited[i] = -1;             // mark all nodes as unvisited
   for (i = 0; i < n; i++)
      visited[forbidden[i]] = -2;  // mark forbidden nodes as visited => they won't be selected
   visited[source] = source;
   
   queue Q = newQueue();
   QueueEnqueue(Q, source);
   bool found = (target == source);
   while (!found && !QueueIsEmpty(Q)) {
      int v = QueueDequeue(Q);
      if (v == target) {
	 found = true;
      } else {
         int wheel, turn;
         for (wheel = 10; wheel <= 10000; wheel *= 10) { // fancy way of generating the
            for (turn = 1; turn <= 9; turn += 8) {       // eight neighbour configurations of v
	       int w = wheel * (v / wheel) + (v % wheel + (wheel/10) * turn) % wheel;
	       if (visited[w] == -1) {
	          visited[w] = v;
		  QueueEnqueue(Q, w);
	       }
	    }
	 }
      }
   }
   dropQueue(Q);
   if (found) {                     // unwind path to determine length
      int length = 0;
      while (target != source) {
         target = visited[target];  // move to predecessor on path
         length++;
      }
      return length;
   } else {
      return -1;                    // no solution
   }
}
