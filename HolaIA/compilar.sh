g++ -c src/my_vector.cpp -I lib -o obj/my_vector.o
g++ -c src/neurona.cpp -I lib -o obj/neurona.o
g++ -c src/lectura.cpp -I lib -o obj/lectura.o
g++ obj/neurona.o obj/my_vector.o obj/lectura.o -o bin/neurona
