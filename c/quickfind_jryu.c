#include <stdio.h>


int main(void) {
	int pairs[][2] = {{3,4},{4,9},{8,0},{2,3},{5,6},{2,9},{5,9},{7,3},{4,8},{5,6},{0,2},{6,1}};
	int row = sizeof(pairs)/sizeof(pairs[0]);
	int col = sizeof(pairs[0])/sizeof(pairs[0][0]);
	printf("row: %ix col: %i matrix",row,col);
}
