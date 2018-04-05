#include <iostream>
#include "singleton.h"

/* Null, because instance will be initialized on demand. */
Singleton* Singleton::instance = 0;

Singleton* Singleton::getInstance()
{
    if (instance == 0)
    {
        instance = new Singleton();
    }

    return instance;
}

Singleton::Singleton()
{
    count = 100;
}
