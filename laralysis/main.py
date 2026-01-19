from storage.database import load_functions, save_function
from core.function_model import FunctionModel
from viz.plotter import plot_functions
from storage.database import init_db
init_db()

def main():
    print("Welcome to laralysis")

    functions = load_functions()

    while True:
        print("\nWhat do you want to do?")
        print("1. Add new function")
        print("2. List functions / Plot functions")
        print("3. Exit")
        
        choice = input("Choose one option: ").strip()

        if choice == "1":
            expr = input("Enter a function formula: ").strip()
            var_name = input("Enter variable name (defaukt 'x'): ").strip() or "x"

            try:
                f = FunctionModel(expr_str=expr, var_name=var_name)
                functions.append(f)
                save_function(f)
                print(f"Function {expr} saved!")
            except Exception as e:
                print("Error:", e)
            
        elif choice == "2":
            if not functions:
                print("No functions saved yet")
            else:
                print("\nSaved functions:")
                for i, f in enumerate(functions, start=1):
                    print(f"{i}. {f}")

                nums = input("\nEnter function numbers to plot separated by commas: ")
                if nums:
                    try:
                        indices = [int(n.strip()) - 1 for n in nums.split(",")]
                        selected = [functions[i] for i in indices if 0 <= i < len(functions)]
                        show_deriv = input("Plot derivatives aswell? (y/n): ").lower() == "y"
                        save_plot = input("Save this plot as iamge? (y/n): ").lower() == "y"
                        if save_plot:
                            filename = input("Enter filename (default: plot.png): ").strip() or "plot.png"
                            plot_functions(selected, show_derivative=show_deriv, save=True, filename=filename)
                        else:
                            plot_functions(selected, show_derivative=show_deriv)
                    except Exception as e:
                        print("Invalid input:", e)

        elif choice == "3":
            print("Bye Bye")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()