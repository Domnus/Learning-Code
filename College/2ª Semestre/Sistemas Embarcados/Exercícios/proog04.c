#include <stdio.h>

int main()
{
    int x = 1, y = 2;
    x++;
    --y;
    y = x+y;
    printf("x = %d\n y = %d\n", x, y);
}
