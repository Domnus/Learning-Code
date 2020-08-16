#include <stdio.h>

int main()
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