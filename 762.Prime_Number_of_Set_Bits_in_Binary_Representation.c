#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int countSetBits(int number){
				int binaryLenght = sizeof(number) * 8;
				//int *output = (int*)malloc(binaryLenght); //those commented lines would create a regular int to binary function
				int counter = 0;

    for (int i = binaryLenght - 1; i >= 0 ; --i) {
        //output[i] = ((number & (1 << i)) != 0) ? 1 : 0; // Check if i-th bit is set
								if((number & (1 << i)) != 0) {
												counter += 1;
								}
    }

				//free(output);

    return counter;
}

int countSetBitsFaster(uint32_t number) {
    int counter = 0;

    while (number) {
        counter += number & 1;
        number >>= 1;
    }

    return counter;
}

int checkPrimeNumber(int number){
				if(number <= 1){
								return false;
				}
				for(int i = 2; i * i <= number; ++i){
								if(number % i == 0){
												return false;
								}
				}
				return true;
}

int countPrimeSetBits(int left, int right) {
				int prime_counter = 0;
				for(int i = left; i <= right; ++i){
								if(checkPrimeNumber(countSetBits(i))){
												prime_counter++;
								}
				}

				return prime_counter;
}

int main() {
				printf("%d", countPrimeSetBits(10, 15));
				return 0;

}

