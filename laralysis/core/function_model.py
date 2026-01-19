from sympy import symbols, sympify
from .base_model import BaseModel

class FunctionModel(BaseModel):
    def __init__(self, expr_str, var_name="x"):
        super().__init__(name="Function")
        self.var_name = var_name
        self.expr_str = expr_str
        self.var = symbols(var_name)

        try:
           self.expr = sympify(expr_str)
        except Exception as e:
            raise ValueError(f"Faulty formula: {expr_str}") 

    def evaluate(self, x_value):
        return float(self.expr.subs(self.var, x_value))
    
    def derivative(self):
        return self.expr.diff(self.var)
    
    def serialize(self):
        base = super().serialize()
        base.update({
            "expr_str": self.expr_str,
            "var_name": self.var_name
        })
        return base
    
    def __repr__(self):
        return f"<FunctionModel {self.expr_str}>"