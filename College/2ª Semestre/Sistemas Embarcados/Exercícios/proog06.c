#include <stdio.h>

int main()
{
    int x = 1, y, w;
    y = 2;
    x = ++y;
    w = x++;
    y = 2*x++;
    printf("x = %d\n y = %d\n w = %d\n", x, y, w);
}
