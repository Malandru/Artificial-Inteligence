#include <my_vector.h>
#include <lectura.h>
#define N 5 //Neuronas
using namespace std;

double x[T] = {2, 0, 4}; //Vector de T entradas (h, v, d)
double w[N][T]; //= {}; //Vector de N neuronas, cada una con T pesos

void init();

//Metodos para procesar vectores
void mk_unit();

int main()
{
    init();
    mk_unit();
    //Imprimir
    double comp;
    for(int neurona = 0; neurona < N; neurona++)
    {
        comp = component(w[neurona], x);
        cout << comp << endl;
    }
    return 0;
}

void init()
{
    for(int i = 0; i < N; i++)
        for(int j = 0; j < T; j++)
            cin >> w[i][j];
    analizar(x);
}

void mk_unit()
{
    mk_unit(x);
    for(int i = 0; i < N; i++)
        mk_unit(w[i]);
}

