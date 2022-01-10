#include <stdio.h>
int main(void){
    unsigned long long x=1, stepX=2, y=1, stepY=3;
    int k = 0;
    for( ; ; ){
        if(x==y){
            k = k + 1;
            printf("%d: %llu\n", k, x);
        }
        else if(x>y){
            y = y + stepY;
            stepY = stepY + 2;
        }
		x = x + stepX++;
    }
    return 0;
}