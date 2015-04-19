#include <stdio.h>
#include <iostream>

#include "src/drivers/GPUAdder.h"


int main(int argc, char **argv) {
	std::cout << "Teste GPU code: " << std::endl;

	int* values = new int[100];
	int* out = new int[100];
	for (int el = 0; el < 100; ++el) {
		values[el] = 2;
	}
	GPUAdder t(values,100);
	t.increment();
	t.retreive_to(out,100);

	for (int el = 0; el < 100; ++el) {
		std::cout <<  out[el] << std::endl;
	}

}
