#include <stdio.h>
int main()
{
    int a = 1, b = 1, c = a + b, e, f, g = 1, h = 1, i = g + h, j = i, k;
    printf("請輸入大於3的值\n");
    scanf("%d", &f);
    for (e = 3; e < f; e++)
    {
        a = b;
        b = c;
        c = a + b;
    }
    printf("%d\n", c);
    printf("1000以內，費波納契數列的個數\n");
    for (k = 3; j < 1000; k++)
    {
        g = h;
        h = i;
        i = g + h;
        j = i;
    }
    printf("%d", k - 1);
}