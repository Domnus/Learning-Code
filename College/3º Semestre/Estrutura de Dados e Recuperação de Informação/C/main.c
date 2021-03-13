#include <stdio.h>

struct dados {
    char nome[30];
    int idade;
};

typedef struct dados PESSOA;

void leia(PESSOA  *v, int tam) {
    int i;
    for (i = 0; i < tam; i++) {
        printf("Nome: ");
        scanf("%s", &v[i].nome);
        printf("Idade: ");
        scanf("%d", &v[i].idade);
    }
}

void imprime(PESSOA *v, int tam) {
    int i;
    for (i = 0; i < tam; i++) {
        printf("Nome: %s\n", v[i].nome);
        printf("Idade: %d\n", v[i].idade);
    }
}

int maisVelho(PESSOA *v, int tam) {
    int p, idade = 0, mv = 0;
    int i;
    for (i = 0; i < tam; i++)  {
        if (v[i].idade > idade) {
            mv = i;
            idade = v[i].idade;
        }
    }
    return mv;
}

int main() {
    int pos, t = 5;
    PESSOA a[t];
    float notas[10];

    leia(a, t);
    imprime(a, t);

    pos = maisVelho(a, t);

    printf("Nome do mais velho: %s\n", a[pos].nome);
    printf("Idade do mais velho: %d", a[pos].idade);

    return 0;
}
