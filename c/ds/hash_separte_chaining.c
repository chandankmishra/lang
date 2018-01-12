#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define SIZE 20

struct DataItem {
    int key;   
    int data;   
    struct DataItem *next;
};

struct DataItem* hashArray[SIZE]; 
struct DataItem* dummyItem;
struct DataItem* item;

int hashCode (int key) {
    return key % SIZE;
}

struct DataItem *
search (int key) {
    struct DataItem *temp = NULL;
    //get the hash 
    int hashIndex = hashCode(key);  

    if (hashArray[hashIndex] == NULL) {
        return NULL;
    }

    temp = hashArray[hashIndex];
    while (temp) {
        if (temp->key == key) {
            break;
        }
        temp= temp->next;
    }

    return temp;        
}

void
insert (int key, int data)
{
    struct DataItem *item = (struct DataItem*) malloc(sizeof(struct DataItem));
    item->key = key;  
    item->data = data;  
    item->next = NULL;
    struct DataItem *root = NULL;
    struct DataItem *temp = NULL, *priv = NULL;

    //get the hash 
    int hashIndex = hashCode(key);

    root = hashArray[hashIndex];
    if (root == NULL) {
        hashArray[hashIndex] = item;
        return;
    } else {
        temp = priv = root;
        while (temp != NULL) {
            // if key matches then update the data and return;
            if (temp->key == key) {
                temp->data = data;
                free(item);
                return;
            }
            priv = temp;
            temp = temp->next;
        }
        priv->next = item; 
    }
}

struct DataItem*
delete(struct DataItem* item)
{
    struct DataItem *temp = NULL, *priv = NULL, *root = NULL;
    int key = item->key;

    //get the hash 
    int hashIndex = hashCode(key);
    if (hashArray[hashIndex] == NULL) {
        return NULL;
    }

    root = hashArray[hashIndex];
    if (root->key == item->key) {
        hashArray[hashIndex] = root->next; 
        free(root); 
    } else {
        priv = temp = root;
        while (temp) {
            if (temp->key == key) {
                break;
            }
            priv = temp;
            temp = temp->next;
        }
        if (temp) {
            priv->next = temp->next;
            free(temp);
        }
    }
    return NULL;
}

void display (void) {
    int i = 0;
    struct DataItem* temp = NULL;

    printf("Printing hash table \n");
    for (i = 0; i<SIZE; i++) {
        if (hashArray[i] != NULL) {
            printf("index->%u : value", i);
            temp = hashArray[i];
            while (temp != NULL) {
                printf("->[%u:%u]", temp->key, temp->data);
                temp = temp->next;
            }
            printf("\n");
        }
    }

    printf("\n");
}

int main() {
    dummyItem = (struct DataItem*) malloc(sizeof(struct DataItem));
    dummyItem->data = -1;  
    dummyItem->next = NULL;

    insert(1, 20);
    display();
    insert(1, 21);
    display();
    insert(1, 22);
    display();
    insert(1, 23);
    display();
    insert(2, 70);
    insert(42, 80);
    insert(4, 25);
    insert(12, 44);
    insert(14, 32);
    insert(17, 11);
    insert(13, 78);
    insert(37, 97);

    display();
    item = search(37);

    if (item != NULL) {
        printf("Element found: key:%u val:%d\n", item->key, item->data);
    } else {
        printf("Element %u not found\n", 37);
    }

    delete(item);
    display();
    item = search(37);

    if(item != NULL) {
        printf("Element found: key:%u val:%d\n", item->key, item->data);
    } else {
        printf("Element %u not found\n", 37);
    }

    item = search(17);
    delete(item);
    display();
    item = search(17);
    if(item != NULL) {
        printf("Element found: key:%u val:%d\n", item->key, item->data);
    } else {
        printf("Element %u not found\n", 17);
    }
}
