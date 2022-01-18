#include <stdio.h>
#include <stdlib.h>

int main(void) {
	typedef struct node {
		int x;
		struct node* next;
	}
	node;

	node n;
	n.x = 2;
	n.next = NULL;

	node m;
	m.x=3;
	m.next =NULL;
	n.next=&m;

	node o;
	o.x=5;
	o.next=NULL;
	m.next=&o;

	node p;
	p.x=4;
	p.next = &o;
	m.next= &p;

	node s;
	s.x=1;
	s.next=&n;

	n=s;
	

	printf("%i",n.x);
	printf("%i",n.next->x);
	printf("%i",n.next->next->x);
	printf("%i",n.next->next->next->x);
	printf("%i",n.next->next->next->next->x);
}
