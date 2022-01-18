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
	

	node* temp = malloc(sizeof(node));
	temp->x=3;
	temp->next = NULL;
	n->next = temp;
	

	temp = malloc(sizeof(node));
	temp->x=5;
	temp->next = NULL;
	n->next->next = temp;


	/*

	node* p =malloc(sizeof(node));
	p->x=4;
	p->next = n->next->next;
	n->next->next = p;

	p=n;

	node* s = malloc(sizeof(node));
	s->x=1;
	s->next=n;
	n=s;
	*/

	printf("%i",n->x);
	printf("%i",n->next->x);
	printf("%i",n->next->next->x);
//	printf("%i",n->next->next->next->x);
//	printf("%i",n->next->next->next->next->x);
	free(n->next->next);
	free(n->next);
	free(n);
}
