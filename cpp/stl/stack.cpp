//
//  stack.cpp
//  Test program to test the std::tupple class
//
//  Created by Chandan Kumar Mishra on 3/27/18.
//

#include <iostream>
#include <stack>
#include "cpp_common.h"

using namespace std;

static void showstack(stack <int> gq)
{
    stack <int> g = gq;
    while (!g.empty())
    {
        cout << '\t' << g.top();
        g.pop();
    }
    cout << '\n';
}

void test_stack ()
{
    stack <int> gquiz;
    gquiz.push(10);
    gquiz.push(30);
    gquiz.push(20);
    gquiz.push(5);
    gquiz.push(1);

    cout << "The stack gquiz is : ";
    showstack(gquiz);

    cout << "\ngquiz.size() : " << gquiz.size();
    cout << "\ngquiz.top() : " << gquiz.top();


    cout << "\ngquiz.pop() : ";
    gquiz.pop();
    showstack(gquiz);
}
