#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
typedef vector<int> array;
typedef vector<bool> matriz;
int n, rows, cols, output;
bool finished = false;

bool es_solucion(array a, int k);
void procesar_solucion(array a, int k, matriz maze);
void crt_cand(array a, int k, matriz maze, array&);
void backtrack(array a, int k, matriz maze);
void laberinto(matriz maze);
void read_data(matriz &maze)
{
    char x;
    rows = 1; cols = 0;
    while((int)(x = getchar()) != EOF)
    {
        if(x == 10)
        {
            rows++;
            cols = 0;
            continue;
        }
        cols++;
        maze.push_back(x == '*');
    }
    n = maze.size();
}
int pos(int i, int j){return i*cols + j;}
void asign(int &pin, matriz maze, bool is_input)
{
    int i = 0, lim = rows, p;
    while(i++ < 2)
    {
        for(int i = 0; i < lim; i++)
        {
            if(lim == rows) //verticales
                p = (is_input ? pos(i, 0) : pos(i, cols - 1));
            else //horizontales
                p = (is_input ? pos(0, i) : pos(rows - 1, i));
            if(maze[p]) //si hay pared en el punto p, prueba en otro
                continue;
            pin = p;
            break;
        }
        lim = cols;
    }
}

int main()
{
    matriz maze;
    read_data(maze);
    laberinto(maze);
    return 0;
}

bool es_repetido(int new_p, array a, int k)
{
    for(int i = 0; i <= k; i++)
        if(a[i] == new_p)
            return true;
    return false;
}

void laberinto(matriz maze)
{
    //Obtener el pin de entrada y de salida
    int input;
    asign(input, maze, true);
    asign(output, maze, false);
    //cout << input << " " << output << endl;
    array a;
    a.push_back(input);
    backtrack(a, 0, maze);
}

void backtrack(array a, int k, matriz maze)
{
    if(es_solucion(a, k))
        procesar_solucion(a, k, maze);
    else
    {
        array cand;
        crt_cand(a, k++, maze, cand);
        for(int c : cand)
        {
            a.push_back(c);
            backtrack(a, k, maze);
            if(finished)
                return;
            a.pop_back();
        }
    }
}

bool es_solucion(array a, int k)
{
    return a[k] == output;
}

void procesar_solucion(array a, int k, matriz maze)
{
    //
    int p, x;
    for(int i = 0; i < rows; i++, cout << endl)
        for(int j = 0; j < cols; j++)
        {
            p = pos(i, j);
            if(es_repetido(p, a, k))
            {
                cout << "-";
                continue;
            }
            x = (maze[p] ? 219 : 32);
            //
        }
    cout << endl;
    finished = true;
}

void crt_cand(array a, int k, matriz maze, array &cand)
{
    int actual_p = a[k], new_p, i = 0, aux = cols;
    while(i++ < 2)
    {
        for(int x = -1; x <= 1; x += 2)
        {
            new_p = actual_p + x * aux;
            if(new_p < 0 || new_p >= n)
                continue;
            if(aux == 1 && new_p/cols != actual_p/cols)
                continue;
            if(maze[new_p] || es_repetido(new_p, a, k))
                continue;
            cand.push_back(new_p);
        }
        aux = 1;
    }
}