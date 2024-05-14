# Quantum Genetic Programming

This project uses Pyggi to synthesize quantum programs.





Required pip packages
jMetalpy
lxml
astor


Files to change:

Pyggi/base/patch.py

Pyggi/base/program.py
-Class RunResult OR Result
I would prefer to extend the RunResult class as that is what default pyggi uses


Tree.py

New classes to modify the AST tree 

XML_engine.py

Modify to support format of Quantum AST


General Changes:
We need to adapt the directory structure to make calls between pyggi and jmetal now that we are not nesting one inside the other.

We need to add the Quantum program / simulation into
Source/Quantum <- Rename to whatever is apporiate for the tool

