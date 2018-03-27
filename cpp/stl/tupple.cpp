//
//  tupple.cpp
//  Test program to test the std::tupple class
//
//  Created by Chandan Kumar Mishra on 3/27/18.
//

#include<iostream>
#include<tuple>
#include "cpp_common.h"

using namespace std;
void test_tupple()
{
    // Declaring tuple
    tuple <char, int, float> geek;
 
    cout << "################# TEST TUPPLE ######################## " << std::endl;

    // Assigning values to tuple using make_tuple()
    geek = make_tuple('a', 10, 15.5);
 
    // Printing initial tuple values using get()
    cout << "The initial values of tuple are : ";
    cout << get<0>(geek) << " " << get<1>(geek);
    cout << " " << get<2>(geek) << endl;
 
    // Use of get() to change values of tuple
    get<0>(geek) = 'b';
    get<2>(geek) =  20.5;
 
     // Printing modified tuple values
    cout << "The modified values of tuple are : ";
    cout << get<0>(geek) << " " << get<1>(geek);
    cout << " " << get<2>(geek) << endl;
}
