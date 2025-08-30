import unittest
from demographic_data_analyzer import *

class TestDemographicDataAnalyzer(unittest.TestCase):

    def test_race_count(self):
        self.assertIsInstance(race_count, pd.Series)
        self.assertTrue('White' in race_count.index)

    def test_average_age_men(self):
        self.assertIsInstance(average_age_men, float)
        self.assertGreater(average_age_men, 0)

    def test_percentage_bachelors(self):
        self.assertIsInstance(percentage_bachelors, float)
        self.assertGreaterEqual(percentage_bachelors, 0)
        self.assertLessEqual(percentage_bachelors, 100)

    def test_higher_education_rich(self):
        self.assertIsInstance(higher_education_rich, float)
        self.assertGreaterEqual(higher_education_rich, 0)
        self.assertLessEqual(higher_education_rich, 100)

    def test_lower_education_rich(self):
        self.assertIsInstance(lower_education_rich, float)
        self.assertGreaterEqual(lower_education_rich, 0)
        self.assertLessEqual(lower_education_rich, 100)

    def test_min_work_hours(self):
        self.assertIsInstance(min_work_hours, int)
        self.assertGreater(min_work_hours, 0)

    def test_rich_percentage(self):
        self.assertIsInstance(rich_percentage, float)
        self.assertGreaterEqual(rich_percentage, 0)
        self.assertLessEqual(rich_percentage, 100)

    def test_highest_earning_country(self):
        self.assertIsInstance(highest_earning_country, str)
        self.assertTrue(len(highest_earning_country) > 0)

    def test_highest_earning_country_percentage(self):
        self.assertIsInstance(highest_earning_country_percentage, float)
        self.assertGreaterEqual(highest_earning_country_percentage, 0)
        self.assertLessEqual(highest_earning_country_percentage, 100)

    def test_top_IN_occupation(self):
        self.assertIsInstance(top_IN_occupation, str)
        self.assertTrue(len(top_IN_occupation) > 0)


if __name__ == '__main__':
    unittest.main()
