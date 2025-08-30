import unittest
from demographic_data_analyzer import calculate_demographic_data

class TestDemographicDataAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.results = calculate_demographic_data(print_data=False)
    
    def test_race_count(self):
        self.assertTrue('White' in self.results['race_count'])
        self.assertTrue('Black' in self.results['race_count'])

    def test_average_age_men(self):
        self.assertIsInstance(self.results['average_age_men'], float)

    def test_percentage_bachelors(self):
        self.assertIsInstance(self.results['percentage_bachelors'], float)

    def test_percentage_higher_education_rich(self):
        self.assertIsInstance(self.results['percentage_higher_education_rich'], float)

    def test_percentage_lower_education_rich(self):
        self.assertIsInstance(self.results['percentage_lower_education_rich'], float)

    def test_min_work_hours(self):
        # Ensure it’s a Python int, not numpy.int64
        self.assertIsInstance(self.results['min_work_hours'], int)

    def test_rich_percentage_min_workers(self):
        self.assertIsInstance(self.results['rich_percentage_min_workers'], float)

    def test_highest_earning_country(self):
        self.assertIsInstance(self.results['highest_earning_country'], str)

    def test_highest_earning_country_percentage(self):
        self.assertIsInstance(self.results['highest_earning_country_percentage'], float)

    def test_top_IN_occupation(self):
        self.assertIsInstance(self.results['top_IN_occupation'], (str, type(None)))

if __name__ == '__main__':
    unittest.main()
