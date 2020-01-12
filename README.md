# atomPython - ENG
An Agent-Based Financial Platform

[ATOM](https://github.com/cristal-smac/atom) is a financial market simulation platform written in Java, powerful both from a functional point of view (multi-agent, multi-orders, multi-assets, intra and extra days, several price fixing, etc ...) and from a speed point of view. atomPython is a very simplified version, written in Python for educational purposes. In particular, it handles only one order (LimitOrder), has only one continuous price fixing and does not allow multi-day pricing. However, it is multi-agent and multi-assets, which allows many experiments on artificial markets.



Several notebooks are provided in order to get familiar with this platform

Team : P Mathieu, R Morvan, A Fleury ([CRISTAL Lab](http://www.cristal.univ-lille.fr), [SMAC team](https://www.cristal.univ-lille.fr/?rubrique27&eid=17), [Lille University](http://www.univ-lille.fr)) , O Brandouy ([Gretha](https://gretha.u-bordeaux.fr/), [Bordeaux University](https://www.u-bordeaux.fr/))

Contact : philippe.mathieu at univ-lille.fr


## Atom.ipynb
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cristal-smac/atomPython/master?filepath=Atom.ipynb)

A notebook to see the full range of the possibilities offered by this atom python version

## tp1.ipynb
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cristal-smac/atomPython/master?filepath=tp1.ipynb)

Introductory notebook to the handling of this platform

## tp2.ipynb
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cristal-smac/atomPython/master?filepath=tp2.ipynb)

Notebook d'introduction à l'écriture de code avec cette plateforme


# Available files

*atom.py*: main file, atom core

*testatom.py*: a simple test file to see the basis of what atom can do

*Atom.ipynb*: A notebook to see the full range of the possibilities offered by atom

*Agents.ipynb*: A notebook introducing agents that are more "evolved" than simple ZITs

*DeterministicArtificialTraders.ipynb*: A notebook introducing the three different kind of
Deterministic Artificial Traders that are described in "A deterministic behaviour for realistic price dynamics"
  
*OrderExecution.pdf/tex*: A short description about why it seems that there doesn't exist a total order on the set of limit orders
  that gives the permutation in which a sequence should be executed in order to maximize a given welfare
  
*OrderExecution.ipynb*: A notebook showing the code used to find counterexamples used in OrderExecution.pdf

*DrawOrderBooks.ipynb*: A notebook that generates some tikz code to draw an orderbook read in a trace file

**DrawOrderBooks.ipynb should not be run before OrderExecution.ipynb, as the latter generates a trace.dat file that is 
read by the first notebook**


*binary_heap.py*: A Python implementation of binary heaps used by atom.py

*data_processing.py*: Some functions that makes reading a trace file easier

# License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.
If not, see http://www.gnu.org/licenses/.
