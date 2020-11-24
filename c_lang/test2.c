#include <stdio.h>

void multiple(int a)
{
	int i;
	for (i = 1; i < 0; i++)
	{
		printf("%d x %d = %d\n", a, i, a*i);
	}
}
