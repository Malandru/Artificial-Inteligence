#include <iostream>
#include <my_vector.h>
#define SIN_CLASIFICACION -1
using namespace std;

typedef double number;
number **E; //Vector de 'vectores estandar' o vector de 'vectores de pesos'
number *x; //Vector de entrada o vector a clasificar
int N, D; //Numero de tipos, Dimensiones

void init_estandar();
int ejemplos();
void leer(int M, int T); //Leer M ejemplos para el tipo T
void clasificar(int K); //Clasificar K ejemplos

int main()
{
    init_estandar();
    for(int tipo = 0; tipo < N; tipo++)
        leer(ejemplos(), tipo);
    clasificar(ejemplos());
    return 0;
}

void init_estandar()
{
    cin >> N;
    cin >> D;
    E = new number*[N];
    x = new number[D];
    for(int i = 0; i < N; i++)
    {
        E[i] = new number[D];
        for(int j = 0; j < D; j++)
            E[i][j] = 0;
    }
}

int ejemplos()
{
    int M;
    cin >> M;
    return M;
}

void leer(int M, int T)
{
    number comp;
    for(int i = 0; i < M; i++)
        for(int d = 0; d < D; d++)
        {
            cin >> comp;
            E[T][d] += comp;
        }
}

void clasificar(int K)
{
    for(int tipo = 0; tipo < N; tipo++)
        mk_unit(E[tipo], D);
    for(int caso = 0; caso < K; caso++)
    {
        for(int d = 0; d < D; d++)
            cin >> x[d];
        mk_unit(x, D);
        int TIPO = SIN_CLASIFICACION;
        number max = 0;
        for(int tipo = 0; tipo < N; tipo++)
        {
            number comp = component(E[tipo], x, D);
            if(comp > max)
            {
                max = comp;
                TIPO = tipo + 1;
            }
        }
        cout << "Caso " << caso + 1 << " es tipo " << TIPO << endl;
    }
}