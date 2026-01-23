from sympy import symbols, sympify, integrate

class FunctionModel:
    def __init__(self, expr_str, var_name="x"):
        self.var_name = var_name
        self.expr_str = expr_str
        self.var = symbols(var_name)
        self.expr = sympify(expr_str)

    def evaluate(self, x_value):
        return float(self.expr.subs(self.var, x_value))
    
    def derivative(self):
        return self.expr.diff(self.var)
    
    def find_root(self, guess=0.0):
        x = self.var
        f = self.expr
        f_prime = self.derivative()
        tol = 1e-6
        max_iter = 100
        x_val = guess

        for _ in range(max_iter):
            fx = float(f.subs(x, x_val))
            fpx = float(f_prime.subs(x, x_val))
            if fpx == 0:
                break
            x_new = x_val - fx/fpx
            if abs(x_new - x_val) < tol:
                return x_new
            x_val = x_new

        return None
        
    def definite_integral(self, a, b):
        return float(integrate(self.expr, (self.var, a, b)))
    
    def serialize(self):
        return {
            "expr_str": self.expr_str,
            "var_name": self.var_name
        }