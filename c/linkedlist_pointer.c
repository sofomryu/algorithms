#include <stdio.h>
#include <stdlib.h>

int main(void) {
	typedef struct node {
		int x;
		struct node* next;
	}
	node;

	node* n =malloc(sizeof(node));
	n->x = 2;
	n->next = NULL;

	node* m = malloc(sizeof(node));
	m->x=3;
	m->next = NULL;
	n->next = m;

	node* o = malloc(sizeof(node));
	o->x=5;
	o->next = NULL;
	m->next = o;

	o=n;
	m=n;

	printf("%i",n->x);
	printf("%i",n->next->x);
	printf("%i",n->next->next->x);
	free(n);
}
