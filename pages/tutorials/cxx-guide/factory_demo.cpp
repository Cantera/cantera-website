#include "cantera/base/Solution.h"
#include "cantera/thermo.h"
#include "cantera/kinetics.h"
#include "cantera/transport.h"

using namespace Cantera;

// The actual code is put into a function that can be called from the main program.
void simple_demo2()
{
    // Create a new 'Solution' object that provides access to ThermoPhase, Kinetics and
    // Transport objects.
    auto sol = newSolution("gri30.yaml", "gri30");

    // Access the ThermoPhase object. Based on the phase definition in the input file,
    // this will reference an IdealGasPhase object.
    auto gas = sol->thermo();

    // Access the Kinetics object. Based on the phase definition in the input file,
    // this will reference a GasKinetics object.
    auto kin = sol->kinetics();

    // Set an "interesting" state where we will observe non-zero reaction rates.
    gas->setState_TPX(500.0, 2.0*OneAtm, "CH4:1.0, O2:1.0, N2:3.76");
    gas->equilibrate("HP");
    gas->setState_TP(gas->temperature() - 100, gas->pressure());

    // Get the net reaction rates.
    vector_fp wdot(kin->nReactions());
    kin->getNetRatesOfProgress(wdot.data());

    writelog("Net reaction rates for reactions involving CO2\n");
    size_t kCO2 = gas->speciesIndex("CO2");
    for (size_t i = 0; i < kin->nReactions(); i++) {
        if (kin->reactantStoichCoeff(kCO2, i) || kin->productStoichCoeff(kCO2, i)) {
            writelog("{:3d}  {:30s}  {: .8e}\n", i, kin->reactionString(i), wdot[i]);
        }
    }
    writelog("\n");

    // Access the Transport object. Based on the phase definition in the input file,
    // this will reference a MixTransport object.
    auto trans = sol->transport();
    writelog("T        viscosity     thermal conductivity\n");
    writelog("------   -----------   --------------------\n");
    for (size_t n = 0; n < 5; n++) {
        double T = 300 + 100 * n;
        gas->setState_TP(T, gas->pressure());
        writelog("{:.1f}    {:.4e}    {:.4e}\n",
            T, trans->viscosity(), trans->thermalConductivity());
    }
}

// the main program just calls function simple_demo2 within a 'try' block, and
// catches exceptions that might be thrown
int main()
{
    try {
        simple_demo2();
    } catch (std::exception& err) {
        std::cout << err.what() << std::endl;
    }
}

