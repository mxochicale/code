//nvcc -o hello_cudnn hello_cudnn.cu

#include<stdio.h>
#include<stdlib.h> 

#include <cudnn.h>


__global__ void print_from_gpu(void) {
	printf("Hello World! from thread [%d,%d] \
		From device\n", threadIdx.x,blockIdx.x); 
}

int main(void) { 
	printf("Hello World from host!\n"); 
	print_from_gpu<<<3,3>>>();
	cudaDeviceSynchronize();
return 0; 
}
