import streamlit as st
from core.function_model import FunctionModel
from storage.database import load_functions, save_function
from viz.plotter import plot_functions

st.title("Laralysis")

functions = load_functions()

st.header("add new function")
expr = st.text_input("Function formula")
var_name = st.text_input("Variable name", value="x")

if st.button("Add function"):
    try:
        f = FunctionModel(expr_str0expr, var_name=var_name)
        functions.append(f)
        save_function(f)
        st.success(f"Function {expr} saved")
    except Exception as e:
        st.error(f"Error: {e}")

st.header("Saved functions")
if functions:
    for i, f in enumerate(functions, 1):
        st.write(f"{i}, {f}")

st.header("Plot function")
if functions:
    idx = st.number_input("Function number to plot", min_value=1, max_value=len(functions), value=1)
    selected = [functions[idx-1]]
    if st.button("Plot"):
        plot_functions(selected)