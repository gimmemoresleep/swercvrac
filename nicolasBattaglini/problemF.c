#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[]) {
	char *buf;
	size_t num = 0;

	getline(&buf, &num, stdin);
	int width = atoi(buf);

	getline(&buf, &num, stdin);
	int n = atoi(buf);

	int res = 0;
	for (int i = 0; i < n; i++) {
		buf = NULL;
		getline(&buf, &num, stdin);
		int wi = atoi(strtok(buf, " "));
		int li = atoi(strtok(NULL, " "));
		res += (wi * li);
	}
	
	free(buf);

	int length = res / width;
	printf("%d\n", length);
	return 0;
}
