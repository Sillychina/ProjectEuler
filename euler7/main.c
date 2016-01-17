#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

bool prime(int x) {
    for(int i = 2; i <= ceil(sqrt(x)); i++) {
        if(x%i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int counter = 1;
    int i = 2;
    for(; counter != 10001; i++) {
        if(prime(i)) {
            counter++;
        }
    }
    printf("%d\n", i);
    return 0;
}
