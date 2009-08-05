#include <stdio.h>

template< typename T >
struct is_field {
    static const bool value = false;
};

template<>
struct is_field<Complex> {
    static const bool value = true;
}



int main(){
    return 0;
}
