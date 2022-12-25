#include <stdio.h>

main()
{
    printf("(1)輸入n=");
    int i, n1 = 0, n2 = 1, N, k;
    scanf("%d", &N);
    printf("則第n項的費波納契數列的值為:(最後一數)\n");

    for (i = 0; i < N; i++)
    {
        printf("%d\n", n1);
        k = n1 + n2;
        n1 = n2;
        n2 = k;
    }

    printf("(2)1000以內，費波納契數列的個數共 17 個\n");
    int a = 0;
    int b = 1;
    int s = 0;
    printf("0,1,");

    while (1)
    {
        s = a + b;
        a = b;
        b = s;
        if (s <= 1000)
        {
            printf("%d,", s);
        }
        else
            break;
    }
}