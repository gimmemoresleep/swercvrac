#include <stdio.h>
#include <readline/readline.h>
#include <readline/history.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
	int width = atoi(readline("width : "));
	int n = atoi(readline("N : "));
	int piece[n][2];
	for(int i = 0; i < n; i++){
		char format[50];
		sprintf(format, "width - length of %d : ", i);
		char *line = readline(format);
		piece[i][0] = atoi(strtok(line, " "));
		piece[i][1] = atoi(strtok(NULL, " "));
	}
	int piece_sum = 0;
	for(int i = 0; i < n; i++){
		piece_sum += (piece[i][0] * piece[i][1]);
	}

	int length = piece_sum/width;
	printf("%d", length);
	return 0;
}
