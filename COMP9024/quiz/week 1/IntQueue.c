// Queue ADO implementation ... COMP9024 20T2

#include "IntQueue.h"

typedef struct {
   int item[MAXITEMS];
   int  end;
} queueRep;                   // defines the Data Structure

static queueRep queueObject;  // defines the Data Object

void QueueInit() {            // set up empty queue
   queueObject.end = 0;
}

int QueueIsEmpty() {          // check whether queue is empty
   return (queueObject.end == 0);
}

void QueueEnqueue(int ch) {     // insert int at end of queue
   queueObject.item[queueObject.end] = ch;
   queueObject.end++;
}

int QueueDequeue() {             // remove int from front of queue
   if(QueueIsEmpty()){        // could print an error message here
   return 0;
   }
    int ch = queueObject.item[0];
    for (int i = 1; i <= queueObject.end; i++)
    {
       queueObject.item[i - 1] = queueObject.item[i];
    }
    queueObject.end--;
    return ch;
}
