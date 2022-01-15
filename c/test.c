#include <stdio.h>
#include <string.h>

int main() {

	char s[] = "Hello";
	int b = sizeof(s);
	printf("%i",b);
	for (int i=0; i<b; i++) {
		printf("%c",s[i]);
	}
	printf("5th: %c",s[5]);
	int len = strlen(s);
	printf("length is : %c",s[0]);
	if (0) {
		printf("true");
	} else {
		printf("false");
	}
}
