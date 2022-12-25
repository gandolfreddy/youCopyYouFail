#include <stdio.h>
main()
{
    int i, a = 1, b = 1, N, k;
    printf("請輸入費氏數列到第幾項:");
    scanf("%d", &N);
    for (i = 0; i < N; i++)
    {
        printf("%d\n", a);
        k = a + b;
        a = b;
        b = k;
    }
    a = 1, b = 1, k = 1;
    for (i = 0; k <= 1000; i++)
    {
        k = a + b;
        a = b;
        b = k;
    }
    printf("1000以內的費氏數列個數有%d個", i);
}