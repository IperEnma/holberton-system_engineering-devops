#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
/**
 * infinite_while - infinite loop
 *
 * Return: void
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
 * main - function principal
 *
 * Return: void
 */
int main(void)
{
	int i = 0;
	pid_t child_pid;

	while (i < 5)
	{
		child_pid = fork();
		if (child_pid <= 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", child_pid);
		i++;
	}
	infinite_while();
	return (0);
}
