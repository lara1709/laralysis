# Laralysis-Math Visualizer

Laralysis is a Math Visualizer, that is very user friendly and interactive, everything is simple and easy to understand. It allows users to add functions, to visualize them and offers basic numerical analysis (finding roots, integrals, derivatives and sequences) so it is very helpful for students just like myself. I created it using Streamlit.
I made this project for my advanced coding class. I used my knowledge from previous classes (e.g. database, basics of coding, using Streamlit) and also gained a lot of knowledge trying to realise this project.

## Features

### 1.Manage your functions
- Add any functions
- Have a list of your functions, view them (no duplicates for a better overview)
- Delete functions 
All of the functions are saved in a simple database

### 2.Visualize functions
- Any saved function can be plotted
- Graphs will be generated 
The graphs are generated using matplotlib

### 3.Numerical Analysis
- Find the root (adding your initial guess), so finds an approximate x value for which the function becomes zero
This is done using numerical method.
- Calculate Integrals (add enter and start value), so calculates area under the curve

### 4.Sequences and Series
- Generates a numerical sequence, with a start and end index

## What was used
- Python
- Matplotlib
- SQLite
- NumPy
- Streamlit
- SymPy

## How to run Laralysis

- Install all the requirements (python and GitHub)
- Clone the repository on Github
- Install the python packages needed (see "What was used") (in the terminal type: pip install streamlit numpy matplotlib sympy)
- run streamlit (in the terminal type: streamlit run app.py)
- Now you can add, delete, view and plot your functions!
