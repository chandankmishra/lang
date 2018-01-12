#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct node {
    int data;
    struct node * next;
};

void append(struct node **, int);
void display(struct node *);
void delete_by_key(struct node **, int);
int  length_iterative(struct node *head);
int  length_recursive(struct node *head);
bool search_iterative(struct node *head, int x);
bool search_recursive(struct node *head, int x);
int  find_middle(struct node *head);
int  get_nth(struct node *head, int index);
void delete_llist_all(struct node **headref);
void sorted_insert(struct node **headref);
int  get_nth_value_from_last(struct node *head, int loc, int *count);
int  get_nth_from_last(struct node *head, int loc);
int  get_nth_from_last2(struct node *head, int loc);
int  get_nth_from_last3(struct node *head, int loc);
int  get_value_count(struct node *head, int value);
void reverse_iterative (struct node **headref);
void reverse_recursive(struct node **headref);
void merge(struct node *head1, struct node *head2, struct node **head3);
struct node * sorted_merge(struct node *head1, struct node *head2);
void print_reverse (struct node *head);
void move_last_to_front(struct node **headref); 
void move_first_to_last(struct node **headref);
void rotate_counter_clock_llist(struct node **headref, int k);
void rotate_clockwise_llist(struct node **headref, int k);
void delete_alt_node(struct node **headref);
void merge_at_alt_location(struct node **headref1, struct node **headref2);

int main (void)
{
    struct node *head1 = NULL;
    struct node *head2 = NULL;
    struct node *head3 = NULL;

    append(&head1, 2);
    append(&head1, 2);
    append(&head1, 1);
    append(&head1, 3);
    append(&head1, 2);
    append(&head1, 4);
    append(&head1, 2);
    append(&head1, 5);
    append(&head1, 6);
    display(head1);

    //4
    printf("4) after deleting key 2: ");
    delete_by_key(&head1, 2);
    display(head1);

    //7
    printf("7) iterative count %d\n", length_iterative(head1));
    printf("7) recursive count %d\n", length_recursive(head1));

    //8
    printf("8) iterative search %d %d\n", 8, search_iterative(head1, 8));
    printf("8) iterative search %d %d\n", 5, search_iterative(head1, 5));

    printf("8) recursive search %d %d\n", 8, search_recursive(head1, 8));
    printf("8) recursive search %d %d\n", 5, search_recursive(head1, 5));

    //14
    printf("11) deleting all elements: ");
    delete_llist_all(&head1);

    //Load new data
    append(&head1, 1);
    append(&head1, 3);
    append(&head1, 5);
    append(&head1, 6);
    append(&head1, 7);
    append(&head1, 8);
    append(&head1, 9);
    append(&head1, 10);
    display(head1);

    //11
    printf("11) get_nth %d element is %d\n", 0, get_nth(head1, 0));
    printf("11) get_nth %d element is %d\n", 2, get_nth(head1, 2));

    //12
    printf("12) middle element is %d\n", find_middle(head1));

    //13
    printf("13) nth(%d) from last is %d\n", 0, get_nth_from_last2(head1, 0));
    printf("13) nth(%d) from last is %d\n", 1, get_nth_from_last2(head1, 1));
    printf("13) nth(%d) from last is ", 3);
    get_nth_from_last(head1, 3);

    //14
    printf("15) get_value_count %d occured %d times\n", 3, get_value_count(head1, 3));

    //15
    reverse_iterative(&head1);
    printf("16) reverse_iterative linked list is ");
    display(head1);
    reverse_recursive(&head1);
    printf("16) reverse_recursive linked list is ");
    display(head1);

    append(&head2, 2);
    append(&head2, 4);
    append(&head2, 6);
    append(&head2, 8);
    append(&head2, 10);
    append(&head2, 12);
    append(&head2, 14);
    printf("18) head1 ");
    display(head1);
    printf("18) head2 ");
    display(head2);
    printf("18) head3 ");
    merge(head1, head2, &head3);
    //head3= sorted_merge(head1, head2);
    display(head3);
    //TBD 22 Function to check if a singly linked list is palindrome
    //TBD 23 Intersection point of two Linked Lists.
    //24
    printf("24) orignal: ");
    display(head1);
    printf("24) print reverse: ");
    print_reverse(head1);
    printf("\n");

    printf("29) move last element to front: ");
    move_last_to_front(&head1);
    display(head1);
    printf("29) move first element to last: ");
    move_first_to_last(&head1);
    display(head1);
    printf("44) rotate counter clock by 4: ");
    rotate_counter_clock_llist(&head1, 4);
    display(head1);
    printf("44) rotate clockwise by 4: ");
    rotate_clockwise_llist(&head1, 4); //revisit
    display(head1);
    printf("31) delete alternative node: ");
    delete_alt_node(&head1);
    display(head1);
    
    //repopulate
    delete_llist_all(&head1);
    delete_llist_all(&head2);
    delete_llist_all(&head3);

    //Load new data
    append(&head1, 5);
    append(&head1, 7);
    append(&head1, 17);
    append(&head1, 13);
    append(&head1, 11);
    append(&head2, 12);
    append(&head2, 10);
    append(&head2, 2);
    append(&head2, 4);
    append(&head2, 6);
    append(&head2, 7);
    append(&head2, 8);
    printf("51) first list: ");
    display(head1);
    printf("51) second list: ");
    display(head2);

    merge_at_alt_location(&head1, &head2);
    printf("51) first list: ");
    display(head1);
    printf("51) second list: ");
    display(head2);

    return 0;
}

//51
void
merge_at_alt_location(struct node **headref1, struct node **headref2)
{
    struct node *head1 = *headref1, *head2 = *headref2;
    struct node *head1_next = NULL, *head2_next = NULL;

    while (head1 != NULL && head2 != NULL)
    {
        head1_next = head1->next;
        head2_next = head2->next;

        head1->next = head2;
        head2->next = head1_next;

        head1 = head1_next;
        head2 = head2_next;
    }

    *headref2 = head2; 
}

//31
void delete_alt_node(struct node **headref) //revisit implement recursive
{
    struct node *temp = NULL, *curr = NULL, *next = NULL;

    next = *headref;

    while (next && next->next) {
        curr = next;
        temp = next->next;
        next = next->next->next; 
        curr->next = next;
        free(temp);
    }
}

//29 Move first element to last of a given Linked List
void move_first_to_last (struct node **headref)
{
    struct node *last = NULL, *priv = NULL;

    last = *headref;
    /* return if the list is empty or having single node */
    if (last == NULL || last->next == NULL) {
        return;
    }

    while (last->next != NULL) {
        last = last->next;
    }
    priv = *headref;
    last->next = priv;
    *headref = priv->next;
    priv->next = NULL;
}

//44.1 rotate a linked list clockwise
struct node *get_nth_ptr_value_from_last (struct node *head, int loc, int *count)
{
    struct node *val = 0;

    if (head == NULL) {
        return NULL;
    }

    val = get_nth_ptr_value_from_last(head->next, loc, count);
    if (val != NULL) {
        return val;
    }

    //printf("count %d loc %d val %d head->data %d\n", *count, loc, val, head->data);
    if (*count == loc) {
        return head;
    }
    *count = *count + 1;

    return NULL;
}
void rotate_clockwise_llist (struct node **headref, int k)
{
    struct node *knode = NULL, *last = NULL; 

    last = *headref;
    while (last->next != NULL) {
        last = last->next;
    }

    int count = 0;
    knode = get_nth_ptr_value_from_last(*headref, k, &count);

    last->next  = *headref;
    *headref    = knode->next;
    knode->next = NULL;
}

//44 Rotate a Linked List
void rotate_counter_clock_llist(struct node **headref, int k)
{
    struct node *knode = NULL, *last = NULL; 

    last = *headref;
    while (last->next != NULL) {
        if (--k == 0) {
            knode = last;
        }
        last = last->next;
    }

    last->next  = *headref;
    *headref    = knode->next;
    knode->next = NULL;
}

//29 Move last element to front of a given Linked List
void move_last_to_front(struct node **headref)
{
    struct node *temp = NULL, *priv = NULL;

    temp = *headref;
    /* return if the list is empty or having single node */
    if (temp == NULL || temp->next == NULL) {
        return;
    }

    while (temp->next != NULL) {
        priv = temp;
        temp = temp->next;
    }
    priv->next = NULL;
    temp->next = *headref; 
    *headref = temp;
}

void  print_reverse (struct node *head)
{
    if (head == NULL) {
        return;
    }

    print_reverse(head->next);

    printf("%d ", head->data);
}

//18 Merge two sorted linked lists
struct node * sorted_merge(struct node *head1, struct node *head2)
{
    struct node *result = NULL;

    if (head1 == NULL) {
        return head2;
    } else if (head2 == NULL) {
        return head1;
    }

    if (head1->data < head2->data) {
        result = head1;
        result->next = sorted_merge(head1->next, head2);
    } else {
        result = head2;
        result->next = sorted_merge(head1, head2->next);
    }
    return result;
}

void merge(struct node *head1, struct node *head2, struct node **head3)
{
    struct node *result = NULL;

    if (head1 == NULL && head2 == NULL) { 
        return;
    }

    while (head1 != NULL && head2 != NULL) {
        if (*head3 == NULL) {
            *head3  = (struct node *)malloc(sizeof(struct node));
            result    = *head3;
        } else {
            result->next = (struct node *)malloc(sizeof(struct node));
            result = result->next;
        }

        if (head1->data < head2->data) {
            result->data  = head1->data;
            head1       = head1->next;
        } else if (head1->data > head2->data) {
            result->data  = head2->data;
            head2       = head2->next;
        } else if (head1->data == head2->data) {
            result->data  = head2->data;
            head1       = head1->next;
            head2       = head2->next;
        }
    }

    while  (head1 != NULL) {
        if (*head3 == NULL) {
            *head3  = (struct node *)malloc(sizeof(struct node));
            result    = *head3;
        } else {
            result->next = (struct node *)malloc(sizeof(struct node));
            result = result->next;
        }
        result->data = head1->data;
        head1 = head1->next;
    }

    while (head2 != NULL) {
        if (*head3 == NULL) {
            *head3  = (struct node *)malloc(sizeof(struct node));
            result    = *head3;
        } else {
            result->next = (struct node *)malloc(sizeof(struct node));
            result = result->next;
        }
        result->data = head2->data;
        head2 = head2->next;
    }
    result->next = NULL;
}

//16 Reverse a linked list
void reverse_iterative (struct node **headref)
{
    struct node *r = NULL, *priv = NULL, *current = *headref;
    while (current != NULL) {
        priv        = r;
        r           = current;
        current     = current->next;
        r->next     = priv;
    }
    *headref = r;
}

void reverse_recursive_node (struct node *cur, struct node *priv, struct node **head)
{
    struct node *next = NULL;

    if (cur->next == NULL) {
        cur->next = priv;
        *head = cur;
        return;
    }

    next = cur->next;
    cur->next = priv;

    reverse_recursive_node(next, cur, head);
}

void reverse_recursive(struct node **head)
{
    if (head == NULL) {
        return;
    }

    reverse_recursive_node(*head, NULL, head);
}

//15 Write a function that counts the number of times a given int occurs in a Linked List
int get_value_count(struct node *head, int value)
{
    struct node *temp = head;
    int          count = 0;

    while (temp) {
        if (temp->data == value) {
            count++;
        }
        temp = temp->next;
    }
    return count;
}

//13 Nth node from the end of a Linked List (Method 1)
int get_nth_from_last(struct node *head, int n)
{
    if (head == NULL)
        return n;

    n = get_nth_from_last(head->next, n);

    if (n==0)
        printf("%d\n", head->data);

    return n-1;
}


//13 Nth node from the end of a Linked List (Method 2)
int get_nth_value_from_last (struct node *head, int loc, int *count)
{
    int val = 0;

    if (head == NULL) {
        return 0;
    }

    val = get_nth_value_from_last(head->next, loc, count);
    if (val) {
        return val;
    }

    //printf("count %d loc %d val %d head->data %d\n", *count, loc, val, head->data);
    if (*count == loc) {
        return head->data;
    }
    *count = *count + 1;

    return 0;
}

int get_nth_from_last2 (struct node *head, int loc)
{
    int  count = 0;

    return get_nth_value_from_last(head, loc, &count);
}

//13 Nth node from the end of a Linked List (Method 3)
int get_nth_from_last3 (struct node *head, int loc)
{
    static int  count   = 0;
    int         val     = 0;

    if (head == NULL) {
        return 0;
    }

    val = get_nth_from_last3(head->next, loc);
    if (val) {
        return val;
    }

    //printf("count %d loc %d val %d head->data %d\n", count, loc, val, head->data);
    if (count == loc) {
        return head->data;
    }
    count = count + 1;

    return 0;
}

//20 Given a linked list which is sorted, how will you insert in sorted way
//void sorted_insert (struct node **headref);

//14 Write a function to delete a Linked List
void delete_llist_all (struct node **headref)
{
    struct node *current = *headref, *temp = NULL;

    while (current != NULL) {
        temp = current;
        current = current->next;
        free(temp);
    }

    *headref = NULL;
}

//11 Write a function to get Nth node in a Linked List
int get_nth (struct node *head, int index)
{
    struct node *temp = head;
    int idx = 0;
  
    while (temp) {
        if (idx == index) {
            return temp->data;
        }
        temp=temp->next;
        idx++;
    }

    return 0;
}

//12 Print the middle of a given linked list
int find_middle (struct node *head)
{
    struct node *slowp, *fastp;

    if (head==NULL) {
        return 0;
    }

    slowp = fastp = head;
    while (fastp && fastp->next) {
        slowp = slowp->next; 
        fastp = fastp->next->next;
    }
    return slowp->data;
}

//7 Find Length of a Linked List (Iterative and Recursive)
int length_iterative (struct node *head)
{
    struct node *temp = NULL;
    int          count = 0;

    temp = head;
    while (temp) {
        temp = temp->next;
        count++;
    }
    return count;
}

int length_recursive (struct node *head)
{
    if (head == NULL) {
        return 0;
    }

    return length_recursive(head->next) + 1;
}

//8 Search an element in a Linked List (Iterative and Recursive)
bool search_iterative(struct node *head, int x)
{
    struct node *temp = head;

    while (temp != NULL) {
        if (temp->data == x) {
            return 1;
        }
        temp = temp->next;
    }
    return 0;
}
bool search_recursive(struct node *head, int x)
{
    struct node *temp = head;

    if (temp == NULL) {
        return 0;
    }

    if (temp->data == x) {
        return 1;
    }

    return search_recursive(temp->next, x);
}

//4 Linked List Deletion (Deleting a given key)
//Delete all occurrences of a given key in a linked list
void delete_by_key(struct node **head_ref, int key)
{
    struct node *temp = *head_ref, *next, *priv;

    while (temp != NULL && temp->data == key) {
        *head_ref = temp->next;
        free(temp);
        temp= *head_ref;
    }

    while (temp != NULL) {
        next = temp->next;
        if (temp->data == key) {
            priv->next = next;
            free(temp);
        } else {
            priv = temp;
        }
        temp = next;
    }
}

void append (struct node **pptr, int data)
{
    struct node *p = NULL;
    struct node *temp = NULL;

    p = (struct node *)malloc(sizeof(struct node));
    p->data = data;
    p->next = NULL;

    if (*pptr == NULL) {
        *pptr = p;
    } else {
        temp = *pptr;
        while (temp->next != NULL) { //revisit
            temp = temp->next;
        }
        temp->next = p;
    }
}

void display (struct node *p)
{
    printf("current elements : ");
    while (p != NULL) {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}
