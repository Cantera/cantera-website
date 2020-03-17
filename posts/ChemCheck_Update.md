---
title: GSoC 2019 Fourth Blog
date: 2020-03-16 14:50 UTC-18:50
slug: GSoC_2019_Fourth_Blog
tags: GSoC 2019
description: 2019 Google Summer of Code Cantera Project Blog
type: text
author: Chao Xu
---

# Update of ChemCheck

## Abstract
[ChemCheck](https://github.com/comocheng/ChemCheck/tree/cx) is a web application for users to visualize the syntax error during conversion of  chemkin files to yaml format (input file for cantera 2.5.0) and the chemical error in the model.
The introduction has been posted on https://cantera.org/blog/GSoC_2019_Project_Introduction.html

## Description
Except the work being done during two months in GSOC 2019(https://cantera.org/blog/GSoC_2019_Project_First_Evaluation.html, https://cantera.org/blog/GSoC_2019_Third_Blog.html,https://cantera.org/blog/GSoC_2019_Fourth_Blog.html), more works get done in past 2 months. 
1. Test Suite
   - Unit tests and the integration test for ChemCheck has been done. The integration test is achieved by travis CI. More tests will be added with the project developing.
2. Syntax Error diagnosis and visualization:
   - After checking some models, the most common error we found is missing index number or index number not being aligned correctly at the end of line in the thermo file or the thermo block in a chemkin file. Cantera throws logging information:`INFO:root:Error while reading thermo entry starting on line (line_number):`  and stops conversion when the “missing index number” error happens. In this case, ChemCheck will check the index number at the end of each line for the thermo data of the error species and make the suggestion to fix it. Here is an example from the model made by [Sarathy](https://github.com/comocheng/ChemCheck/tree/cx/ChemCheck/media/examples/2028-Sarathy):\
   {{% thumbnail "/images/GSoC_2019_images/missing_idx.png" alt="Missing index check" align="center" %}}<p class="text-center">Missing Index check</p>{{% /thumbnail %}}\
Another example is from the model made by [Wang](https://github.com/comocheng/ChemCheck/tree/cx/ChemCheck/media/examples/335-Wang):\
{{% thumbnail "/images/GSoC_2019_images/idx_out_of_position.png" alt="Index position check page" align="center" %}}<p class="text-center">Index position check</p>{{% /thumbnail %}}
   - For the lines starting with special or redundant characters which causes difficulty to cantera recognition, ChemCheck will show the position of the character and make the  suggestion to delete them. An example from model [032-cheng](https://github.com/comocheng/ChemCheck/tree/cx/ChemCheck/media/examples/032-Cheng):\
   {{% thumbnail "/images/GSoC_2019_images/redundant_character.png" alt="Special character check" align="center" %}}<p class="text-center">Special or redundant character check</p>{{% /thumbnail %}}\
   - If a model misses the transport data for a species, ChemCheck suggests users delete the transport file or delete the species from the mechanism file or manually add the transport data for the species which misses the transport data. Here is an example diagosing the model [111-Atef](https://github.com/comocheng/ChemCheck/tree/cx/ChemCheck/media/examples/111-Atef):\
   {{% thumbnail "/images/GSoC_2019_images/missing_transport_data.png" alt="Missing transport data check" align="center" %}}<p class="text-center">Missing transport data check</p>{{% /thumbnail %}}
   - If a reaction has two type of parameter for one species, for example, PLOG parameters and non pressure dependent arrhenius parameters, ChemCheck will suggest to delete one set of them, for instance, [038-Labbe-Zhao](https://github.com/comocheng/ChemCheck/tree/cx/ChemCheck/media/examples/038-Labbe-Zhao):\
   {{% thumbnail "/images/GSoC_2019_images/duplicate_parameters.png" alt="duplicate parameters check" align="center" %}}<p class="text-center">Duplicate reaction parameters check</p>{{% /thumbnail %}}
   - Errors like the indentation error in the first line of a species thermo data, Missing E in the the NASA polynomial parameters, and unexpected character in the middle of the thermo data, which causes the value error raised by cantera are hard to diagnose, so ChemCheck will suggest all possible reasons. This diagnosis is not very precise and could be improved in the future work. Here is the example [0325-Nawdiyal](https://github.com/comocheng/ChemCheck/tree/cx/ChemCheck/media/examples/0325-Nawdiyal):\
   {{% thumbnail "/images/GSoC_2019_images/indentation_error.png" alt="Indentation error check" align="center" %}}<p class="text-center">Indentations error, Missing E etc. check</p>{{% /thumbnail %}}

3. Chemical Error visualization:
   - NASA Polynomial discontinuity:
Some species in the model have NASA polynomial discontinuity, which means the values calculated from high temperature NASA polynomial parameters and low temperature NASA polynomial parameters at the mid of temperature range are not equal. The reason for this problem could be the wrong NASA polynomial parameter provided in the model or the mid temperature is chosen inappropriately. To visualize this, ChemCheck plots figures of the thermal properties of the error species with NASA polynomial discontinuity.
ChemCheck is able to check for NASA 7 polynomials now, and the check for NASA 9 polynomials will be added shortly. Here is the example model in [cantera ncm-2017-materials](https://github.com/Cantera/ncm-2017-materials/tree/master/mech_debug):\
{{% thumbnail "/images/GSoC_2019_images/NASA_Poly_discontinuity.png" alt="NASA polynomial discontinuity check" align="center" %}}<p class="text-center">NASA polynomial discontinuity check</p>{{% /thumbnail %}}
   - Negative sum of kinetic constants and A factor for pressure dependent reactions and duplicate reactions:
This problem has been discussed in [cantera user’s group](https://groups.google.com/forum/#!topic/cantera-users/zy4GOvsiYVM/discussion) and [cantera issues](https://github.com/Cantera/cantera-website/issues/77),
The pressure-dependent arrhenius rate expressions in cantera are calculated by logarithmically interpolating between Arrhenius rate expressions at various pressures. To calculate the rate expression at a certain pressure P between P1, P2 which are given in the thermo data for this pressure dependent reaction, it will need log k1 under pressure P1, log k2 under pressure P2 to plug in an equation in terms of the rate expression at pressure P.  Details are showing here. (https://cantera.org/science/reactions.html#pressure-dependent-arrhenius-rate-expressions-p-log) If there are more than one set of arrhenius parameter at P1 or P2, cantera will take the sum of reaction rate constants calculated from all sets of arrhenius parameter under this pressure, and take the logarithm of the sum of k. However, if the sum of k is negative, the logarithm of a negative number does not exist, so cantera throws a validation error. Similarly, the sum of k also needs to be positive for duplicate reactions.
To diagnose this, ChemCheck goes through all the pressure dependent reactions and duplicate reactions, calculate the sum of reaction rate constants under the same pressure at temperature `[200K, 500K, 1000K, 2000K, 10000K]` respectively. If the result is negative, the equation and the wrong arrhenius parameters for that equation temperature, and pressure will be shown on the website. It will also check if the A factor is negative for the pressure with only one set of parameters.
Here is the diagnosis example for [cantera issue 77](https://github.com/Cantera/cantera-website/issues/77):\
{{% thumbnail "/images/GSoC_2019_images/negative_pdep_sum_k.png" alt="Negative pressure dependent sum of k" align="center" %}}<p class="text-center">Negative sum of k for pressure dependent reactions</p>{{% /thumbnail %}}\
{{% thumbnail "/images/GSoC_2019_images/negative_duplicate_sum_k.png" alt="Negative sum of k for duplicate reactions" align="center" %}}<p class="text-center">Negative sum of k for duplicate reactions</p>{{% /thumbnail %}}
## Works need to be done:
Collision Violation Check: we are working on adding collision violation check for a kinetic model in yaml format. The collision limit calculation for bimolecular reaction  is mentioned in [’Violation of collision limit in recently published reaction models’](https://doi.org/10.1016/j.combustflame.2017.08.005) , However, this methodology may not be appropriate to apply on falloff reactions and three body reactions, so we are trying to explore a  methodology to calculate the collision limit for falloff and three body reactions. 
As we discussed before, the future check will be including the dead-end path way which is mentioned in https://doi.org/10.1016/j.combust%EF%AC%82ame.2014.05.001, and the CVODE errors explanation.
 

