//
//  main.cpp
//  cpp
//
//  Created by Chandan Kumar Mishra on 3/27/18.
//  Copyright © 2018 Juniper Networks Inc. All rights reserved.
//

#include <iostream>
#include "problems.h"

int main(int argc, const char * argv[]) {
    std::string nstr = "-1234";
    std::cout << string_to_integer("-13242") << std::endl;
    std::cout << integer_to_string(-24235) << std::endl;
    std::cout << integer_to_string(6435) << std::endl;

    return 0;
}
