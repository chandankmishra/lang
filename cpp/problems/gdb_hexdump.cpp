#include <iostream>

static void
print_hex_dump(char *arr, int len, int n)
{
    if (n >= len) return;
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (count % 8 == 0)
            std::cout << std::hex << static_cast<void *> (&arr[i]); 
        count++;
        std::cout << std::hex <<  "   0x" << int(arr[i]);
        if (count % 8 == 0)
            std::cout << std::endl;
    }
    std::cout << std::endl;
}

int main()
{
    char arr[] = "abcdefghijklmnopqrstuvqxyz";
    int n = 20;
    print_hex_dump(arr, sizeof(arr), n);
    return 0;
}
