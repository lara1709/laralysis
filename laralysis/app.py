import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from core.function_model import FunctionModel
from storage.database import init_db, save_function, load_functions
from core.sequence_model import SequenceModel

init_db()

functions = load_functions()

st.title("Laralysis - Math Visualizer")

st.subheader("Add a new function")
new_expr = st.text_input("Enter function in x")
if st.button("Add function"):
    if new_expr.strip() != "":
        try:
            f = FunctionModel(expr_str=new_expr)
            functions.append(f)
            save_function(f)
            st.success(f"Function '{new_expr}' added!")
        except Exception as e:
            st.error(f"Error: {e}")

st.subheader("Saved functions")
if functions:
    df = pd.DataFrame([{"Expression": f.expr_str} for f in functions])
    st.table(df)
else:
    st.info("No function saved yet")

st.subheader("Plot a function")
if functions:
    selected_expr = st.selectbox("Select function to plot", [f.expr_str for f in functions])
    f_to_plot = next(f for f in functions if f.expr_str == selected_expr)

    x_vals = np.linspace(-10, 10, 400)
    y_vals = [f_to_plot.evaluate(x) for x in x_vals]

    plt.figure(figsize=(6,4))
    plt.plot(x_vals, y_vals, label=f"{selected_expr}")

    y_deriv = [float(f_to_plot.derivative().subs(f_to_plot.var, x)) for x in x_vals]
    plt.plot(x_vals, y_deriv, label=f"Derivative of {selected_expr}", linestyle="--")

    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    st.pyplot(plt)
else:
    st.info("No function to plot")

st.subheader("Numerical analysis tools")

if functions:
    selected_func = st.selectbox("Select function for analysis", [f.expr_str for f in functions], key="analysis")
    f_analysis = next(f for f in functions if f.expr_str == selected_func)

    st.markdown("**Find Root**")
    guess = st.number_input("Initial guess for root:", value=0.0, key="guess")
    if st.button("Find Root"):
        root = f_analysis.find_root(guess)
        if root is not None:
            st.sucess(f"Approximate root: x = {root:.6f}")
        else:
            st.error("Couldnt find root")

    st.markdown("**Definite Integral**")
    a = st.number_input("Lower bound a:", value=0.0, key="a")
    b = st.number_input("Upper bound b:", value=1.0, key="b")
    if st.button("Compute Integral"):
        result = f_analysis.definite_integral(a, b)
        st.success(f"Definite integral  from {a} to {b}: {result:.6f}")

st.subheader("Sequences and Series")

new_seq = st.text_input("Enter a sequnece formula in n", key="seq_input")
start= st.number_input("Start index", value=0, key="seq_start")
end = st.number_input("End index", value=10, key="seq_end")

if st.button("Generate sequence"):
    try:
        seq = SequenceModel(new_seq, start=start, end=end)
        values = seq.generate()
        st.success(f"Sequence: {values}")
        st.line_chart(values)
    except Exception as e:
        st.error(f"Error: {e}")