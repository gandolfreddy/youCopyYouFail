#include <stdio.h>
main()
{
	/*第一題*/
	int n;
	printf("(1)找到第n項的費波納契數列的值 (假設第一項 = 1, 第二項 = 1)\n"
		   "   請輸入 n = ");
	scanf("%d", &n);
	int i, j, a = 1, b = 1;
	for (i = 3; i <= n; i++)
	{
		j = a + b;
		a = b;
		b = j;
	}
	printf("   第%d項 = %d\n", n, j);
	/*第二題*/
	int k, c = 1, d = 1;
	for (i = 1; k <= 1000; i++)
	{
		k = c + d;
		c = d;
		d = k;
	}
	printf("(2)1000以內，費波納契數列的個數 = %d", i);
}