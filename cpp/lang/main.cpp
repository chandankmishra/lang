#include <iostream>
#include "singleton.h"

int main()
{
    //new Singleton(); // Won't work
    Singleton* s = Singleton::getInstance(); // Ok
    Singleton* r = Singleton::getInstance();

    /* The addresses will be the same. */
    std::cout << s << std::endl;
    std::cout << r << std::endl;

    s->hello();
    std::cout << s->count << std::endl;
    
    auto i = 6;
    std::cout << std::bitset<32>(1 << i) << std::endl;
    auto x =(1 << i)-1;
    std::cout << std::bitset<32>(~x) << std::endl;
    
    //
    // Right propate the rightmost bit
    //
    x = 80; //b'1010000
    auto y = x | (x & ~(x-1)) - 1 ;
    std::cout << x << " " << std::bitset<32>(x) << std::endl;
    std::cout << y << " " << std::bitset<32>(y) << std::endl;
    
    //
    // Computer X modulus power of 2 e.g. 77 returns 13 (= 77 % 64)
    //
    x = 77;
    auto power = 6;
    y = x & (1 << power) -1;
    std::cout << x << " " << std::bitset<32>(x) << std::endl;
    std::cout << y << " " << std::bitset<32>(y) << std::endl;
    
    //
    // Compute if x is power of 2 return true for 1,2,4,8,16 etc.
    //
    x = 1;
    auto res = (x & (x -1)) > 0 ? "no" : "yes";
    std::cout << x << " " << res << std::endl;
    x = 2;
    res = (x & (x -1)) > 0 ? "no" : "yes";
    std::cout << x << " " << res << std::endl;
    x = 3;
    res = (x & (x -1)) > 0 ? "no" : "yes";
    std::cout << x << " " << res << std::endl;
    x = 4;
    res = (x & (x -1)) > 0 ? "no" : "yes";
    std::cout << x << " " << res << std::endl;
    x = 5;
    res = (x & (x -1)) > 0 ? "no" : "yes";
    std::cout << x << " " << res << std::endl;
    x = 6;
    res = (x & (x -1)) > 0 ? "no" : "yes";
    std::cout << x << " " << res << std::endl;
    x = 7;
    res = (x & (x -1)) > 0 ? "no" : "yes";
    std::cout << x << " " << res << std::endl;
    x = 8;
    res = (x & (x -1)) > 0 ? "no" : "yes";
    std::cout << x << " " << res << std::endl;
}
