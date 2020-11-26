#include <stdio.h>
#include <stdlib.h>
extern void multiple();

int main( int argc, char *argv[] )
{
	multiple( atoi(argv[1]) );
}
