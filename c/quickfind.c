#include <stdio.h>


void main(void) {
	int i, p , q, t, N, id[N];
	N=10000;
	for ( i =0; i < N; i++) {
		id[i] = i;}
	while (scanf("%d %d\n", &p, &q) ==2) {
		if (id[p] == id[q]) {
			continue;}
		for (t= id[p], i=0; i<N; i++) {
			if (id[i] ==t) {
				id[i] =id[q];}
		}
		printf(" %d %d\n", p, q);
	}
}
