from abc import ABC, abstractmethod
from laralysis.core.base_model import BaseModel

class NumericalMethod(BaseModel, ABC):
    def __init__(self, name):
        super.__init__(name)

    def solve(self):
        pass
    