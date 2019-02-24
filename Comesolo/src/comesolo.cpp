#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

typedef vector<bool> array;
typedef vector<int> enteros;
const int n = 5;
int testing, count;
bool finished = false;

void init(array&);
int sigma(int);
int pos(int, int);
bool out_rng(int, int);
void brincar(int ini, int dest, int med, array &input, enteros &a);
//backtracking
bool es_solucion(int k);
void procesar_solucion(enteros a);
void crt_candts(enteros a, enteros &ini, enteros &dest, enteros &med, array input);
void backtrack(enteros &a, int k, array input);
void comesolo(array a);

int main()
{
    array a;
    init(a);
    comesolo(a);
    cout << count << " soluciones en la posicion deseada\n";
    return 0;
}

void comesolo(array input)
{
    cout << "Casilla vacia (i, j): ";
    int i, j;
    cin >> i; cin >> j;
    input[pos(i, j)] = false;
    cout << "Posicion a evaluar (i, j): ";
    cin >> i; cin >> j;
    testing = pos(i, j);
    count = 0;
    enteros a;
    backtrack(a, 0, input);
}

void init(array &input)
{
    input.resize(n * (n + 1) / 2);
    for(int i = 0; i < input.size(); i++)
        input[i] = true;
}

int sigma(int i)
{
    return i * (i + 1) / 2;
}

int pos(int i, int j)
{
    return sigma(i) + j;
}

bool out_rng(int suma)
{
    return suma < 0 || suma >= n;
}

void brincar(int ini, int dest, int med, array &input, enteros &a)
{
    input[ini] = !input[ini];
    input[med] = !input[med];
    input[dest] = !input[dest];
}

bool es_solucion(int k)
{
    //procesar_solucion(a);
    return k == sigma(n) - 2;
}

void procesar_solucion(enteros a)
{
    if(testing == a[a.size() - 1])
        count++;
    /*
    cout << "Solucion\n";
    int i = 0;
    while(i < a.size())
        cout << a[i++] << " -> " << a[i++] << endl;
    cout << endl << endl;
    cout << "Ultimo: " << a[a.size() - 1] << endl;
    finished = true;*/
}

void crt_candts(enteros a, enteros &ini, enteros &dest, enteros &med, array input)
{
    int xr, yr, dx;
    for(int y = 0; y < n; y++)
        for(int x = 0; x <= y; x++)
        {
            if(input[pos(y, x)] == false)
                continue;
            for(int i = -2; i <= 2; i += 2)
            {
                yr = y + i;
                if(out_rng(yr))
                    continue;
                for(int j = 0; j < 2; j++)
                {
                    i != 0 ? dx = i * j : dx = 2 * pow(-1, j);
                    xr = x + dx;
                    if(out_rng(xr) || xr > yr)
                        continue;
                    int
                        mx = x + dx/2,
                        my = y + i/2,
                        m = pos(my, mx),
                        d = pos(yr, xr);
                    //cout << "medio = " << m << endl;
                    if(!input[d] && input[m])
                    {
                        ini.push_back(pos(y, x));
                        med.push_back(m);
                        dest.push_back(d);
                    }
                }
            }
        }
        /*
    cout << "Candidatos\n";
    for(int i = 0; i < ini.size(); i++)
    {
        cout << ini[i] << " -> " << dest[i] << endl;
        cout << "con punto medio en: " << med[i] << endl << endl;
    }
    cout << endl;
    cin.get();*/
}

void backtrack(enteros &a, int k, array input)
{
    enteros inicios, destinos, medios;
    if(es_solucion(k))
        procesar_solucion(a);
    else
    {
        crt_candts(a, inicios, destinos, medios, input);
        k++;
        int c = inicios.size();
        for(int i = 0; i < c; i++)
        {
            brincar(inicios[i], destinos[i], medios[i], input, a);
            a.push_back(inicios[i]);
            a.push_back(destinos[i]);
            backtrack(a, k, input);
            if(finished)
                return;
            brincar(inicios[i], destinos[i], medios[i], input, a);
            a.pop_back();
            a.pop_back();
        }
    }
}
