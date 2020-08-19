#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

void cr()
{
  int x, y, m;
  int a, b = 0, i, j, k = 0;
  
  printf("Insira a range no formato [COMEÇO FIM] -> ");
  scanf("%d %d", &x, &y);
  y++;

  printf("Insira o M -> ");
  scanf("%d", &a);

  for (i = 0; i < a; i++)
  {
    for (j = x; j < y; j++)
    {
      if ((j - i) % a == 0)
      {
        b++;
      }
    }
  }
  
  int list[a][b];

  for (i = 0; i < a; i++)
  {
    k = 0;
    for (j = x; j < y; j++)
    {
      if ((j - i) % a == 0)
      {
        list[i][k] = j;
      }
      else
      {
        list[i][k] = 0;
      }
      
      k++;
    }
  }
  
  for (i = 0; i < a; i++)
  {
    printf("[%d]=", i);
    for (j = 0; j < b; j++)
    {
      if (list[i][j] == 0)
      {
        continue;
      }
      else
      {
        printf("[%d]", list[i][j]);
      }
    }
    printf("\n");
  }
}

void cong()
{
  int a, b, c, cong;

  printf("A ≡ B(MOD C)");

  printf("Insira os números no formato [A B C] -> ");
  scanf("%d %d %d", &a, &b, &c);

  cong = (a - b) % c;
  printf("%d ≡ %d (Mod %d) = %d", a, b, c, cong);

}
int main()
{
  char x[4];
  
  while (true)
  {
    printf("Modulo = Mod \n Divisor = Div \n Congruencia = Cong \n Classe de Residuo = Cr \n Se desejar encerrar digite CLOSE");
    scanf("%s", &x);

    int j = 0;
    char str[] = x;
    char ch;

    while (str[j]) 
    { 
        ch = str[j]; 
        putchar(toupper(ch)); 
        j++; 
    } 

    if (ch == "CR ")
    {
      cr();
    }

  }
}