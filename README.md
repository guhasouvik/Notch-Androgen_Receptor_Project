# Notch-Androgen_Receptor_Project
# Androgen Receptor Signaling Simulations

This repository provides Python scripts for simulating **single-cell** and **tissue-level** (multi-cell lattice) models of Notch-EMT-AR signaling.  

---

## Requirements

To run the simulations, you need:

- **Python** ≥ 2.6  
- The following Python packages:  
  - [NumPy](https://numpy.org/)  
  - [SciPy](https://scipy.org/)  
  - [Matplotlib](https://matplotlib.org/)  
  - [PyDSTool](http://www.ni.gsu.edu/~rclewley/PyDSTool/FrontPage.html)  

---
The files are: (1) aux_andro.py - auxiliary functions (2) singlecell.py - methods for the single cell simulations (3) multicell.py - methods for the multi-cell lattice simulations.
singlecell.py contains the code for the single cell simulation, while multi_cell.py contains the code for tissue-level simulations. Both programs rely on auxiliary functions contained in aux_andro.py, so that must be in the same folder when compiling single_cell.py/multi_cell.py (otherwise, the path .../aux_andro.py must be indicated). To compile, run python singlecell.py (or python multicell.py) on your terminal after entering in your work directory. 


For further questions about the code, please contact me (Souvik - souvik.guha.25@ucl.ac.uk)
