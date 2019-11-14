from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Population_Variance import variance
from Statistics.Std_dev import std_dev
from Statistics.Z_score import z_score
class Statistics(Calculator):
    result = 0

    def __init__(self):
        super().__init__()

    def mean(self, a, b, c, length):
        self.result = mean(a, b, c, length)
        return self.result

    def median(self, a, b, c):
        self.result = median(a, b, c)
        return self.result

    def mode(self, a, b, c, d):
        self.result = mode(a, b, c, d)
        return self.result

    def pop_variance(self, a, b, c):
        self.result = variance(a, b, c)
        return self.result

    def std_dev(self, a, b, c):
        self.result = std_dev(a, b, c)
        return self.result

    def z_score(self, a, b, c):
        self.result = z_score(a, b, c)
        return self.result