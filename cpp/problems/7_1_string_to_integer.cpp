//
//  7_1 string_to_integer.cpp
//  problems
//
//  Created by Chandan Kumar Mishra on 4/4/18.
//

#include <stdio.h>
#include <iostream>
#include "problems.h"

int
string_to_integer (const std::string &nstr)
{
    auto sum = 0;
    auto is_negative = (nstr[0] == '-');
    int i = is_negative ?  1 : 0;
    for (; i < nstr.size(); i++) {
        sum = sum * 10 + nstr[i] - '0';
    }

    return is_negative ? -1 * sum : sum;
}

std::string
integer_to_string (int num)
{
    auto is_negative = false;
    if (num < 0) {
        is_negative = true;
        num = -num;
    }
    
    std::string nstr;
    while (num > 0) {
        nstr = std::to_string(num % 10) + nstr;
        num = num / 10;
    }
    
    return is_negative ? '-' + nstr : nstr;
}
