graficas.png: euler_001.dat euler_01.dat euler_1.dat implicit_001.dat implicit_01.dat implicit_1.dat
	python CarlosCordoba_Ejercicio25.py
    
all: euler_001.dat euler_01.dat euler_1.dat implicit_001.dat implicit_01.dat implicit_1.dat

%.dat: datos.x
	./datos.x
    
datos.x: CarlosCordoba_Ejercicio25.cpp
	g++ CarlosCordoba_Ejercicio25.cpp -o datos.x