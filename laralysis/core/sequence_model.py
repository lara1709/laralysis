from .base_model import BaseModel

class SequenceModel(BaseModel):
    def __init__(self, formula_str, var_name="n", start=0, end=10):
        super().__init__(name="Sequence")
        self.formula_str = formula_str
        self.var_name = var_name
        self.start = start
        self.end = end

        self.func = lambda n: eval(formula_str)

    def generate(self):
        return [self.func(n) for n in range(self.start, self.end + 1)]

    def serialize(self):
        base = super().serialize()
        base.update({
            "formula_str": self.formula_str,
            "var_name": self.var_name,
            "start": self.start,
            "end": self.end
            })
        return base
    def __repr__(self):
        return f"<SequenceModel {self.formula_str} from {self.start} to {self.end}>"