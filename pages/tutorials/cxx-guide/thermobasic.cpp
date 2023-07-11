#include "cantera/core.h"
#include <iostream>

int main(int argc, char** argv)
{
    // Create a new Solution object
    auto sol = Cantera::newSolution("h2o2.yaml", "ohmech", "None");
    auto gas = sol->thermo();

    std::cout << gas->temperature() << std::endl;
    return 0;
}
