#include <iostream>

class Singleton
{
    private:
        /* Here will be the instance stored. */
        static Singleton* instance;

        /* Private constructor to prevent instancing. */
        Singleton();

    public:
        /* Static access method. */
        static Singleton* getInstance();
        int count;
        void hello() {
            std::cout << "hello" << std::endl;
        }
};

