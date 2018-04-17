///
///Implement a UNIX TAIL command
///
#include <iostream>
#include <fstream>
using namespace std;

std::string tail(std::string file_name, int n)
{
    fstream file_ptr(file_name.c_str());
    file_ptr.seekg(0, file_ptr.end);
    int file_size = file_ptr.tellg(), newline_cnt = 0;
    std::cout << "file size: " << file_size  << " # of line: " << n <<  std::endl;

    string last_n_lines;
    for (int i = 0; i < file_size; i++) {
        file_ptr.seekg(-1 -i, file_ptr.end);
        char c;
        file_ptr.get(c);
        if (c == '\n') newline_cnt++;
        if (newline_cnt >= n) break;
        last_n_lines.push_back(c);
    }
    reverse(last_n_lines.begin(), last_n_lines.end());
    return last_n_lines;
}
int main()
{
    std::cout << tail("7_13_tail.cpp", 10) << std::endl;
    return 0;
}
