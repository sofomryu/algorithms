#include <iostream>

using namespace std;
int main() {
	int a =3;
	int* ptr = &a;
	int** pop= &ptr;

	cout << ptr <<"and " << pop<< endl;
	cout << *ptr << "and " << *pop <<endl;
}
