//
//  main.cpp
//  Test Application for C++ STL Container data strcutreus and algorithms
//
//  Created by Chandan Kumar Mishra on 3/27/18.
//

#include <iostream>
#include "cpp_common.h"

int main(int argc, const char * argv[]) {
    //
    // insert code here...
    //
    
    //
    // STL data structures
    //
    std::cout << "################# TEST VECTOR ############################# " << std::endl;
    test_vector();
    
    std::cout << "################# TEST VECTOR COPY ######################## " << std::endl;
    test_vector_copy();
    
    std::cout << "################# TEST UNORDERED MAP ###################### " << std::endl;
    test_unordered_map();

    //
    // STL Algorithms
    //
    std::cout << "################# TEST BINARY SEARCH ###################### " << std::endl;
    test_binary_search();
    
    std::cout << "################# TEST SORT ############################### " << std::endl;
    test_sort();
    
    return 0;
}
