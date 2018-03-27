//
//  list.cpp
//  Test program to test the stl::list class
//
//  Created by Chandan Kumar Mishra on 3/27/18.
//

#include <iostream>
#include <list>
#include <iterator>
#include "stl_common.h"

using namespace std;

static void
print_list(list <int> l)
{
    list <int> ::iterator i;

    for (i = l.begin(); i != l.end(); i++)
    {
        cout << " " << *i;
    }
    cout << endl;
}

void test_list()
{
    list <int> l1;

    for (int i = 0; i < 5; i++) {
        l1.push_back(i*2);
        l1.push_front(10+i*3);
    }

    print_list(l1);

    list <int> l3(l1);
    print_list(l3);
    l3.sort();
    print_list(l3);

    list <int> l2(l3);
    l2.reverse();
    print_list(l2);

    cout << "size "<< l2.size() << " front " << l2.front() << " back " << l2.back(); 
    cout << endl;
}
