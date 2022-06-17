#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
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
	sleep(100);
	return (0);
}
