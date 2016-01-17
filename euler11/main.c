#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *input = fopen("euler11text.txt", "r");
    if (input == NULL) {
        perror("Error: File not found\n");
    }
    int inputNums[20][20];
    for(int i = 0; i < 20; i++) {
        for(int j = 0; j < 20; j++) {
            fscanf(input, "%d", &inputNums[i][j]);
            printf("%d \n", inputNums[i][j]);
        }
    }
    return 0;
}
