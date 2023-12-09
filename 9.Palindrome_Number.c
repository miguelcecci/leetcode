#include <stdbool.h>
bool isPalindrome(int x) {
    if(x < 0){
        return false;
    }
    char as_str[12];

    sprintf(as_str, "%d", x);

    int string_total_size = 0;
    for(int i = 0; as_str[i] != '\0'; i++){
        string_total_size = i;
    }
    for(int i = 0; i < string_total_size; i++){
        if(as_str[i] != as_str[string_total_size - i]){
            return false;
        }
    }
    return true;
}
