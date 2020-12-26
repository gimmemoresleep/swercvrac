#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[]) {
	int n;
	scanf("%d\n", &n);
	char a[n*2], b[n*2];
	fgets(a, (n*2)+1, stdin);
	fgets(b, n*2, stdin);
	int a_tab[n], b_tab[n], res_tab[3];
	memset(a_tab, 0, n);
	memset(b_tab, 0, n);
	memset(res_tab, 0, 3);
	char *token = strtok(a, " ");
	int i, j;
	for(i = 0; i < n; i++){
		a_tab[i] = atoi(token);
		token = strtok(NULL, " ");
	}
	token = strtok(b, " ");
	for(i = 0; i < n; i++){
		b_tab[i] = atoi(token);
		token = strtok(NULL, " ");
	}

	for(i = 0; i < n; i++){
		for (j = 0; j < n; j++){
			res_tab[(i+j)%3] += a_tab[i]*b_tab[j];
		}
	}
	printf("%d %d %d", res_tab[1], res_tab[2], res_tab[0]);
	return 0;
}
