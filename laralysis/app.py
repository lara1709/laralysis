import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from core.function_model import FunctionModel
from storage.database import init_db, save_function, load_functions, delete_function
from core.sequence_model import SequenceModel

init_db()
functions = load_functions()

st.set_page_config(page_title="Laralysis", layout="wide")

st.title("Laralysis - Math Visualizer")
st.markdown("### Functions")

col1, col2 = st.columns(2)

with col1:
   st.subheader("Add a new function")
   new_expr = st.text_input("Enter function in x", key="new_func")
   if st.button("Add function"):
       if new_expr.strip() != "":
           try:
               existing_exprs = [f.expr_str for f in functions]

               if new_expr in existing_exprs:
                   st.warning("This function was already saved")
               else:
                   f = FunctionModel(expr_str=new_expr)
                   functions.append(f)
                   save_function(f)
                   st.success(f"Function '{new_expr}' added!")
           except Exception as e:
               st.error(f"Error: {e}")

   st.markdown("---")
   st.subheader("Saved functions")

   if functions:
       func_to_delete = st.selectbox(
           "Select a function to delete",
           [f.expr_str for f in functions],
           key="delete_select"
       )

       if st.button("Deelete selected function"):
           try:
               delete_function(func_to_delete)
               st.success(f"Deleted function: {func_to_delete}")
               st.rerun()
           except Exception as e:
               st.error(f"Error deleting the function: {e}")

       st.markdown("**All saved functions:**")
       for f in functions:
           st.write("°", f.expr_str)

   else:
       st.info("No functions saved yet")
   

with col2:
    st.subheader("Plot a function")
    if functions:
        selected_expr = st.selectbox("Select function to plot", [f.expr_str for f in functions], key="plot_func")
        f_to_plot = next(f for f in functions if f.expr_str == selected_expr)

        x_vals = np.linspace(-10, 10, 400)
        y_vals = [f_to_plot.evaluate(x) for x in x_vals]

        plt.figure(figsize=(6,4))
        plt.plot(x_vals, y_vals, color="#FFB6C1", label=f"{selected_expr}")

        y_deriv = [float(f_to_plot.derivative().subs(f_to_plot.var, x)) for x in x_vals]
        plt.plot(x_vals, y_deriv, color="#FF69B4", linestyle="--", label=f"Derivative")

        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        st.pyplot(plt)
    else:
        st.info("No function saved")

with st.expander("Numerical Analysis tools"):
    if functions:
        selected_func = st.selectbox(
            "Select a function for analysis",
            [f.expr_str for f in functions],
            key="analysis"
        )
        f_analysis = next(f for f in functions if f.expr_str == selected_func)

        st.markdown("**Find Root")
        guess = st.number_input("Initial guess for root:", value=0.0, key="root_guess")
        if st.button("Find root", key="root_button"):
            try:
                root = f_analysis.find_root(guess)
                if root is not None:
                    st.success(f"Approximate root: x = {root:.6f}")
                else:
                    st.error("Couldnt find root")
            except Exception as e:
                st.error(f"Error: {e}")

        st.markdown("**Definite Integral**")
        a = st.number_input("Lower bound a:", value=0.0, key="int_a")
        b = st.number_input("Upper bound b :", value=1.0, key="int_b")
        if st.button("Compute Integral", key="integral_button"):
            try:
                result = f_analysis.definite_integral(a, b)
                st.success(f"Definite integral from {a} to {b}: {result:.6f}")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.info("No function saved yet")

with st.expander("Sequences and Series"):
    new_seq = st.text_input("Enter a sequence formula in n", key="seq_input")
    start = st.number_input("Start index", value=0, key="seq_start")
    end = st.number_input("End index", value=10, key="seq_end")

    if st.button("Generate sequence"):
        try:
            seq = SequenceModel(new_seq, start=start, end=end)
            values = seq.generate()
            st.success(f"Sequence: {values}")
            st.line_chart(values)
        except Exception as e:
            st.error(f"Error: {e}")