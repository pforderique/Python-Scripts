#include <iostream>
#include <string.h>
using namespace std;

int main(){

    uint16_t data[100] = {1650, 1411, 1617, 1473};

    char data_string[300] = {0};
    for (int i=0;i<4;i++) {
        sprintf(data_string+strlen(data_string),"%d,",data[i]);
    }

    char post_body[150] = {0};
    sprintf(post_body,"kerb=Piero&MAC=16&thedata=%s", data_string);

    printf("%s", post_body);
}