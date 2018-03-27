//
//  main.cpp
//  Test Application for C++ STL Container data strcutreus and algorithms
//
//  Created by Chandan Kumar Mishra on 3/27/18.
//

#include <iostream>
#include "stl_common.h"

int main(int argc, const char * argv[]) {
    //
    // STL data structures
    //
    std::cout << "################# TEST VECTOR ############################# " << std::endl;
    test_vector();
    
    std::cout << "################# TEST VECTOR COPY ######################## " << std::endl;
    test_vector_copy();
    
    std::cout << "################# TEST UNORDERED MAP ###################### " << std::endl;
    test_unordered_map();

    std::cout << "################# TEST PAIR ############################### " << std::endl;
    test_pair();
    
    std::cout << "################# TEST QUEUE ############################### " << std::endl;
    test_queue();
    
    std::cout << "################# TEST STACK ############################### " << std::endl;
    test_stack();
    
    std::cout << "################# TEST TUPPLE ############################### " << std::endl;
    test_tupple();
    
    std::cout << "################# TEST MAP ############################### " << std::endl;
    test_map();
    
    //
    // STL Algorithms
    //
    std::cout << "################# TEST BINARY SEARCH ###################### " << std::endl;
    test_binary_search();
    
    std::cout << "################# TEST SORT ############################### " << std::endl;
    test_sort();
    
    return 0;
}
