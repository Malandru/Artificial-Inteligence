#include <stdio.h>
#include <stdlib.h>
#define MAXCAND 8
int n, fin, s;
int alfa[] = {-2 , -1, 1, 2},
    beta[] = {1, -1, 2, -2, 2, -2, 1, -1};

void imprimir(int *a, int size)
{
    for(int i = 0; i < size; i++)
    {
        if(i % n == 0)
            printf("\n");
        printf("%d\t", a[i]);
    }
    printf("\n");
}

void get(int *i, int *j, int index)
{
    *i = index / n;
    *j = index % n;
}

int pos(int i, int j)
{
    return i * n + j;
}

void recorre(int* a, int index, int k)
{
    if(k == fin)
    {
        printf("Solucion: %d", ++s);
        imprimir(a, n * n);
    }
    else
    {
        k++;
        int cand[MAXCAND], c = 0;
        int i, j, x, y;
        get(&i, &j, index);
        for(int p = 0; p < MAXCAND; p++)
        {
            x = i + alfa[p / 2];
            y = j + beta[p];
            if(0 <= x && x < n && y / n == j / n)
                if(a[(index = pos(x, y))] == -1)
                    cand[c++] = index;
        }
        for(i = 0; i < c; i++)
        {
            a[cand[i]] = k;
            recorre(a, cand[i], k);
            a[cand[i]] = -1;
        }
    }
}

int init()
{
    int i, j;
    printf("Fila: ");
    scanf("%d", &i);
    printf("Columna: ");
    scanf("%d", &j);
    return pos(i, j);
}

int main(int argc, char const *argv[])
{
    printf("Lado del tablero [n]: ");
    scanf("%d", &n);
    fin = n * n - 1;
    int *a = (int*)malloc(sizeof(int)*n);
    for(int i = 0; i < n * n; i++)
        a[i] = -1;
    printf("Posicion inicial\n");
    int index = init();
    a[index] = 0;
    recorre(a, index, 0);
    return 0;
}
