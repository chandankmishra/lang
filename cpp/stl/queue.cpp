//
//  queue.cpp
//  Test program to test the stl::queue class
//
//  Created by Chandan Kumar Mishra on 3/27/18.
//

#include <iostream>
#include <queue>
#include "cpp_common.h"
 
using namespace std;
 
static void showq(queue <int> gq)
{
    queue <int> g = gq;
    while (!g.empty())
    {
        cout << '\t' << g.front();
        g.pop();
    }
    cout << '\n';
}
 
void test_queue()
{
    queue <int> gquiz;

    gquiz.push(10);
    gquiz.push(20);

    cout << "The queue gquiz is : ";
    showq(gquiz);
 
    cout << "\ngquiz.size() : " << gquiz.size();
    cout << "\ngquiz.front() : " << gquiz.front();
    cout << "\ngquiz.back() : " << gquiz.back();
 
    cout << "\ngquiz.pop() : ";
    gquiz.pop();
    showq(gquiz);
}
