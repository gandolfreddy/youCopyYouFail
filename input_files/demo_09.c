#include <stdio.h>
main()
{
	int n, m, i, a1 = 0, a2 = 1, k;
	printf("輸入一個n並找到第n項的費波納契數列的值\n");
	printf("n= ");
	scanf("%d", &n);
	if (n == 1)
	{
		k = 1;
	}
	else
	{
		for (i = 1; i < n; i++)
		{
			k = a1 + a2;
			a1 = a2;
			a2 = k;
		}
	}
	printf("An= %d\n\n", k);

	a1 = 0, a2 = 1;
	printf("1000以內的費波納契數列的個數\n");
	for (i = 0; m <= 1000; i++)
	{
		m = a1 + a2;
		a1 = a2;
		a2 = m;
	}
	printf("共%d個", i);
}