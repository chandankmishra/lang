#include <iostream>
#include <algorithm>
 
using namespace std;
 
void show(int a[], int arraysize)
{
    for(int i = 0; i < arraysize; ++i)
        cout << '\t' << a[i];
}
 
 
int main()
{
    int a[]= {1, 5, 8, 9, 6, 7, 3, 4, 2, 0};
    int asize = sizeof(a) / sizeof(a[0]);
    cout << "\n The array is : ";
    show(a, asize);
 
    cout << "\n\nLet's say we want to search for 2 in the array";
    cout << "\n So, we first sort the array";
    sort(a, a + 10);
    cout << "\n\n The array after sorting is : ";
    show(a, asize);

    if (binary_search(a, a + 10, 2)) 
       cout << "\nElement found in the array";
    else
       cout << "\nElement not found in the array";
 
     if (binary_search(a, a + 10, 10)) 
       cout << "\nElement found in the array";
    else
       cout << "\nElement not found in the array";
    cout << endl;

    return 0;
}
