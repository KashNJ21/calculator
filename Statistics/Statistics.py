from Calculator.Calculator import Calculator
from Statistics.Mean import mean

class Statistics(Calculator):
    result = 0

    def __init__(self):
        super().__init__()

    def mean(self, a, b, length):
        self.result = mean(a, b, length)
        return self.result



