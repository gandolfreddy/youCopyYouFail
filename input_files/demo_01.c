#include <stdio.h>
main()
{
	int i, n1 = 1, n2 = 1, N, k;
	printf("請輸入費氏數列到第幾項:");
	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		printf("%d\n", n1);
		k = n1 + n2;
		n1 = n2;
		n2 = k;
	}
	n1 = 1, n2 = 1;
	for (i = 0; k <= 1000; i++)
	{
		k = n1 + n2;
		n1 = n2;
		n2 = k;
	}
	printf("1000以內的費氏數列個數有%d個", i);
}