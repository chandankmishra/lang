//
//  map.cpp
//  Test program to test the std::map class
//
//  Created by Chandan Kumar Mishra on 3/27/18.
//

#include <iostream>
#include <map>
#include <iterator>
#include "cpp_common.h"
 
using namespace std;

static void
print_map (map <int, int> m)
{
    map <int, int> :: iterator itr;

    cout << "\tKEY\tVALUE\n";
    for (itr = m.begin(); itr != m.end(); ++itr)
    {
        cout  <<  '\t' << itr->first 
              <<  '\t' << itr->second << '\n';
    }
    cout << endl;
} 

void test_map()
{
    map <int, int> gquiz1;        // empty map container
     
    // insert elements in random order
    gquiz1.insert(pair <int, int> (4, 20));
    gquiz1[4] = 400;
    gquiz1[5] = 500;
    gquiz1[6] = 600;
    gquiz1[7] = 700;
    gquiz1[8] = 800;
    gquiz1[9] = 900;
    gquiz1[3] = 300;
 
    // printing map gquiz1
    map <int, int> :: iterator itr;
    cout << "\nThe map gquiz1 is : \n";
    print_map(gquiz1);
 
    // assigning the elements from gquiz1 to gquiz2
    map <int, int> gquiz2(gquiz1.begin(), gquiz1.end());
    cout << "\nThe map gquiz2 after assign from gquiz1 is : \n";
    print_map(gquiz2);
 
    // remove all elements up to element with key=3 in gquiz2
    cout << "\ngquiz2 after removal of elements less than key=3 : \n";
    gquiz2.erase(gquiz2.begin(), gquiz2.find(3));
    print_map(gquiz2);
 
    // remove all elements with key = 4
    int num;
    num = gquiz2.erase (4);
    cout << "\ngquiz2.erase(4) : " << num << " removed \n" ;
    print_map(gquiz2);
 
    //lower bound and upper bound for map gquiz1 key = 5
    cout << "gquiz1.lower_bound(5) : " << "\tKEY = ";
    cout << gquiz1.lower_bound(5)->first << '\t';
    cout << "\tELEMENT = " << gquiz1.lower_bound(5)->second << endl;
    cout << "gquiz1.upper_bound(5) : " << "\tKEY = ";
    cout << gquiz1.upper_bound(5)->first << '\t';
    cout << "\tELEMENT = " << gquiz1.upper_bound(5)->second << endl;
    cout << endl;
     
    
    //use pair as a key
    cout << "use pair as map key " << endl;
    map<pair<int, int>, int> vis;
    vis[make_pair(0,0)] = 10;
    vis[make_pair(0,1)] = 20;
    vis[make_pair(1,2)] = 30;
    vis[make_pair(2,2)] = 40;
    for (int i =0; i < 3; i++) {
        for (int j =0; j < 3; j++) {
            if (vis.find(make_pair(i,j)) != vis.end())  {
                cout << "key (" << i << ", " << j << ") ";
                cout << "value "<<vis[make_pair(i,j)] << endl;
            }
        }
    }
    cout << endl;

    // use greater <int> argument to keep the map sorted in reverse order
    cout << "use greater <int> to print map in reverse order " << endl;
    map<int, string, greater <int> > mymap;
    mymap.insert(make_pair(10, "queen"));
    mymap.insert(make_pair(20, "rose"));
    mymap.insert(make_pair(5," lion"));
    for (auto it=mymap.begin() ; it!=mymap.end() ; it++)
        cout << "(" << (*it).first << ", "
            << (*it).second << ")" << endl; 
    cout << endl;
}
