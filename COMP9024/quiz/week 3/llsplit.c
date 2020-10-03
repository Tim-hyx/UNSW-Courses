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

void splitLL(NodeT *head, NodeT **list1, NodeT **list2)
{
    // need to at least 3 elememnts
    NodeT *normal_speed = head; //point to the linked list head
    NodeT *double_speed = head; //point to the linked list head
    NodeT *prev;
    NodeT *break_point;
    int flag = 0;
    while (double_speed->next != NULL)
    {
        prev = normal_speed;               //remember the previous value
        normal_speed = normal_speed->next; //one step speed
        double_speed = double_speed->next;
        if (double_speed->next != NULL)
        {
            double_speed = double_speed->next; //two steps speed
        }
        else
        {
            // unable to move the second step
            break_point = prev; //even list the second speed points to null
            flag = 1;
            break;
        }
    }
    if (flag == 0) //odd list because double speed points to null and while loop break
    {
        break_point = normal_speed;
    }
    *list2 = break_point->next; //list2 equals to the latter linked list
    break_point->next = NULL;   //break point points to null
    *list1 = head;              //list1 equals to the front list
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
        return 0;
    }
    else
    {
        printf("Done. List is ");
        showLL(all);
    }
    NodeT *head1 = NULL;
    NodeT *head2 = NULL;
    splitLL(all, &head1, &head2);
    if (head1 != NULL)
    {
        printf("\nFirst part is ");
        showLL(head1);
        freeLL(head1);
    }
    if (head2 != NULL)
    {
        printf("\nSecond part is ");
        showLL(head2);
        freeLL(head2);
        // no need to free all because all has been splited into head1 and head2
    }
    return 0;
}
