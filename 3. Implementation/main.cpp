#include <iostream>
#include "Calculator.h"

using namespace std;

int main(){

    int r;
    Calculator c01;

    r = c01.add();
    cout << r;

    r = c01.substract();
    cout << r;

    r = c01.multiply();
    cout << r;

    r = c01.divide();
    cout << r;

    return 0;
}