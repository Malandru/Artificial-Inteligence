#include <my_vector.h>
using namespace std;

double longitud(double *vector, int D)
{
    double suma = 0;
    for(int i = 0; i < D; i++)
        suma += pow(vector[i], 2);
    return sqrt(suma);
}

void mk_unit(double *vector, int D)
{
    double norma = longitud(vector, D);
    for(int i = 0; i < D; i++)
        vector[i] /= norma;
}

double component(double *a, double *b, int D)
{
    //Proyeccion escalar de b sobre a.
    double prod = 0; //Producto punto
    for(int i = 0; i < D; i++)
        prod += a[i] * b[i];
    return prod / longitud(a, D);
}

void print(double *vector, int D)
{
    for(int i = 0; i < D; i++)
        cout << vector[i] << " ";
    cout << endl;
}