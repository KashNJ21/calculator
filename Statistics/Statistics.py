from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Population_Variance import variance
from Statistics.PopulationMean import population_mean
from Statistics.Sample_Standard_Deviation import sample_st_deviation
from Statistics.ConfidenceInterval import confidence_interval
from Statistics.Proportion import proportion
from Statistics.Pvalue import p_value




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

    def population_mean(self):
        self.result = population_mean(self.data)
        return self.result

    def sample_st_deviation(self):
        self.result = sample_st_deviation(self.data)
        return self.result

    def confidence_interval(self):
        self.result = confidence_interval(self.data)
        return self.result

    def proportion(self, ):
        self.result = proportion()
        return self.result

    def p_value(self, ):
        self.result = p_value()
        return self.result

