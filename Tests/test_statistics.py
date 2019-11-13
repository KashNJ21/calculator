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
           self.assertEqual(self.statistics.mean(row['Value 1'], row['Value 2'], row['Value 3']), result)
           self.assertEqual(self.statistics.result, result)

    def test_results_property(self):
        self.assertEqual(self.statistics.result, 0)


if __name__ == '__main__':
    unittest.main()