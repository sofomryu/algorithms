#include <iostream>
using namespace std;
int fibnum;
int N;
int fib(int a, int b, int n);
int main(void) {
	cin >> N;
	fib(0,1,N);	
	return 0;

}

int fib(int a, int b, int n) {
	fibnum = a+b;
	
	cout<< fibnum << endl;	
	
	if (fibnum >n) {
		return  0;
	}	
	fib(b,fibnum, n);

	return 0;
}
