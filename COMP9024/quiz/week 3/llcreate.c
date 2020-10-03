#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
typedef struct node
{
    int data;
    struct node *next;
} NodeT; // taken from the lecture

void freeLL(NodeT *list)
{
    NodeT *p, *temp;
    p = list;
    while (p != NULL)
    {
        temp = p->next;
        free(p);
        p = temp;
    }
} // taken from the lecture

void showLL(NodeT *list)
{
    NodeT *p;
    p = list;
    while (p != NULL)
    {
        printf("%d", p->data);
        p = p->next;
        if (p != NULL)
        {
            printf("-->");
        }
    }
}

NodeT *makeNode(int v)
{
    NodeT *new = malloc(sizeof(NodeT));
    assert(new != NULL);
    new->data = v;    // initialise data
    new->next = NULL; // initialise link to next node
    return new;       // return pointer to new node
} //take from the lecture

NodeT *joinLL(NodeT *list, int v)
{
    NodeT *new = makeNode(v); // create new list element
    NodeT *p;
    p = list;
    if (p != NULL)
    {
        while (p->next != NULL)
        {
            p = p->next;
        }                 // literate over the linked list and p points to the last node
        p->next = new;    // p points to the new end
        new->next = NULL; // new end points to NULL
    }
    else
    {
        list = new;
    }
    return list; // new element is new end
}

int main()
{
    int n;
    NodeT *all = NULL;
    printf("Enter an integer: ");
    while (scanf("%d", &n) == 1)
    {
        all = joinLL(all, n);
        printf("Enter an integer: ");
    }
    if (all == NULL)
    {
        printf("Done.\n");
    }
    else
    {
        printf("Done. List is ");
        showLL(all);
        freeLL(all);
    }
    return 0;
}
