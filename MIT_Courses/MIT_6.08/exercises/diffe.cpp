#include <iostream>
#include <string.h>
using namespace std;

void print_hello(){cout << "Hello World!" << "\n";}

void caesar_cipher(char* message_in, char* message_out, int shift, bool encrypt, int message_out_size){
    // clear message_out
    strcpy(message_out, "");

    if(encrypt == true){
        for(int idx=0; idx < message_out_size; idx++){
            // get the character in message_in and get its ascii index -> new ascii idx
            char curr_char = message_in[idx];
            int ascii_idx = (int) curr_char;
            int new_ascii_idx = (ascii_idx - 32) + shift;

            //if we reached null char, add it and return!
            if (curr_char == '\0' || idx == message_out_size - 1){
                message_out[idx] = '\0';
                return;
            }

            // mod new index as necessary
            if(new_ascii_idx >= 95){ new_ascii_idx = (new_ascii_idx%95 + 95)%95 + 32; }
            else{ new_ascii_idx += 32; }
            printf("%c: %d -> %c: %d\n", curr_char, ascii_idx, (char) new_ascii_idx, new_ascii_idx);

            // add new char to message_out
            message_out[idx] = (char) new_ascii_idx;
        }
    }

    else {  
        for(int idx=0; idx < message_out_size; idx++){
            // get the character in message_in and get its ascii index -> new ascii idx
            char curr_char = message_in[idx];
            int ascii_idx = (int) curr_char;
            int new_ascii_idx = (ascii_idx - 32) - shift;

            //if we reached null char, add it and return!
            if (curr_char == '\0' || idx == message_out_size - 1){
                message_out[idx] = '\0';
                return;
            }

            // mod new index as necessary
            if(new_ascii_idx < 0){ new_ascii_idx = (new_ascii_idx%95 + 95)%95 + 32; }
            else{ new_ascii_idx += 32; }
            printf("%c: %d -> %c: %d\n", curr_char, ascii_idx, (char) new_ascii_idx, new_ascii_idx);

            // add new char to message_out
            message_out[idx] = (char) new_ascii_idx;
        }
    }
}

void vigenere_cipher(char* message_in, char* message_out, char* keyword, bool encrypt, int message_out_size){
    // get length of keyword:
    int keyword_length = 0;
    int idx = 0;
    while(keyword[idx] != '\0'){
        keyword_length += 1;
        idx += 1;
    }

    int keyword_idx = 0;
    for(int idx=0; idx < message_out_size; idx++){
        char curr_char = message_in[idx];

        char shift_char = keyword[keyword_idx];
        int shift = (int) shift_char - 32;

        keyword_idx = (keyword_idx + 1)%keyword_length;


        //if we reached null char, add it and return!
        if (curr_char == '\0' || idx == message_out_size - 1){
            message_out[idx] = '\0';
            return;
        }

        char old_char[2];
        old_char[0] = curr_char;
        old_char[1] = '\0';

        // create a message out str to hold our one character
        char output[2] = "";
        caesar_cipher(old_char, output, shift, encrypt, 2);
        message_out[idx] = output[0];
    }
}

int modulo(int a, int b, int n){
    long long x=1, y=a; 
    while (b > 0) {
        if (b%2 == 1) {
            x = (x*y) % n; // multiplying with base
        }
        y = (y*y) % n; // squaring the base
        b /= 2;
    }
    return x % n;
}

char keyword_generate();

void dhke(int t,int p,int m,int b,char* message_in, char* message_out, bool encrypt, int out_buffer_size){
    int num_key = modulo(t, a, p);
    return vigenere_cipher(message_in, message_out, keyword_generate(num_key), encrypt, out_buffer_size);
}



int main(){
    char encrypted_message[] = "584*8&;e,<0@@C?5C_EX7G;KKNJ";
    char message[100] = "";
    char key[] = "super_secret";
    vigenere_cipher(encrypted_message,message,key,false,100);

    printf("%s", message);
}