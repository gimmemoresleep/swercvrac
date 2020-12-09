#include <stdio.h>

int main()
{
	int w, h, area = 0;
	int n, W;

	scanf("%d", &W);
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d %d", &w, &h);
		area += w * h;
	}
	printf("%d", area / W);
	return (0);
}