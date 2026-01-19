import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def plot_functions(function_models, show_derivative=False, save=False, filename="plot.png"):
    x_vals = np.linspace(-10, 10, 400)
    plt.figure(figsize=(10,6))

    colors = plt.cm.tab10.colors
    for i, f in enumerate(function_models):
        color = colors[i % len(colors)]

        y_vals = []
        for x in x_vals:
            try:
                y_vals.append(f.evaluate(x))
            except Exception:
                y_vals.append(None)

        plt.plot(x_vals, y_vals, label=f"$f_{i+1}(x) = {f.expr_str}$", color=color, linewidth=2)

        if show_derivative:
            deriv = f.derivative()
            dy_vals = [float(deriv.subs(f.var, x)) for x in x_vals]
            plt.plot(x_vals, dy_vals, linestyle='--',color=color, linewidth=1.5, label=f"$f_{i+1}'(x)$")

    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.title("Laralysis Function Plot", fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, linestyle=':', linewidth=0.8)
    plt.tight_layout()

    if save:
        folder = Path(__file__).parent / "plots"
        folder.mkdir(exist_ok=True)
        file_path = folder / filename
        plt.savefig(file_path)
        print(f"Plot saved as {file_path}")
        
    plt.show()
    
    