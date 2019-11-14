from Statistics.PopulationMean import population_mean
from Statistics.Sample_Standard_Deviation import sample_st_deviation
from Calculator.Subtraction import subtraction
from Calculator.Division import division


def z_score(data):
    x = 64
    u = population_mean(data)
    sample_sd = sample_st_deviation(data)
    y = subtraction(x, u)
    return division(sample_sd, y)