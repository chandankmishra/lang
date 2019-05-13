#include <stdio.h> 

#define BSIZE 10
typedef struct {
    char buf[BSIZE];
    int count;
    int write_idx;
    int read_idx;
    pthread_mutex_t mutex;
    pthread_cond_t cv_empty;
    pthread_cond_t cv_full;
	capacity;
} buffer_t;

buffer_t buffer;

void producer(buffer_t *b, char item)
{
    pthread_mutex_lock(&b->mutex);
   
    while (b->count >= BSIZE)
        pthread_cond_wait(&b->cv_full, &b->mutex);

    assert(b->count < BSIZE);

	b->write_idx = (b->write_idx + 1) % BSIZE
    b->buf[b->write_idx] = item;
    b->count++;

    /* now: either b->count < BSIZE and b->write_idx is the index
       of the next empty slot in the buffer, or
       b->count == BSIZE and b->write_idx is the index of the
       next (count) slot that will be emptied by a consumer
       (such as b->write_idx == b->read_idx) */

    pthread_cond_signal(&b->cv_empty);
    pthread_mutex_unlock(&b->mutex);
}


char consumer(buffer_t *b)
{
    char item;
    pthread_mutex_lock(&b->mutex);
    while(b->count <= 0)
        pthread_cond_wait(&b->cv_empty, &b->mutex);

    assert(b->count > 0);
	
	b->read_idx = (b->read_idx + 1) % BSIZE
    item = b->buf[b->read_idx];
    b->count--;

    /* now: either b->count > 0 and b->read_idx is the index
       of the next count slot in the buffer, or
       b->count == 0 and b->read_idx is the index of the next
       (empty) slot that will be filled by a producer (such as
       b->read_idx == b->write_idx) */

    pthread_cond_signal(&b->cv_full);
    pthread_mutex_unlock(&b->mutex);

    return(item);
}



