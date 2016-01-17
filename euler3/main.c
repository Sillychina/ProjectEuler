#include <stdio.h>
#include <stdlib.h>

int main() {
    long long int num = 600851475143;
    long long int largestFact = 0;
    while (num != 1){
        for(long long int i = 2; i <= num; i++){
            if(num %i == 0){
                num /= i;
                if(i > largestFact){
                    largestFact = i;
                }
                break;
            }
        }
    }
    printf("%lli", largestFact);
    return 0;
}
