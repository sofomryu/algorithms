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

	node* p =malloc(sizeof(node));
	p->x=4;
	p->next = n->next->next;
	n->next->next = p;

	p=n;

	node* s = malloc(sizeof(node));
	s->x=1;
	s->next=n;
	n=s;
	

	printf("%i",n->x);
	printf("%i",n->next->x);
	printf("%i",n->next->next->x);
	printf("%i",n->next->next->next->x);
	printf("%i",n->next->next->next->next->x);
	free(n);
}
