from demographic_data_analyzer import *

def main():
    print("Race count:\n", race_count, "\n")
    print("Average age of men:", average_age_men, "\n")
    print("Percentage with Bachelor's degrees:", percentage_bachelors, "\n")
    print("Percentage with higher education earning >50K:", higher_education_rich, "\n")
    print("Percentage without higher education earning >50K:", lower_education_rich, "\n")
    print("Minimum work hours per week:", min_work_hours, "\n")
    print("Percentage of rich among those who work minimum hours:", rich_percentage, "\n")
    print("Country with highest % earning >50K:", highest_earning_country)
    print("Highest percentage:", highest_earning_country_percentage, "\n")
    print("Top occupation in India for >50K:", top_IN_occupation, "\n")

if __name__ == "__main__":
    main()
