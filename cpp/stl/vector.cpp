//
//  main.cpp
//  cpp
//
//  Created by Chandan Kumar Mishra on 3/27/18.
//

#include <iostream>
#include <vector>
#include "cpp_common.h"

using namespace std;

void test_vector()
{
    vector <int> g1;
    vector <int> ::iterator i;
    vector <int> ::reverse_iterator ri;

    //push_back, begin, end, iterator
    for (int i = 0; i < 5; i++) {
        g1.push_back(i * 10);
    }

    for (i = g1.begin(); i != g1.end(); i++) {
        cout << *i << '\t';
    } 
    cout << endl;

    for (ri = g1.rbegin(); ri != g1.rend(); ri++) {
        cout << *ri << '\t';
    }
    cout << endl;

    // size, capacity, max_size, empty
    cout << "Size : " << g1.size();
    cout << "\nCapacity : " << g1.capacity();
    cout << "\nMax_Size : " << g1.max_size();
    cout << "\nIsEmpty  : " << g1.empty();
    cout << endl;

    // front, back, at
    cout << "Reference operator [g] : g1[2] = " << g1[2];
    cout << endl;
    cout << "at : g1.at(4) = " << g1.at(4);
    cout << endl;
    cout << "front() : g1.front() = " << g1.front();
    cout << endl;
    cout << "back() : g1.back() = " << g1.back();
    cout << endl;

    //assign
    vector <int> g2;
    vector <int> g3;
    g1.assign(5, 10);   // 5 elements with value 10 each
 
    vector <int> :: iterator it;
    it = g1.begin() + 1;
 
    g2.assign(it, g1.end() - 1); // the 3 middle values of g1
 
    int gquiz[] = {1, 2};
    g3.assign(gquiz, gquiz + 2);   // assigning from array
 
    cout << "Size of g1: " << int(g1.size()) << '\n';
    cout << "Size of g2: " << int(g2.size()) << '\n';
    cout << "Size of g3: " << int(g3.size()) << '\n';

    cout << endl;

    //push_back, pop_back
    vector <int> g10;
    int sum = 0;
    g10.push_back(10);
    g10.push_back(20);
    g10.push_back(30);

    cout << "front " << g10.front() << " back "<< g10.back() << endl;
    while (!g10.empty())
    {
        sum += g10.back();
        g10.pop_back();
    }

    cout << "The sum of the elements of g10 is :  "
         << sum << endl;


    // back, front, data
    vector <int> g11;
    g11.push_back(10);
    g11.push_back(20);
    g11.push_back(30);

    int * tmp = g11.data();
    while (!g11.empty()) {
        cout << "back "<< g11.back() << endl;
        cout << "data " << tmp << " "<<*tmp << " "<< endl;
        g11.pop_back();
        tmp = tmp + 1;
    }

    //insert
    vector <int> g12(3, 10);
 
    it = g12.begin();
    it = g12.insert(it, 20);
    g12.insert(it, 2, 30);
    it = g12.begin();
 
    vector <int> gquiz2(2, 40);
    g12.insert(it + 2, gquiz2.begin(), gquiz2.end());
 
    int gq [] = {50, 60, 70};
    g12.insert(g12.begin(), gq, gq + 3);
 
    cout << "g12 contains : ";
    for (it = g12.begin(); it < g12.end(); it++)
        cout << *it << '\t';
    
    cout << endl;

    //delete - delete some elements
    vector <int> g13;

    for (int i = 1; i <= 10; i++)
        g13.push_back(i * 2);

    // erase the 5th element
    g13.erase(g13.begin() + 4);

    // erase the first 5 elements:
    g13.erase(g13.begin(), g13.begin() + 5);

    cout << "g13 contains :";
    for (int i = 0; i < g13.size(); ++i)
        cout << g13[i] << '\t';
    cout << endl;

    vector <int> g14;
    vector <int> g15;
    //vector <int> :: iterator i;
 
    g14.push_back(10);
    g14.push_back(20);
 
    g15.push_back(30);
    g15.push_back(40);
 
    cout << "Before Swapping, \n"
         <<"Contents of vector g14 : ";
 
    for (i = g14.begin(); i != g14.end(); ++i)
        cout << *i << '\t';
 
    cout << "\nContents of vector g15 : ";
    for (i = g15.begin(); i != g15.end(); ++i)
        cout << *i << '\t';
 
    swap(g14, g15);
 
    cout << "\n\nAfter Swapping, \n";
    cout << "Contents of vector g14 : ";
    for (i = g14.begin(); i != g14.end(); ++i)
        cout << *i << '\t';
 
    cout << "\nContents of vector g15 : ";
    for (i = g15.begin(); i != g15.end(); ++i)
        cout << *i << '\t';
 
    cout << "\n\nNow, we clear() and then add "
         << "an element 1000 to vector g14 : ";
    g14.clear();
    g14.push_back(1000);
    cout << g14.front();

    cout << endl;
    int gfg[] = {5,6,7,7,6,5,5,6};
     
    vector<int> v(gfg,gfg+8);    // 5 6 7 7 6 5 5 6
 
    sort (v.begin(), v.end());  // 5 5 5 6 6 6 7 7
 
    vector<int>::iterator lower,upper;
    lower = lower_bound (v.begin(), v.end(), 6); 
    upper = upper_bound (v.begin(), v.end(), 6); 
 
    cout << "lower_bound for 6 at position " << (lower - v.begin()) << '\n';
    cout << "upper_bound for 6 at position " << (upper - v.begin()) << '\n';
    cout << endl;

    vector<int> v1(gfg,gfg+8);    // 5 6 7 7 6 5 5 6
    sort(v1.begin(), v1.end());  // 5 5 5 6 6 6 7 7

    for (it=v1.begin(); it != v1.end(); it++){
        cout << " " << *it;
    }
    cout << endl;
    for (ri=v1.rbegin(); ri != v1.rend(); ri++){
        cout << " " << *ri;
    }
    cout << endl;
    while (!v1.empty()) {
        cout << " " << v1.back();
        v1.pop_back();
    }
    cout << endl << "isempty " << v1.empty() << endl;
}
