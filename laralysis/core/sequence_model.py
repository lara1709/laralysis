from .base_model import base_model
class SequenceModel(BaseModel):
    def __init__(self, name, values=None):
        super().__init__(name)
        self.values = values if values is not None else []

    def append(self, value):
        self.values.append(value)

    def mean(self):
        return sum(self.values)/len(self.values) if self.values else None
    
    def serialize(self):
        base = super().serialize()
        base.update({"values": self.values})
        return base
    def __repr__(self):
        return f"<SequenceModel {self.name}: {self.values}>"