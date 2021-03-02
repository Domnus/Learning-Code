#include <stdio.h>

int main(){
	int idade;
	int soma = 0;
	int cont = 0;

	do {
		printf("Digite a idade: ");
		scanf("%d", &idade);
		if (idade < 0) {
			break;
		}
		soma += idade;
		cont++;
	} while (idade > 0);

	printf("Média das idades: %f", (soma/(float)cont));
				
	return 0;
}
