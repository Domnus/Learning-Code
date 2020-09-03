#include <stdio.h>
#include <math.h>

int main(void)
{
    int n1, n2;
    printf("Digite um número: ");
    scanf("%d", &n1);

    n2 = pow(n1, 2);

    printf("%d ao quadrado é igual a %d.\n", n1, n2);
    
}