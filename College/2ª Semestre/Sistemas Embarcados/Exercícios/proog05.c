#include <stdio.h>

int main()
{
    int x = 1, y;
    x++;
    y = 2 + (++x);
    printf("x = %d\n y = %d\n", x, y);
}
