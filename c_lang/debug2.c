#include <stdio.h>

void swap( int x, int y )
{
	int temp;
	temp = x;
	x = y;
	y = temp;
}

int main()
{
	int a, b;
	a = 10;
	b = 30;
	printf("before swap: %d %d \n", a, b);
	swap(a, b);
	printf(" after swap: %d %d \n", a, b);
}
