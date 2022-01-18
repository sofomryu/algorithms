#include <stdio.h>
#include <stdlib.h>

int main(void) {
	typedef struct node {
		int x;
		struct node* next;
	}
	node;

	node n;
	n.x = 1;
	n.next = NULL;

	node m;
	m.x=2;
	m.next =NULL;
	n.next=&m;

	node o;
	o.x=3;
	o.next=NULL;
	m.next=&o;

	printf("%i",n.x);
	printf("%i",n.next->x);
	printf("%i",n.next->next->x);
}
