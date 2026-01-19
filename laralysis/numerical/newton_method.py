from laralysis.numerical.numerical_methods import NumericalMethod

class NewtonMethod(NumericalMethod):

    def __init__(self, function_model, start_value, tolerance=1e-6, max_iter=100):
        super().__init__("Newton Method")
        self.function = function_model
        self.x = start_value
        self.tolerance = tolerance
        self.max_iter = max_iter

    def solve(self):
        x = self.x

        for _ in range(self.max_iter):
            f_x = self.function.evaluate(x)
            df_x = self.function.derivative().subs(self.function.var, x)

            if abs(df_x) < self.tolerance:
                 raise ValueError("Derivative is too small")
        
            x_new = x - f_x / float(df_x)

            if abs(x_new - x) < self.tolerance:
                 return x_new
        
            x = x_new

        raise ValueError("Didnt converge")