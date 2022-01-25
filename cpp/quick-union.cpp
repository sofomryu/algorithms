#include <iostream>
#include <string>

using namespace std;
const int N = 10000;
int main(void) {
	int i,j, p , q, id[N];
	for (i =0; i<N; i++) {
		id[i] = i;
	}
	while (cin >>p >>q) {
		for (i=p; i!=id[i]; i=id[i]);
		for (j=q; j!=id[j]; j=id[j]);
		if (i == j) continue;
		id[i]=j;
		cout << " " << p << " " << q << endl;
	}
}
