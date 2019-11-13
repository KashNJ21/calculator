from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
class Statistics(Calculator):
    result = 0

    def __init__(self):
        super().__init__()

    def mean(self, a, b, length):
        self.result = mean(a, b, length)
        return self.result

    def median(self, a, b, c):
        self.result = median(a, b, c)
        return self.result



