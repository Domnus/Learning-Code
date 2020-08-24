#include <stdio.h>

int main()
{
    int dia, mes, ano;

    printf("Digite a data: ");
    scanf("%d/%d/%d", &dia, &mes, &ano);

    printf("%d/%d/%d", dia, mes, ano);
}