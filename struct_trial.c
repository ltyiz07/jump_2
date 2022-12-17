#include <stdio.h>
#include <stdlib.h>

typedef struct tagNode {
     int key;
     void* value;
} Node;

int main(void) {
     Node n;
     Node* n_p = &n;

     int node_ar_size = 10;
     Node* node_ar = malloc(sizeof(Node) * node_ar_size);

     for (int i = 0; i < node_ar_size; i++) {
          node_ar[i].key = i;
     }
     for (int i = 0; i < node_ar_size; i++) {
          printf("key: %d\n", node_ar[i].key);
     }


     free(node_ar);

     return 0;
}
