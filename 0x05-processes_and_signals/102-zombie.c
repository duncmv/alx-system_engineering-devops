#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
/**
 * infinite_while - loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - main
 * Return: 0
 */
int main(void)
{
	int i = 0;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie == 0)
		{
			exit(0);
		}
		printf("Zombie process created, PID: %u\n", zombie);
	}
	infinite_while();
	return (0);
}
