# Quantum Genetic Programming

This project uses Pyggi to synthesize quantum programs.

Required pip packages
pip install antlr4-python3-runtime==4.9.2 jMetalpy lxml astor pandas pytest

To run:

python Source/qgen.py 


To run with a benchmark program

python Source/qgen.py --project_path Benchmark/cl_adder

To select operators [TODO - confirm correctness]

python Source/qgen.py --project_path Benchmark/cl_adder --operators [QRepalcement, QInsert, QDelete]