//
//  vector_copy.cpp
//  Test program to test the std::vector class copy functionality
//
//  Created by Chandan Kumar Mishra on 3/27/18.
//

#include <iostream>
#include <vector>
#include "cpp_common.h"

using namespace std;

static void
print_vector(vector <int> v)
{
    vector <int> ::iterator i;

    for (i = v.begin(); i != v.end(); i++) {
        cout << " " << *i;
    }
    cout << endl;
}

void test_vector_copy()
{
    vector <int> g1;
    vector <int> g2;
    vector <int> g3;
    vector <int> ::iterator i;
    vector <int> ::reverse_iterator ri;
   
    cout << "################# TEST VECTOR COPY ######################## " << std::endl;

    for (int j = 0; j < 5; j++) {
        g1.push_back(j);
    } 

    // vector copy by iterative assignment
    for (i = g1.begin(); i != g1.end(); i++) {
        cout << " " << *i;
        g2.push_back(*i);
    }   
    cout << endl;

    g2[2] = 100;
    print_vector(g2);

    // vector copy by assignment
    g3 = g2;
    g3[2] = 200;
    print_vector(g3);

    // vector copy by passing vector in constructor
    vector<int> g4(g3);
    g4[2] = 300;
    print_vector(g4);

    // vector copy by using copy() function
    vector<int> g5;
    copy(g4.begin(), g4.end(), back_inserter(g5));
    g5[2] = 400;
    print_vector(g5);

    // vector copy using assign() function
    vector<int> g6;
    g6.assign(g4.begin(), g4.end());
    g6[2] = 500;
    print_vector(g6);

    //two more methods
    //v2.insert(v2.begin(), v1.begin(), v1.end());
    //vector<int>v2(v1.begin(),v1.end());
}
