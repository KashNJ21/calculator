from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_population_mean(self):
        test_data = CsvReader("Tests/Data/mean.csv").data
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.mean(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4']), result)
           self.assertEqual(self.statistics.result, result)

    def test_median(self):
        test_data = CsvReader("Tests/Data/median.csv").data
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.median(row['Value 1'], row['Value 2'], row['Value 3']), result)
           self.assertEqual(self.statistics.result, result)

    def test_mode(self):
        test_data = CsvReader("Tests/Data/mode.csv").data
        for row in test_data:
           result = [float(row['Result'])]
           self.assertAlmostEqual(self.statistics.mode(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4']), result)
           self.assertAlmostEqual(self.statistics.result, result)

    def test__pop_variance(self):
        test_data = CsvReader("Tests/Data/pop_variance.csv").data
        for row in test_data:
           result = float(row['Result'])
           self.assertAlmostEqual(self.statistics.pop_variance(row['Value 1'], row['Value 2'], row['Value 3']), result)
           self.assertAlmostEqual(self.statistics.result, result)

    def test_p_value(self):
        test_data = CsvReader('Tests/Data/just_age.csv').data
        test_result = CsvReader('Tests/Data/Age_Results.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.p_value, float(row['Age']))
            self.assertEqual(self.statistics.result, test_result(row['PValue']))

    def sample_st_deviation(self):
        test_data = CsvReader('Tests/Data/just_age.csv').data
        test_result = CsvReader('Test/Data/Age_Results.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.p_value, float(row['Sample SD']))
            self.assertEqual(self.statistics.result, test_result(row['Sample SD']))

    def pop_standard_dev(self):
        test_data = CsvReader('Tests/Data/just_age.csv').data
        test_result = CsvReader('Test/Data/Age_Results.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.p_value, float(row['Sample SD']))
            self.assertEqual(self.statistics.result, test_result(row['Sample SD']))

    def proportion(self):
        test_data = CsvReader('Tests/Data/just_age.csv').data
        test_result = CsvReader('Test/Data/Age_Results.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.p_value, float(row['Proportion']))
            self.assertEqual(self.statistics.result, test_result(row['Proportion']))


    def test_results_property(self):
        self.assertEqual(self.statistics.result, 0)


if __name__ == '__main__':
    unittest.main()