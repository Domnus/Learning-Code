#include <stdio.h>
#include <string.h>

int main()
{
    char frase[100];

    printf("Digite uma frase: ");
    scanf("%s", &frase);

    strrev(frase);

    printf("Frase invertida: %s.\n", frase);

    return 0;
}