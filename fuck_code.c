#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX_PUSSY_SIZE 12
#define MULTIPLE_PUSSY
#define NO_GIRLFRIEND NULL

void *remove_condom(char *manforce)
{
	printf("\nFUCK OFF, YOU DONT HAVE CONDOM TO REMOVE\n");
	return NULL;
}

int main()
{
	pthread_t dick;
	char *all_tits = malloc(MAX_PUSSY_SIZE*sizeof(char));
	*(all_tits+0) = 'H';
	*(all_tits+1) = 'E';
	*(all_tits+2) = 'L';
	*(all_tits+3) = 'L';
	*(all_tits+4) = 'O';
	*(all_tits+5) = ' ';
	*(all_tits+6) = 'W';
	*(all_tits+7) = 'O';
	*(all_tits+8) = 'R';
	*(all_tits+9) = 'L';
	*(all_tits+10) = 'D';
	for(int i=0;i<MAX_PUSSY_SIZE;i++)
	{
		printf("%c ",*(all_tits+i));
	}
	pthread_create(&dick,NO_GIRLFRIEND,&remove_condom,NO_GIRLFRIEND);
	pthread_join(&dick,NO_GIRLFRIEND);
	pthread_exit(&dick);
	return 0;
}